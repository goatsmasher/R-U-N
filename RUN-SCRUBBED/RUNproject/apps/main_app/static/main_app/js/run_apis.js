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

function initialize() {
    var defaultBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(47.6062, -122.3321)
    );
    var origin_input = document.getElementById('saddr');
    var destination_input = document.getElementById('daddr');

    var options = {
    bounds: defaultBounds,
    componentRestrictions: {country: 'us'}
    };

    var autocomplete_origin = new google.maps.places.Autocomplete(origin_input, options);
    var autocomplete_destination = new google.maps.places.Autocomplete(destination_input, options);
}