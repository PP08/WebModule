/**
 * Created by phucphuong on 4/13/17.
 */
var g_average_values;
var g_points;
var markers;
var trackers;
var circles;
var mymap_mul;

function initialize_map_mul(points, average_values, location) {

    g_average_values = average_values;
    g_points = points;

    setHeightForMap();

    mymap_mul = L.map('mapid-mul').setView(location, 18);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibGFuY2Vsb2Z0MTAwOCIsImEiOiJjajE4OXExcWkwMDRyMzJwcDNsdDIzMzU4In0.1JIG2H6f-CZ572Wmzxm77g', {
        maxZoom: 20,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.streets'
    }).addTo(mymap_mul);

    trackers = new L.FeatureGroup();
    circles = new L.FeatureGroup();
    markers = new L.FeatureGroup();

    // console.log('received data: ' + points);

    addTrackers(points, average_values);

}

function setHeightForMap() {
    // console.log('triggered');
    var height = $(window).height();
    var offset = $('#top-nav-bar').height();
    $('div#mapid-mul').css({'height': height - offset, 'width': $(window).width()});
}

function addTrackers(points, average_values) {

    // console.log("points lenght " + points.length);

    for (var i = 0; i < points.length; i++) {
        var polyline_points = [];
        // console.log('point ' + i + ' length: ' + points[i].length);
        for (var j = 0; j < points[i].length; j++) {

            var point = new L.LatLng(points[i][j]['fields'].latitude, points[i][j]['fields'].longitude);
            polyline_points.push(point);
            var circle = L.circle(point, {
                color: '#F5F5F5',
                fillColor: '#57B2F1',
                fillOpacity: 1,
                radius: 1,
                weight: 4
            });
            circle.bindPopup("<p class='center-align'><b>SPL: " + points[i][j]['fields'].spl_value + " dB</b></p><br><div class='center-div'>" +
                "<button class='btn' id='btn-dtm-" + i + "' onClick='get_details_multiple(this.id)' >" +
                "Details</button></div>");

            circles.addLayer(circle);
        }
        // console.log('points: ' + polyline_points);

        var start_point_marker = L.marker(polyline_points[0]);
        var end_point_marker = L.marker(polyline_points[polyline_points.length - 1]);

        start_point_marker.bindPopup("<p class='center-align'><b>Start Point</b></p><p class='center-align'>" +
            "Average SPL: " + average_values[i]['fields'].average_spl + " dB</p><br><div class='center-div'>" +
            "<button class='btn' id='btn-dtm-" + i + "' onClick='get_details_multiple(this.id)' >" +
            "Details</button></div>");

        end_point_marker.bindPopup("<p class='center-align'><b>End Point</b></p><p class='center-align'>" +
            "Average SPL: " + average_values[i]['fields'].average_spl + " dB</p><br><div class='center-div'>" +
            "<button class='btn' id='btn-dtm-" + i + "' onClick='get_details_multiple(this.id)' >" +
            "Details</button></div>");

        markers.addLayer(start_point_marker);
        markers.addLayer(end_point_marker);

        var pathLine = new L.Polyline(polyline_points, {
            color: 'red',
            weight: 4,
            opacity: 0.7,
            smoothFactor: 1
        });

        pathLine.bindPopup("<p class='center-align'><b>Average SPL: " + average_values[i]['fields'].average_spl + " dB</b></p><br><div class='center-div'>" +
            "<button class='btn' id='btn-dtm-" + i + "' onClick='get_details_multiple(this.id)' >" +
            "Details</button></div>");

        trackers.addLayer(pathLine);
    }

    mymap_mul.addLayer(trackers);
    mymap_mul.addLayer(circles);
    mymap_mul.addLayer(markers);
}

function get_details_multiple(btn_id) {

    var clicked_id = btn_id.split('-')[2];

    var modalDetails = document.getElementById('modal-mul');
    var modal_template = Handlebars.compile(document.getElementById('modal-template-mul').innerHTML);

    var context = {values: g_average_values[clicked_id]};

    // console.log(context);

    modalDetails.innerHTML = modal_template(context);

    $('.modal').modal();
    $('#modal-detail-mul').modal('open');


    //set the height
    var div_table = document.getElementById("table-details-mul");
    var height = $(div_table).height();
    var width = $(div_table).width();
    $("div#graphs-mul").css("height", height);

    renderGraphsMul(width, height, clicked_id);
}

