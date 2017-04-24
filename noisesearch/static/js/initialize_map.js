/**
 * Created by phucphuong on 4/13/17.
 */
var g_points;
var markers;
var mymap;

function initialize_map(points) {
    g_points = points;
    mymap = L.map('mapid').setView([48.72305363, 44.53600696], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibGFuY2Vsb2Z0MTAwOCIsImEiOiJjajE4OXExcWkwMDRyMzJwcDNsdDIzMzU4In0.1JIG2H6f-CZ572Wmzxm77g', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.streets'
    }).addTo(mymap);

    markers = new L.FeatureGroup();
    addMarkers(points);

}


function addMarkers(points) {
    for (var i = 0; i < points.length; i++) {
        var latitude = points[i].latitude;
        var longitude = points[i].longitude;
        var splvalue = points[i].average_spl;
        var marker = L.marker([latitude, longitude]);
        marker.bindPopup('<b>SPL value:</b> ' + splvalue.toString() + '<strong> dB</strong><br><br> ' +
            'Calculated from ' + points[i].ids.length.toString() + ' measurement(s)<br><br>' +
            '<button type="button" class="btn btn-default" id="' + i.toString() + '" onClick="get_details(this.id)">Details</button>');

        markers.addLayer(marker);
    }

    mymap.addLayer(markers);
}

function get_details(clicked_id) {
    $.ajax({
        url: '/get_details/',
        data: {
            'ids[]': g_points[clicked_id].ids
        },
        dataType: 'text',
        success: function (data) {
            if (data) {
                var string_data = '[' + data + ']'

                var jsonData = JSON.parse(string_data);
                console.log(jsonData);

                var myModal = document.getElementById('modal');
                var modal_template = Handlebars.compile(document.getElementById('modal-template').innerHTML);

                var context = {objects: jsonData};
                myModal.innerHTML = modal_template(context);

                $('.modal').modal();
                $('#modal-detail').modal('open');

                var dateTime = document.getElementsByClassName("dateTime");

                for (var j = 0; j < dateTime.length; j++) {
                    $(dateTime[j]).text(new Date($(dateTime[j]).text()));

                    console.log(new Date($(dateTime[j]).text()));
                }

                // TODO: set height for graph div

                var div_table = document.getElementsByClassName("div-table");
                var div_graphs = document.getElementsByClassName("div-graphs");
                var div_ids = document.getElementsByClassName("div-ids");
                for (var k = 0; k < div_table.length; k++) {
                    $(div_graphs[k]).css("height", $(div_table[k]).height());
                    $(div_ids[k]).css("height", $(div_table[k]).height());
                }

                renderGraphs();
            }
        }
    });
}

