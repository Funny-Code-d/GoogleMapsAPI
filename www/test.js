function initialize()
{
	var latlng = new google.maps.LatLng(55.014879, 82.948738);
    var myOptions = {
      zoom: 13,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    google.maps.event.addListener(map, 'bounds_changed', function () {
        console.log(map.getBounds());
        console.log(map.getZoom());
        console.log(map.getCenter());
    });
}