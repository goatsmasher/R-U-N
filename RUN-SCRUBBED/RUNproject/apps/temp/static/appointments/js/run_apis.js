// This example requires the Places library. Include the libraries=places
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

      function initMap() {
        // var map = new google.maps.Map(document.getElementById('map'), {
        //   center: {lat: -33.8688, lng: 151.2195},
        //   zoom: 13
        // });
        var input = /** @type {!HTMLInputElement} */(
            document.getElementById('pac-input'));

        // var types = document.getElementById('type-selector');
        // map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
        // map.controls[google.maps.ControlPosition.TOP_LEFT].push(types);

        var autocomplete = new google.maps.places.Autocomplete(input);
        // autocomplete.bindTo('bounds', map);

        // var infowindow = new google.maps.InfoWindow();
        // var marker = new google.maps.Marker({
        //   map: map,
        //   anchorPoint: new google.maps.Point(0, -29)
        // });

        autocomplete.addListener('place_changed', function() {
          infowindow.close();
          marker.setVisible(false);
          var place = autocomplete.getPlace();
          if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
          }

          // If the place has a geometry, then present it on a map.
        //   if (place.geometry.viewport) {
        //     map.fitBounds(place.geometry.viewport);
        //   } else {
        //     map.setCenter(place.geometry.location);
        //     map.setZoom(17);  // Why 17? Because it looks good.
        //   }
        //   marker.setIcon(/** @type {google.maps.Icon} */({
        //     url: place.icon,
        //     size: new google.maps.Size(71, 71),
        //     origin: new google.maps.Point(0, 0),
        //     anchor: new google.maps.Point(17, 34),
        //     scaledSize: new google.maps.Size(35, 35)
        //   }));
        //   marker.setPosition(place.geometry.location);
        //   marker.setVisible(true);

          var address = '';
          if (place.address_components) {
            address = [
              (place.address_components[0] && place.address_components[0].short_name || ''),
              (place.address_components[1] && place.address_components[1].short_name || ''),
              (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
          }

          infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        //   infowindow.open(map, marker);
        });

        // Sets a listener on a radio button to change the filter type on Places
        // Autocomplete.
        function setupClickListener(id, types) {
          var radioButton = document.getElementById(id);
          radioButton.addEventListener('click', function() {
            autocomplete.setTypes(types);
          });
        }

        setupClickListener('changetype-all', []);
        setupClickListener('changetype-address', ['address']);
        setupClickListener('changetype-establishment', ['establishment']);
        setupClickListener('changetype-geocode', ['geocode']);
      }




function janrain() {
    if (typeof window.janrain !== 'object') window.janrain = {};
    if (typeof window.janrain.settings !== 'object') window.janrain.settings = {};

    janrain.settings.tokenUrl = '__REPLACE_WITH_YOUR_TOKEN_URL__';

    function isReady() { janrain.ready = true; };
    if (document.addEventListener) {
    document.addEventListener("DOMContentLoaded", isReady, false);
    } else {
    window.attachEvent('onload', isReady);
    }

    var e = document.createElement('script');
    e.type = 'text/javascript';
    e.id = 'janrainAuthWidget';

    if (document.location.protocol === 'https:') {
    e.src = 'https://rpxnow.com/js/lib/r-u-n/engage.js';
    } else {
    e.src = 'http://widget-cdn.rpxnow.com/js/lib/r-u-n/engage.js';
    }

    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(e, s);
}

// function initialize() {
//     var defaultBounds = new google.maps.LatLngBounds(
//     new google.maps.LatLng(47.6062, -122.3321)
//     );
//     var origin_input = document.getElementById('saddr');
//     var destination_input = document.getElementById('daddr');
//
//     var options = {
//     bounds: defaultBounds,
//     componentRestrictions: {country: 'us'}
//     };
//
//     var autocomplete_origin = new google.maps.places.Autocomplete(origin_input, options);
//     var autocomplete_destination = new google.maps.places.Autocomplete(destination_input, options);
// }
