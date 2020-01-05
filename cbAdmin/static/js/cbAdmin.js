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

});
///////////////////////////////////////////////////////
//  Defaults                                         //
//////////////////////////////////////////////////////

saveUrl = "save/";

function initialize(){
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
///////////////////////////////////////////////////////
//  Save                                            //
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