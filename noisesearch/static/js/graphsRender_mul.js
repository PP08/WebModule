/**
 * Created by phucphuong on 4/24/17.
 */

function renderGraphsMul(width, height, id) {

    var div_graph = document.getElementById("graphs-mul");

    div_graph.innerHTML = '<div class="center-icon z-depth-2" id="result-graph"> </div>';

    var result_graph = document.getElementById("result-graph");


    // TODO: render bar chart

    var measurement_values = g_points[id];

    var counter = [0, 0, 0, 0, 0, 0];

    for (var i = 0; i < measurement_values.length; i++) {

        var spl = measurement_values[i]['fields'].spl_value;

        if (spl < 40) {
            counter[0]++;
        }
        else if (40 <= spl && spl < 60) {
            counter[1]++;
        }
        else if (60 <= spl && spl < 80) {
            counter[2]++;
        }
        else if (80 <= spl && spl < 100) {
            counter[3]++;
        }
        else if (100 <= spl && spl < 120) {
            counter[4]++;
        }
        else if (120 <= spl && spl < 140) {
            counter[5]++;
        }
    }

    var data = [
        {
            x: ['< 40', '40 - 60', '60 - 80', '80 - 100', '100 - 120', '120 - 140'],
            y: counter,
            marker: {
                color: ['rgba(1,1,1,0.0)', 'rgba(50,171, 96, 0.7)', 'rgba(50,171, 96, 0.7)', 'rgba(219, 64, 82, 0.7)', 'rgba(55,128,191,0.7)', 'rgba(55,128,191,0.7)']
            },
            type: 'bar'
        }
    ];

    var layout = {
        autosize: false,
        width: width,
        height: height,
        yaxis: {title: "Noise Search"},
        margin: {
            l: 40, b: 30, r: 10, t: 20
        }
    };

    Plotly.newPlot(result_graph, data, layout, {showLink: false});

    // //console.log('global variable' + g_points);

    // var trace = {
    //     type: 'scatter',                    // set the chart type
    //     mode: 'lines',                      // connect points with lines
    //     x: data['timestamps'],
    //     y: data['spl_values'],
    //     line: {                             // set the width of the line.
    //         width: 1
    //     }
    // };
    //
    // var layout = {
    //     autosize: false,
    //     width: width,
    //     height: height,
    //     yaxis: {title: "Noise Search"},       // set the y axis title
    //     xaxis: {
    //         showgrid: false,                  // remove the x-axis grid lines
    //         tickformat: "%H:%m:%S"              // customize the date format to "month, day"
    //     },
    //     margin: {                           // update the left, bottom, right, top margin
    //         l: 40, b: 30, r: 10, t: 20
    //     }
    // };
    //
    // Plotly.plot(result_graph, [trace], layout, {showLink: false});

}