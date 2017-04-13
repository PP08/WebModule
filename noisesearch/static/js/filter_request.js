/**
 * Created by phucphuong on 4/12/17.
 */

$(document).ready(function () {

    $("#chx_duration").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            console.log('checked');
            $("#duration_values :input").attr("disabled", false);
        } else {
            console.log('unchecked');
            $("#duration_values :input").attr("disabled", true);
        }
    });

    $("#chx_spl_value").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            console.log('checked');
            $("#spl_values :input").attr("disabled", false);
        } else {
            console.log('unchecked');
            $("#spl_values :input").attr("disabled", true);
        }
    });

    $("#chx_date").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            console.log('checked');
            $("#date_values :input").attr("disabled", false);
        } else {
            console.log('unchecked');
            $("#date_values :input").attr("disabled", true);
        }
    });

    $("#chx_time").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            console.log('checked');
            $("#time_values :input").attr("disabled", false);
        } else {
            console.log('unchecked');
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

            console.log(filterArray);
            filtersJson = JSON.stringify(filterArray);
            console.log('filter array: ', filterArray.length);
            get_data(filtersJson);
        }
    });

    function get_data(array) {
        console.log(array);
        $.ajax({

            url: /data_filter/,
            type: 'POST',
            data: {'filters': array},

            success: function (data) {
                console.log("success");
                console.log('filtered: ', data);
                markers.clearLayers();
                if (data)
                g_points = data;
                addMarkers(data)
            }
        });
    }

    $("form#test-form").on('submit', function (event) {

        event.preventDefault();
        console.log("submitted");
        console.log($(this).serializeArray());

        var formArray = $(this).serializeArray();

        for (var i = 0; i < formArray.length; i++) {
            // console.log(formArray[i].value);
            if (formArray[i].value == "") {
                Materialize.toast(formArray[i].name + ' is empty', 4000)
            }
        }

    });

});