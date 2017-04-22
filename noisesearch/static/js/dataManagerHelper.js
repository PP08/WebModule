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
            $('#pbs_tab:checkbox').each(function () {
                this.checked = true;
            });

        } else {
            $('#pbs_tab:checkbox').each(function () {
                this.checked = false;
            });
        }
    });


    $('#btn-visualize-prs').click(function () {
        // console.log("btn prs clicked");
        var selected_items = [];
        $('#prs_tab :checkbox:checked').each(function () {
            // console.log($(this).val());
            selected_items.push($(this).val());
        });


        if (selected_items.length > 0) {
            console.log(selected_items);
        }

    });

    $('#btn-delete-prs').click(function () {
        // console.log("btn prs clicked");
        var selected_items = [];
        var selected_items_tr = [];
        $('#prs_tab :checkbox:checked').each(function () {
            selected_items.push($(this).val());
        });

        if (selected_items.length > 0) {

            for(var i = 0; i < selected_items.length; i++){
                selected_items_tr.push("row_prs" + selected_items[i]);
            }

            $.ajax({
                url: '/data_manager/delete_private_data/',
                type: 'POST',
                data: {'modelName': 'privateSingle', 'ids[]': selected_items},

                success: function (data) {
                    for (var i = 0; i < selected_items_tr.length; i++){
                        $('#' + selected_items_tr[i]).remove();
                    }
                }
            });

        }

    });

});