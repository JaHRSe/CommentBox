$( document ).ready(function() {

    initialize();

    $('#addEmailButton').click(function(){
        if (validateEmail( $('#emailAdd').val())) {
            $('#emailAddError').text('');
            window.notifyList.push($('#emailAdd').val());
            $('#emailAdd').val('');
            render();
        }   else {
            $('#emailAddError').text(' Please enter a valid email address');
        }
    });

    $(document).on("click", '[id^="emailRemoveButton"]',function(){
            let id_arr = this.id.split('_');
            let id = parseInt(id_arr[id_arr.length-1])

            let temp_arr =[];
            for(let i=0;i<window.notifyList.length;i++){
                if(i!==id){
                    temp_arr.push(window.notifyList[i])
                }
            }
            window.notifyList=temp_arr;
            render();
    });

    $('#saveButton').click(function () {
        save();
    });

    ////////////////////////////////////
    // Comment Response Controls
    ////////////////////////////////////

    $('#saveresponsebutton').click(function(){
        saveCommentResponse();
    });

});
///////////////////////////////////////////////////////
//  Globals                                        //
//////////////////////////////////////////////////////

let responseEditor = null; // Hold editor instance

///////////////////////////////////////////////////////
//  Defaults                                         //
//////////////////////////////////////////////////////

saveUrl = "";

function initialize(){
    // Ckeditor setup
    ClassicEditor
        .create( document.querySelector( '#responsetext' ),{
            removePlugins:["EasyImage","ImageCaption","ImageUpload"]
        })
        .then( editor => {
           responseEditor = editor;
        } )
        .catch( error => {
            console.error( error );
        } );
    render(); // Needed to populate notify list

}

///////////////////////////////////////////////////////
//  Render                                           //
//////////////////////////////////////////////////////
function render(){
    createNotifyList();
}

function createNotifyList(){

    let tableRows="";
    for(let i=0;i<window.notifyList.length;i++){
        tableRows+= '<tr><th>'+window.notifyList[i]+'</th><th>'+
            '<button id="emailRemoveButton_'+i+'">'+
            '<i id="removeButtonIcon_'+i+ '" class="fas fa-user-minus"></i></button>' +
            '</th></tr>';
    }
    $('#notifyListDiv').html('<table class="table">'+tableRows+'</table>');
};

///////////////////////////////////////////////////////
// Validation                                        //
//////////////////////////////////////////////////////

function validateEmail($email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  if(!$email){
      return false;
  } else {
      return emailReg.test($email);
  }
}

function apply_form_field_error(fieldname, error) {

    let div_container = null;
    let input = null;
    if(fieldname=='body'){
        input = $("#responsetext");
        div_container = input;
    } else{
        let input = $("#" + fieldname);
        div_container = input.parent();
    }


    let error_msg = $("<span />").addClass("help-inline alert-danger ckFormError").text(error.message);
    div_container.addClass("alert-danger");
    div_container.after(error_msg);



}

function clearErrors(){

    if($('.ckFormError'))
    {
        $('.ckFormError').remove();
    }
}
///////////////////////////////////////////////////////
//  Save   Email Settings                           //
//////////////////////////////////////////////////////

function save(){
    let data = {
        "commentBoxEmail":$('#commentBoxInput').val(),
        "notificationList":window.notifyList,
    };
    sendPost(data,window.saveUrl,saveResults)
}

function saveResults(result){
     $('#saveResult').html('');
    if(result['result']){
        $('#saveResult').html(saveSuccessHtml);
    }else{
        $('#saveResult').html(saveErrorHtml);
    }
}

let saveSuccessHtml = `
    <h2>Success!</h2>
`;

let saveErrorHtml= `
    <h2>Fail!</h2>
`;

///////////////////////////////////////////////////////
//  Comment Response                                //
//////////////////////////////////////////////////////
function saveCommentResponse(){
    // Get the title text
    let title = $('#title').val();

    if(!title){
       $('<span style="color:red;">Unique response title required</span>').insertAfter($('#title'));
       $('#title').css("border-color", "red");
    } else{
        // Get text body
       let responsebody = responseEditor.getData();
       // Reset success message
        if($('#responsesuccess')){
            $('#responsesuccess').remove();
        }
        let data={'title':title, 'body':responsebody}
        let url = 'commentresponse/'; //post to current url
        sendPost(data,url,responseSavedCallBack, responseCallBackError);
    }
}

function responseSavedCallBack(result){
    $('<span class="success" style="color:green"> Response posted</span>').insertAfter($('#saveresponsebutton'));
    $('#title').val('');
    responseEditor.setData('');
}

function responseCallBackError(errors){
    $.each(errors, function(index, value) {
        apply_form_field_error(index, value[0]); //value[0]=message
    }) // close foreach
}

function clearMessages(){

    if($('.success')){
        $('.success').remove();
    }

    // clear errors
    clearErrors();

}

///////////////////////////////////////////////////////
//  AJax                                            //
//////////////////////////////////////////////////////
function sendPost(data, url, callback, errorcallback=null){
    data = JSON.stringify(data);
    clearMessages()
    $.ajax({
        url:url,
        type:'POST',
        contentType: "application/json; charset=utf-8",
        data:data,
        error: function(request, error){
            if(errorcallback){
                let errors = JSON.parse(request.responseJSON);
                errorcallback(errors);
            } else{
                alert('Server Error');
            }
        },
        success: function(result){
            callback(result);
        },
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