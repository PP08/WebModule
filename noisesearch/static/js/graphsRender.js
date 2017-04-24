/**
 * Created by phucphuong on 4/24/17.
 */

// $(document).ready(function () {
//     $('a').click(function (event) {
//         console.log("ok. it's clicked!");
//         event.preventDefault();
//         var url = $(this).attr('href');
//         alert('url: ' + url);
//     });
// });


function renderGraphs() {
    $('#modal-detail a').click(function (event) {
        console.log("ok. it's clicked!");
        event.preventDefault();
        var url = $(this).attr('href');
        // alert('url: ' + url);

        // TODO: add preload for graph :)
        /*
         <div class="spinner-layer spinner-green">
         <div class="circle-clipper left">
         <div class="circle"></div>
         </div><div class="gap-patch">
         <div class="circle"></div>
         </div><div class="circle-clipper right">
         <div class="circle"></div>
         </div>
         </div>
         </div>
         */

    });
}