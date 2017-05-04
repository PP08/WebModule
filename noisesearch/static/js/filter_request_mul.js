/**
 * Created by phucphuong on 4/12/17.
 */

var global_model_name = '';
var global_ids = [];

$(document).ready(function () {

    $("#chx_distance_mul").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#distance_values_mul :input").attr("disabled", false);
        } else {
            $("#distance_values_mul :input").attr("disabled", true);
        }
    });

    $("#chx_spl_value_mul").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#spl_values_mul :input").attr("disabled", false);
        } else {
            $("#spl_values_mul :input").attr("disabled", true);
        }
    });

    $("#chx_date_mul").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#date_values_mul :input").attr("disabled", false);
        } else {
            $("#date_values_mul :input").attr("disabled", true);
        }
    });

    // $("#chx_time").change(function () {
    //     var $checkbox = $(this);
    //     if ($checkbox.prop('checked')) {
    //         $("#time_values_mul :input").attr("disabled", false);
    //     } else {
    //         $("#time_values_mul :input").attr("disabled", true);
    //     }
    // });

    $("form :input").change(function () {
        $("#btn-apply-mul").removeClass("disabled");
    });

    function validate(array) {
        for (var i = 0; i < array.length; i++) {
            if (array[i].value == "") {
                Materialize.toast('Empty input', 3000)
                return false;
            }
        }
        return true;
    }

    $("form#filter-form-mul").submit(function () {
        event.preventDefault();
        var filterArray = $(this).serializeArray();
        // raise_toast(filterArray);

        if (validate(filterArray)) {
            $("#btn-apply-mul").addClass("disabled");
            $('.modal').modal();
            $('#modal-filter-mul').modal('close');

            filtersJson = JSON.stringify(filterArray);

            // todo: handle form changes or not. + handle when receive null

            get_data(filtersJson);

        }
    });

    function get_data(array) {

        if (global_ids.length > 0) {
            var visualized = true;
        } else {
            visualized = false;
        }

        //console.log(global_ids);
        // alert('model name: ' + global_model_name);

        $.ajax({
            url: /data_filter_mul/,
            type: 'POST',
            data: {'filters': array, 'visualized': visualized, 'ids[]': global_ids, 'modelName': global_model_name},
            typeData: 'json',

            success: function (data) {
                circles.clearLayers();
                trackers.clearLayers();
                markers.clearLayers();


                if (data['message']) {

                    Materialize.toast(data.message, 4000)

                } else {
                    g_average_values = data['average_objects'];
                    g_points = data['detail_objects'];
                    console.log(g_points);

                    addTrackers(g_points, g_average_values);
                    Materialize.toast("Found " + g_average_values.length + " results" , 4000)

                }
            }
        });
    }
});