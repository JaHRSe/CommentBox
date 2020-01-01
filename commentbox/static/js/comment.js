$( document ).ready(function() {
    $('#submitCommentButton').on('click',function (){
        processForm();
    });

    // File Upload
    fileUploadSetup();

});

function fileUploadSetup(){

    $('#fileUploadInput').filepond({
        allowMultiple:true,
        maxFileSize: '3MB',
    });

    $(function(){

    $.fn.filepond.setDefaults({
        maxFileSize: '3MB',
        server: {
            url: 'http://localhost:8000/',
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
            alert('Could not save data')
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