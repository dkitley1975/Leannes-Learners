function initMap() {
	const map = new google.maps.Map(document.getElementById('map'), {
		zoom: 12,
		center: {
			lat: 53.6356968,
			lng: -1.8108689,
		},
	});
	const trafficLayer = new google.maps.TrafficLayer();

	trafficLayer.setMap(map);
}
