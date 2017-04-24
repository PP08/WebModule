/**
 * Created by phucphuong on 4/23/17.
 */

$(document).ready(function () {
    $("#checkAllPrs").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $('#prs_tab :checkbox').each(function () {
                this.checked = true;
            });
        } else {
            $('#prs_tab :checkbox').each(function () {
                this.checked = false;
            });
        }
    });


    $("#checkAllPbs").change(function () {
        var $checkbox = $(this);
        if ($checkbox.prop('checked')) {
            $('#pbs_tab :checkbox').each(function () {
                this.checked = true;
            });
        } else {
            $('#pbs_tab :checkbox').each(function () {
                this.checked = false;
            });
        }
    });


    $('#btn-make-public-prs').click(function () {
        // make_public('privateSingle');
        change_state_of_data_single('prs', 'privateSingle', '/data_manager/pbs/', 'pbs');
        console.log("sanity check");
    });


    $('#btn-make-private-pbs').click(function () {

        change_state_of_data_single('pbs', 'publicSingle', '/data_manager/prs/', 'prs');

    });


    $('#btn-delete-prs').click(function () {
        delete_selected_data("prs", '/data_manager/delete_data/', 'privateSingle');
    });


    $('#btn-delete-pbs').click(function () {
        delete_selected_data("pbs", '/data_manager/delete_data/', 'publicSingle');
    });

    function delete_selected_data(tabName, url, modelName) {
        var selected_items = [];
        var selected_items_tr = [];
        $('#' + tabName + '_tab :checkbox:checked').each(function () {
            selected_items.push($(this).val());
        });

        if (selected_items[0] == 0) {
            selected_items.splice(0, 1);
        }

        if (selected_items.length > 0) {

            for (var i = 0; i < selected_items.length; i++) {
                selected_items_tr.push("row_" + tabName + selected_items[i]);
            }

            $.ajax({
                url: url,
                type: 'POST',
                data: {'modelName': modelName, 'ids[]': selected_items},

                success: function (data) {
                    for (var i = 0; i < selected_items_tr.length; i++) {
                        // $('#' + selected_items_tr[i]).hide('slow').remove();
                        $('#' + selected_items_tr[i]).fadeOut("slow", function () {
                            $(this).remove();
                        });
                    }
                }
            });
        }
    }


    function change_state_of_data_single(tabName, modelName, linkUrl, tableName) {

        var selected_items = [];
        var selected_items_tr = [];
        $('#'+ tabName +'_tab :checkbox:checked').each(function () {
            selected_items.push($(this).val());
        });

        if (selected_items[0] == 0) {
            selected_items.splice(0, 1);
        }
        if (selected_items.length > 0) {
            for (var i = 0; i < selected_items.length; i++) {
                selected_items_tr.push("row_" + tabName + selected_items[i]);
            }

            $.ajax({
                url: '/data_manager/change_state_single/',
                type: 'POST',
                data: {'modelName': modelName, 'ids[]': selected_items},
                dataType: 'text',

                success: function (data) {
                    for (var i = 0; i < selected_items_tr.length; i++) {
                        $('#' + selected_items_tr[i]).fadeOut("slow", function () {
                            $(this).remove();
                        });
                    }

                    var string_data = '[' + data + ']'
                    var jsonData = JSON.parse(string_data);
                    console.log(jsonData);
                    //
                    // console.log(jsonData[0][0]['fields']);
                    // console.log(jsonData[0][0]['pk']);

                    for (var j = 0; j < jsonData.length; j++) {
                        $('#table-'+ tableName+ ' tbody').append('<tr id="row_'+ tableName + jsonData[j][0]['pk'] + '">' +
                            '<td><p><input type="checkbox" id="' + tableName + jsonData[j][0]['pk'] + '" value="' + jsonData[j][0]['pk'] + '"/>' +
                            '<label for="' + tableName + jsonData[j][0]['pk'] + '"></label></p></td>' +
                            '<td><a href="' + linkUrl + jsonData[j][0]['pk'] + '">' + new Date(jsonData[j][0]['fields'].start_time) + '</a></td>' +
                            '<td>' + jsonData[j][0]['fields'].average_spl + '</td>' +
                            '<td>' + jsonData[j][0]['fields'].duration + '</td></tr>');
                    }
                }
            });
        }

    }

    // function make_public(modelName) {
    //     var selected_items = [];
    //     var selected_items_tr = [];
    //     $('#prs_tab :checkbox:checked').each(function () {
    //         selected_items.push($(this).val());
    //     });
    //
    //     if (selected_items[0] == 0) {
    //         selected_items.splice(0, 1);
    //     }
    //     if (selected_items.length > 0) {
    //         for (var i = 0; i < selected_items.length; i++) {
    //             selected_items_tr.push("row_prs" + selected_items[i]);
    //         }
    //
    //         $.ajax({
    //             url: '/data_manager/make_public/',
    //             type: 'POST',
    //             data: {'modelName': modelName, 'ids[]': selected_items},
    //             dataType: 'text',
    //
    //             success: function (data) {
    //                 for (var i = 0; i < selected_items_tr.length; i++) {
    //                     $('#' + selected_items_tr[i]).fadeOut("slow", function () {
    //                         $(this).remove();
    //                     });
    //                 }
    //
    //                 var string_data = '[' + data + ']'
    //                 var jsonData = JSON.parse(string_data);
    //                 console.log(jsonData);
    //
    //                 console.log(jsonData[0][0]['fields']);
    //                 console.log(jsonData[0][0]['pk']);
    //
    //                 for (var j = 0; j < jsonData.length; j++) {
    //                     $('#table-pbs tbody').append('<tr id="row_pbs' + jsonData[j][0]['pk'] + '">' +
    //                         '<td><p><input type="checkbox" id="pbs' + jsonData[j][0]['pk'] + '" value="' + jsonData[j][0]['pk'] + '"/>' +
    //                         '<label for="pbs' + jsonData[j][0]['pk'] + '"></label></p></td>' +
    //                         '<td><a href="/data_manager/pbs/' + jsonData[j][0]['pk'] + '">' + new Date(jsonData[j][0]['fields'].start_time) + '</a></td>' +
    //                         '<td>' + jsonData[j][0]['fields'].average_spl + '</td>' +
    //                         '<td>' + jsonData[j][0]['fields'].duration + '</td></tr>');
    //                 }
    //             }
    //         });
    //     }
    // }

});
