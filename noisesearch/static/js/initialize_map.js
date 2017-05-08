/**
 * Created by phucphuong on 4/13/17.
 */
var g_points;
var markers;
var mymap;

function initialize_map(points, location) {

    setHeightForMap();
    g_points = points;
    mymap = L.map('mapid').setView(location, 15);
    layout = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibGFuY2Vsb2Z0MTAwOCIsImEiOiJjajE4OXExcWkwMDRyMzJwcDNsdDIzMzU4In0.1JIG2H6f-CZ572Wmzxm77g', {
        maxZoom: 20,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.streets'
    });
    layout.addTo(mymap);

    var searchControl = L.esri.Geocoding.geosearch().addTo(mymap);
    var results = L.layerGroup().addTo(mymap);

    searchControl.on("results", function (data) {

        var RedIcon = L.Icon.Default.extend({
            options: {
            	    imagePath: 'marker-icon-red.png'
            }
         });

        var redIcon = new RedIcon();

        results.clearLayers();
        for (var i = data.results.length - 1; i >= 0; i--) {

            var mk = L.marker(data.results[i].latlng, {icon: redIcon});

            mk.bindPopup('<p class="center-align">Place: ' + data.results[i].properties.PlaceName +'</p>' +
                '<p class="center-align">Address: ' + data.results[i].properties.Place_addr +'</p>').openPopup();

            // console.log(data.results[i]);

            results.addLayer(mk);
        }
    });


    markers = new L.FeatureGroup();
    addMarkers(points);
}

function setHeightForMap() {
    // console.log('triggered');
    var height = $(window).height();
    var offset = $('#top-nav-bar').height();
    $('div#mapid').css({'height': height - offset, 'width': $(window).width()});
}

function addMarkers(points) {
    for (var i = 0; i < points.length; i++) {
        var latitude = points[i].latitude;
        var longitude = points[i].longitude;
        var splvalue = points[i].average_spl;
        var marker = L.marker([latitude, longitude]);
        marker.bindPopup('<div class="center-align"><b>SPL value:</b> ' + splvalue.toString() + '<b> dB</b></div><br><br> ' +
            'Calculated from ' + points[i].ids.length.toString() + ' measurement(s)<br><br>' +
            '<div class="center-div"><button type="button" class="btn btn-default center-div" id="' + i.toString() + '" onClick="get_details(this.id)">Details</button></div>');

        markers.addLayer(marker);
    }

    mymap.addLayer(markers);
}

function get_details(clicked_id) {

    var url = "";
    // if (window.location.url)
    // console.log(window.location.href);
    var cur_url = window.location.href;

    if (cur_url.indexOf("private") > 0) {
        url = '/get_details_prs/'
    } else {
        url = '/get_details_pbs/'
    }

    $.ajax({
        url: url,
        data: {
            'ids[]': g_points[clicked_id].ids
        },
        dataType: 'json',
        success: function (data) {
            if (data) {

                var myModal = document.getElementById('modal');
                var modal_template = Handlebars.compile(document.getElementById('modal-template').innerHTML);

                console.log(data);

                var context = {objects: data};

                myModal.innerHTML = modal_template(context);

                $('.modal').modal();
                $('#modal-detail').modal('open');

                var dateTime = document.getElementsByClassName("dateTime");

                for (var j = 0; j < dateTime.length; j++) {
                    $(dateTime[j]).text(new Date($(dateTime[j]).text()));
                    // console.log(new Date($(dateTime[j]).text()));
                }

                // TODO: set height for graph div

                var div_table = document.getElementsByClassName("div-table");
                // var div_graphs = document.getElementsByClassName("div-graphs");
                var div_ids = document.getElementsByClassName("div-ids");

                for (var k = 0; k < div_table.length; k++) {
                    $(div_ids[k]).css('background', random_color());
                    // console.log(random_color());
                }

                var height = $(div_table[0]).height();
                var width = $(div_table[0]).width();
                $("div.div-graphs").css("height", height);

                renderGraphs(width, height);
            }
        }
    });
}

function random_color() {
    var color = '#';
    var letters = ['c2185b', '7b1fa2', '1976d2', '303f9f', '00796b', '0097a7', '0288d1', '388e3c', 'f57c00', 'ffa000']; //Set your colors here
    color += letters[Math.floor(Math.random() * letters.length)];

    return color;
}

