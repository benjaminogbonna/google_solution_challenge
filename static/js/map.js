//javascript.js
//set map options
var myLatLng = { lat: 9.0765, lng: 7.3986 };
var mapOptions = {
    center: myLatLng,
    zoom: 7,
    mapTypeId: google.maps.MapTypeId.ROADMAP

};

//create map
var map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

//create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

//create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer();

//bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);


//define calcRoute function
function calcRoute() {
    //create request
    var request = {
        origin: document.getElementById("from").value,
        destination: document.getElementById("to").value,
        travelMode: google.maps.TravelMode.DRIVING, //WALKING, BYCYCLING, TRANSIT
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }

    //pass the request to the route method
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {

            //Get distance and time
            const output = document.querySelector('#output');
            output.innerHTML = "<div class='alert-info'>From: " + document.getElementById("from").value + " to " + document.getElementById("to").value + ".<br /> Distance <i class='fa fa-road'></i> : " + result.routes[0].legs[0].distance.text + ".<br />Duration <i class='fa fa-clock-o'></i> : " + result.routes[0].legs[0].duration.text + ".</div>";

            //display route
            directionsDisplay.setDirections(result);
        } else {
            //delete route from map
            directionsDisplay.setDirections({ routes: [] });
            //center map in Nigeria
            map.setCenter(myLatLng);

            //show error message
            output.innerHTML = "<div class='alert-danger'><i class='fas fa-exclamation-triangle'></i> Could not retrieve trip details.</div>";
        }
    });

}

//create autocomplete objects for all inputs
var options = {
//    fields: ["formatted_address", "geometry", "name"]
    types: ['(cities)']
//    types: ['(establishment)', '(address)', '(cities)', '(regions)']
}

var input1 = document.getElementById("id_start");
//var input1 = document.getElementById("postForm").elements['start'].id = 'from';
var autocomplete1 = new google.maps.places.Autocomplete(input1, options);

var input2 = document.getElementById("id_destination");
//var input2 = document.getElementById("postForm").elements['destination'].id = 'to';
var autocomplete2 = new google.maps.places.Autocomplete(input2, options);


// Get current location
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}


// Create marker
var marker = new google.maps.Marker({
  map: map,
  position: new google.maps.LatLng(8.9807, 7.1805),
  title: 'VIP'
});

// Add circle overlay and bind to marker
var circle = new google.maps.Circle({
  map: map,
  radius: 500,    // 10 miles in metres
  fillColor: '#AA0000',
  fillOpacity: 0.2,
  strokeColor: "#FF0000",
  strokeOpacity: 0.8,
  strokeWeight: 2,
});
circle.bindTo('center', marker, 'position');