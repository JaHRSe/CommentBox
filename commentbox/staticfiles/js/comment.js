$( document ).ready(function() {
    $('#submitCommentButton').on('click',function (){
        // Hide success msg if present
        $('#submitSuccessMsg').hide();
        processForm();
    });

    FilePond.registerPlugin(FilePondPluginFileValidateSize);

    // File Upload
    fileUploadSetup();

});

function fileUploadSetup(){

    $('#fileUploadInput').filepond({
        allowMultiple:true,
        // maxFileSize: '3MB',
    });

    $(function(){

    $.fn.filepond.setDefaults({
        // maxFileSize: '10MB',
        // maxFiles: 4,
        maxTotalFileSize: '20MB',
        server: {
            url: '/comment/',
            process: 'upload/',
            revert: null,
            restore: null,
            fetch: null
        }
    });

    // Actions to take on upload
    $('#fileUploadInput').on('FilePond:addfile', function(e) {
        console.log('file added event', e);
    });

});
}

function processForm(){

        // Build list of file IDs for all uploaded files
    let hidInps =  $("[name='filepond'][type=hidden]");

     // If no comment, and no files return
    if(hidInps.length==0 && !$('#comment').val() ){return}

    let data = {};

    data['comment'] = $('#comment').val();

    let files = [];
    for(let i=0; i<hidInps.length; i++){
        files.push(hidInps[i].value)
    }

    data['files'] = files;

    let url = '';

    let callBack = function(){postFormSubmit()};

    sendPost(data,url,callBack);
}

function postFormSubmit(){

    $('#submitSuccessMsg').show();

    $('#comment').val('');

    $('#submitCommentButton').prop('disabled', true);
    $('#submitCommentButton').css('color','lightgrey');
    // setTimeout(function(){
    //   location.reload();
    // }, 2000);

    // $('#comment').attr('placeholder','Write a comment here. Unless you tell us your name, your comment will be 100% anonymous')
}

///////////////////////////////////////////////////////
//  AJax                                            //
//////////////////////////////////////////////////////
function sendPost(data, url, callback){
    data = JSON.stringify(data);
    $.ajax({
        url:url,
        type:'POST',
        contentType: "application/json; charset=utf-8",
        data:data,
        success: function(result){
            callback(result);
        },
        errror:function(request,error){
           //
        }
    })
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});