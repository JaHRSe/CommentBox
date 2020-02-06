$( document ).ready(function() {

    $(document).on('click', '[id^=responseTruncToggle]',function(){
       $(this).prev().toggleClass('truncate');
       $(this).text(
           function(i,text){ return text=="Read More"?"less":"Read More"});
    });
});

function toggleText(e) {
  $('#responsetext').classList.toggle('truncate');
}