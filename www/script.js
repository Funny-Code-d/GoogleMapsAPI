//------------------------------------------------------------------
function initMap() {
//-------------------------------------------------------------------
	var element = document.getElementById("map")
	var opt = {
		center: {lat: 55.7558, lng: 37.6173},
		zoom: 3,
		mapId: '1234'
	};
	var myMap = new google.maps.Map(element, opt);
//--------------------------------------------------------------------
	addMarker({
		coordinates: {lat: 55.7558, lng: 37.6173},
		info: "<h3>Moscow</h3>"
	});
	addMarker({
		coordinates: {lat: 55.030199, lng: 82.92043},
		//info: "<h3>Novosibirsk</h3>"
		info: latlng2distance(55.7558, 37.6173, 55.030199, 82.92043)
	});
//--------------------------------------------------------------------

    function latlng2distance(lat1, long1, lat2, long2) {
        //радиус Земли
        var R = 6372795;
        //перевод коордитат в радианы
        lat1 *= Math.PI / 180;
        lat2 *= Math.PI / 180;
        long1 *= Math.PI / 180;
        long2 *= Math.PI / 180;
        //вычисление косинусов и синусов широт и разницы долгот
        var cl1 = Math.cos(lat1);
        var cl2 = Math.cos(lat2);
        var sl1 = Math.sin(lat1);
        var sl2 = Math.sin(lat2);
        var delta = long2 - long1;
        var cdelta = Math.cos(delta);
        var sdelta = Math.sin(delta);
        //вычисления длины большого круга
        var y = Math.sqrt(Math.pow(cl2 * sdelta, 2) + Math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2));
        var x = sl1 * sl2 + cl1 * cl2 * cdelta;
        var ad = Math.atan2(y, x);
        var dist = ad * R; //расстояние между двумя координатами в метрах
        return dist
    }


//--------------------------------------------------------------------
	function addMarker(date)
	{	
		var marker = new google.maps.Marker({
			position: date.coordinates,
			map: myMap
		});

		if (date.info)
		{
			var infoWindow = new google.maps.InfoWindow({
				content: date.info
			});
			marker.addListener("click", function(){
				infoWindow.open(myMap, marker);
			})
		}
	}
//--------------------------------------------------------------------	
	}



//--------------------------------------------------------------------

