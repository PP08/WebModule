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


    $("#btn-apply").click(function () {
        $('.modal').modal();
        $('#modal-filter').modal('close');
        $(this).addClass("disabled");
        // console.log($('#details-form').serialize());

    });

    // $("form#details-form").submit(function () {
    //
    //     $("#btn-apply").addClass("disabled");
    //
    //     // TODO: get the data of the form
    // });

});