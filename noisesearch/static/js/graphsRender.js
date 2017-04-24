/**
 * Created by phucphuong on 4/24/17.
 */

function renderGraphs() {
    $('#modal-detail a').click(function (event) {
        // console.log("ok. it's clicked!");
        event.preventDefault();
        var url = $(this).attr('href');
        var div_id = $(this).attr('id');
        // alert('url: ' + url);

        var str_id = div_id.split('-')[1];

        document.getElementById("graphs" + str_id).innerHTML =
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
            }
        })

    });
}