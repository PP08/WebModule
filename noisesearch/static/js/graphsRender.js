/**
 * Created by phucphuong on 4/24/17.
 */

function renderGraphs(width, height) {
    $('#modal-detail a').click(function (event) {
        // console.log("ok. it's clicked!");
        event.preventDefault();
        var url = $(this).attr('href');
        var div_id = $(this).attr('id');
        // alert('url: ' + url);

        var str_id = div_id.split('-')[1];

        var div_graph = document.getElementById("graphs" + str_id);

        div_graph.innerHTML =
            '<div class="center-icon">' +
            '<div class="preloader-wrapper active"> ' +
            '<div class="spinner-layer spinner-blue"> ' +
            '<div class="circle-clipper left"> ' +
            '<div class="circle"></div> ' +
            '</div> ' +
            '<div class="gap-patch"> ' +
            '<div class="circle"></div> ' +
            '</div> ' +
            '<div class="circle-clipper right"> ' +
            '<div class="circle"></div> ' +
            '</div> ' +
            '</div> ' +
            '<div class="spinner-layer spinner-red"> ' +
            '<div class="circle-clipper left"> ' +
            '<div class="circle"></div> ' +
            '</div> ' +
            '<div class="gap-patch"> ' +
            '<div class="circle"></div> ' +
            '</div> ' +
            '<div class="circle-clipper right"> ' +
            '<div class="circle"></div> ' +
            '</div> ' +
            '</div> ' +
            '<div class="spinner-layer spinner-yellow"> ' +
            '<div class="circle-clipper left"> ' +
            '<div class="circle"></div> ' +
            '</div>' +
            '<div class="gap-patch"> ' +
            '<div class="circle"></div> ' +
            '</div>' +
            '<div class="circle-clipper right"> ' +
            '<div class="circle"></div> ' +
            '</div>' +
            '</div>' +
            '<div class="spinner-layer spinner-green"> ' +
            '<div class="circle-clipper left"> ' +
            '<div class="circle"></div> ' +
            '</div>' +
            '<div class="gap-patch"> ' +
            '<div class="circle"></div> ' +
            '</div>' +
            '<div class="circle-clipper right"> ' +
            '<div class="circle"></div> ' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>';

        $.ajax({
            url: url,
            type: 'GET',
            data: {'id': str_id},

            success: function (data) {
                console.log(data);
                $(div_graph).empty();

                div_graph.innerHTML = '<div class="center-icon z-depth-2" id="result-graph' + str_id + '"> </div>';

                var result_graph = document.getElementById("result-graph" + str_id);

                var trace = {
                    type: 'scatter',                    // set the chart type
                    mode: 'lines',                      // connect points with lines
                    x: data['timestamps'],
                    y: data['spl_values'],
                    line: {                             // set the width of the line.
                        width: 1
                    },
                };

                var layout = {
                    autosize: false,
                    width: width,
                    height: height,
                    yaxis: {title: "Noise Search"},       // set the y axis title
                    xaxis: {
                        showgrid: false,                  // remove the x-axis grid lines
                        tickformat: "%H:%m:%S"              // customize the date format to "month, day"
                    },
                    margin: {                           // update the left, bottom, right, top margin
                        l: 40, b: 30, r: 10, t: 20
                    }
                };

                Plotly.plot(result_graph, [trace], layout, {showLink: false});
            }
        })
    });
}