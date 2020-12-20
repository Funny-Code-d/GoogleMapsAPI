function initialize() {
var moscow = new google.maps.LatLng(55.763585,37.560883);
var myOptions = {
	zoom: 10,
 	center: moscow,
	mapTypeId: google.maps.MapTypeId.ROADMAP
	};
var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

var point1 = new google.maps.LatLng(55.763525,37.560893);
var marker = new google.maps.Marker({
 	position: point1, map: map, title: 'Пробная точка!'
	});

google.maps.event.addListener(marker, 'click', function() {
  	alert("Test addListener")
  	//document.location='http://4xpro.ru';
	});
}