from PIL import Image, ImageFilter
import sys


def run(filename):


    MIN_LAT = 0; MIN_LNG = 0
    MAX_LAT = 0; MAX_LNG = 0

    MAX_X = 0; MAX_Y = 0

    colors = []

    distant_lat_lng = []

    color_rgb = [
        (255, 0, 0), # RED
        (255, 69, 0), # Orange red
        (255, 99, 71), # Tomato
        (255, 127, 80), # Coral
        (255, 255, 0), # Yellow
        (255, 215, 0), # Gold
        (218, 165, 32), # Goldenrod
        (0, 255, 0), # Green
        (50, 205, 50), # Lime green
        (34, 139, 34), # Forest green
        (0, 255, 255), # Cyan
        (64, 224, 208),
        (0, 206, 209),
        (0, 0, 255), # Blue
        (0, 0, 205) # Medium Blue
    ]


    with open('min_max.txt', 'r') as file:
        for line in file:
            if not line[0].isdigit():
                continue
            MIN_LAT, MIN_LNG, MAX_LAT, MAX_LNG = line.strip().split()



    with open(filename, 'r') as inf:
        for line in inf:
            if not line[0].isdigit():
                continue

            dist, x_coordinate, y_coordinate = line.strip().split()
            distant_lat_lng.append([int(dist), float(x_coordinate), float(y_coordinate)])

    with open('size_image.txt', 'r') as file:
        for line in file:
            if not line[0].isdigit():
                continue
            MAX_X, MAX_Y = line.strip().split()
    MAX_X = int(MAX_X)
    MAX_Y = int(MAX_Y)



    def color(val):
        if val <= 140:
            return color_rgb[0]
        elif val <= 280:
            return color_rgb[1]
        elif val <= 420:
            return color_rgb[2]
        elif val <= 560:
            return color_rgb[3]
        elif val <= 700:
            return color_rgb[4]
        elif val <= 840:
            return color_rgb[5]
        elif val <= 980:
            return color_rgb[6]
        elif val <= 1120:
            return color_rgb[7]
        elif val <= 1260:
            return color_rgb[8]
        elif val <= 1400:
            return color_rgb[9]
        elif val <= 1540:
            return color_rgb[10]
        elif val <= 1680:
            return color_rgb[11]
        elif val <= 1820:
            return color_rgb[12]
        elif val <= 1960:
            return color_rgb[13]
        elif val > 1960:
            return color_rgb[14]


    image = Image.new("RGBA", (MAX_X, MAX_Y))

    IM = image.load()
    iter = 0
    p = 0
    processing = int((MAX_X * MAX_Y) / 100)
    present = 1

    for x in range(MAX_X):
        for y in range(MAX_Y):
            IM[x, y] = color(distant_lat_lng[iter][0])
            iter += 1
            p += 1
            if p >= processing:
                print('', end='\r')
                print(str(present) + '%', end='')
                present += 1
                p = 0

    rotate = image.rotate(90, expand=True)
    blured = rotate.filter(ImageFilter.GaussianBlur(3))
    blured.save("HeatMap.png", "PNG")


if __name__ == '__main__':
    if sys.argv[1] == 'help':
        print("***Программа для создания тепловой карты***")
        print("-В качестве опции передать имя файла в котором записанны данные, необходимые для построения рисунка")
    else:
        run(sys.argv[1])
