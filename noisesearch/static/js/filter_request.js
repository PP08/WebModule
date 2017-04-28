/**
 * Created by phucphuong on 4/12/17.
 */

var global_model_name = '';
var global_ids = [];

$(document).ready(function () {

    $("#chx_duration").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#duration_values :input").attr("disabled", false);
        } else {
            $("#duration_values :input").attr("disabled", true);
        }
    });

    $("#chx_spl_value").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#spl_values :input").attr("disabled", false);
        } else {
            $("#spl_values :input").attr("disabled", true);
        }
    });

    $("#chx_date").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#date_values :input").attr("disabled", false);
        } else {
            $("#date_values :input").attr("disabled", true);
        }
    });

    $("#chx_time").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $("#time_values :input").attr("disabled", false);
        } else {
            $("#time_values :input").attr("disabled", true);
        }
    });

    $("form :input").change(function () {
        $("#btn-apply").removeClass("disabled");
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

    $("form#filter-form").submit(function () {
        event.preventDefault();
        var filterArray = $(this).serializeArray();
        // raise_toast(filterArray);

        if (validate(filterArray)) {
            $("#btn-apply").addClass("disabled");
            $('.modal').modal();
            $('#modal-filter').modal('close');

            filtersJson = JSON.stringify(filterArray);

            // todo: handle form changes or not. + handle when receive null

            get_data(filtersJson);

        }
    });

    function get_data(array) {

        if (global_ids.length > 0){
            var visualized = true;
        }else {
            visualized = false;
        }

        // alert('model name: ' + global_model_name);

        $.ajax({
            url: /data_filter/,
            type: 'POST',
            data: {'filters': array, 'visualized': visualized, 'ids[]': global_ids, 'modelName': global_model_name},
            typeData: 'json',

            success: function (data) {
                markers.clearLayers();

                if (data.length > 0) {
                    g_points = data;
                    addMarkers(data);
                    Materialize.toast("Found " + data.length + " results" , 4000)
                } else {
                    Materialize.toast(data.message, 4000)
                }
            }
        });
    }
});