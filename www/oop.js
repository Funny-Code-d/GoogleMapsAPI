// function initialize() {
// var moscow = new google.maps.LatLng(55.763585,37.560883);
// var myOptions = {
// 	zoom: 10,
//  	center: moscow,
// 	mapTypeId: google.maps.MapTypeId.ROADMAP
// 	};
// var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

// var point1 = new google.maps.LatLng(55.763525,37.560893);
// var marker = new google.maps.Marker({
//  	position: point1, map: map, title: 'Пробная точка!'
// 	});

// google.maps.event.addListener(marker, 'click', function() {
//   	alert("Test addListener")
//   	//document.location='http://4xpro.ru';
// 	});
// }

MyMap = function () { 
self = this; // потребуется для ссылки на экземпляр MyMap во вложенных функциях 
this.map = new google.maps.Map(document.getElementById("map_canvas"), { zoom: 10, center: {lat: 55.763585, lng: 37.560883}, // можно не создавать объект LatLng явно, а использовать литерал такого вида mapTypeId: google.maps.MapTypeId.ROADMAP }); 
this.markers = new Array; 
this.markers[0] = new google.maps.Marker({ position: new google.maps.LatLng(55.763525,37.560893), // опять обходимся без дополнительной переменной 
map: this.map, title: 'Пробная точка!' }); // сюда будет добавляться новый код 
}; 
myMap = new MyMap; 
google.maps.event.addDomListener(window, 'load', myMap);