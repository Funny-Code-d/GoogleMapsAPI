import math
from time import sleep
import sys
import os
#--------------------------------------------------------------------------------------------------
# # degrees to radians
def deg2rad(degrees):
    return math.pi*degrees/180.0

#--------------------------------------------------------------------------------------------------
# # radians to degrees
def rad2deg(radians):
    return 180.0*radians/math.pi


#-------------------------------------------------------------------------------------------------
# # Semi-axes of WGS-84 geoidal reference
WGS84_a = 6378137.0  # Major semiaxis [m]
WGS84_b = 6356752.3  # Minor semiaxis [m]

# # Earth radius at a given latitude, according to the WGS-84 ellipsoid [m]
def WGS84EarthRadius(lat):
    # http://en.wikipedia.org/wiki/Earth_radius
    An = WGS84_a*WGS84_a * math.cos(lat)
    Bn = WGS84_b*WGS84_b * math.sin(lat)
    Ad = WGS84_a * math.cos(lat)
    Bd = WGS84_b * math.sin(lat)
    return math.sqrt( (An*An + Bn*Bn)/(Ad*Ad + Bd*Bd) )


#--------------------------------------------------------------------------------------------------
# Bounding box surrounding the point at given coordinates,
# assuming local approximation of Earth surface as a sphere
# of radius given by WGS84
def boundingBox(latitudeInDegrees, longitudeInDegrees, halfSideInKm):
    lat = deg2rad(latitudeInDegrees)
    lon = deg2rad(longitudeInDegrees)
    halfSide = 1000*halfSideInKm

#    Radius of Earth at given latitude
    radius = WGS84EarthRadius(lat)
#    Radius of the parallel at given latitude
    pradius = radius*math.cos(lat)

    latMin = lat - halfSide/radius
    latMax = lat + halfSide/radius
    lonMin = lon - halfSide/pradius
    lonMax = lon + halfSide/pradius
    return (rad2deg(latMin), rad2deg(lonMin), rad2deg(latMax), rad2deg(lonMax))



#---------------------------------------------------------------------------------------------------
#Задаётся центр прямоугольника
#И вычисляются его пределы
#Последним парамером задаётся дистанция от цетра до края прямоугольника (в км)
MIN_LAT, MIN_LNG, MAX_LAT, MAX_LNG = boundingBox(55.013787, 82.948433, 2)


#Запись данных в файл
#Эти данные нужны программе для создания изображения
with open("min_max.txt", "w") as file:
    file.write(str(MIN_LAT) + ' ' + str(MIN_LNG) + ' ' + str(MAX_LAT) + ' ' + str(MAX_LNG))



#---------------------------------------------------------------------------------------------------
#Функция для расчёта дистанции от точки до точки (возвращает значение в метрах)
def distance(LAT1, LNG1, LAT2, LNG2):
    radius = 6372795
    lat1 = LAT1 * math.pi / 180
    lat2 = LAT2 * math.pi / 180
    lng1 = LNG1 * math.pi / 180
    lng2 = LNG2 * math.pi /180

    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)

    delta = lng2 - lng1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)

    y = math.sqrt(math.pow(cl2 * sdelta, 2) + math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
    x = sl1 * sl2 + cl1 * cl2 * cdelta
    ad = math.atan2(y, x)
    dist = ad * radius
    return dist


#-------------------------------------------------------------------------------------------------------
#Основная функция программы
#Создаёт файл и записывает в него данные
#----------------------------------------------
#    Дистанция     Долгота(lat)     Широта(lng)
#----------------------------------------------
#В функции происходит:
#Создаётся 2 списка с коорднатами базовых станций
#Находиться дистанция от точки до ближайшей станции и записывается в файл
#В файл сохраняются данные необходимые для определения размера изображения
#

def create_file(filename1, filename2):
    processing = int(((MAX_LAT - MIN_LAT) / 0.0001) * ((MAX_LNG - MIN_LNG) / 0.0001) / 100)
    persent = 1
    x = MIN_LAT
    y = MIN_LNG
    x_coord = []
    y_coord = []
    minimum = 10000
    maximum = -1
    iter = 0
    file = open(filename1, 'w+')
    file_xy = open(filename2, 'r')
    base_station_x = []
    base_station_y = []
    with open(filename2) as inf:
        for line in inf:
            if not line[0].isdigit():
                continue

            x_coordinate, y_coordinate = line.strip().split()
            base_station_x.append(float(x_coordinate))
            base_station_y.append(float(y_coordinate))
    check_x = 0
    check_y = 0
    iter = 0
    print('[', end='')
    while x < MAX_LAT:
        y = MIN_LNG
        while y < MAX_LNG:
            minimum_dist_touch = 100000
            maximum = -1
            for i in range(len(base_station_x)):
                d = distance(x,  y, base_station_x[i], base_station_y[i])
                if d < minimum_dist_touch:
                    minimum_dist_touch = d
                if d > maximum:
                    maximum = d
            file.write('%s %.9s %.9s\n' % (int(minimum_dist_touch), x, y))
            x_coord.append(x)
            y_coord.append(y)
            y += 0.0001
            check_y += 1
            iter += 1
            if iter > processing:
                print('', end='\r')
                print(str(persent) + '%', end='')
                persent += 1
                iter = 0
        x += 0.0001
        check_x += 1
    if persent  >= 100:
        print('file completed successfully')
    with open("size_image.txt", 'w') as file:
        file.write(str(check_x) + ' ' + str(int(check_y/check_x)))

if __name__ == '__main__':
    if sys.argv[1] == 'help':
        print("В качестве параметров передать названия файлов")
        print('1. Куда записывать данные (файл будет перезаписан)\n2. Откуда брать координаты базовых станций')
    else:
        create_file(sys.argv[1], sys.argv[2])
