$( document ).ready(function() {

    initialize();

    $('#addEmailButton').click(function(){
        if (validateEmail( $('#emailAdd').val())) {
            $('#emailAddError').text('');
            window.emailList.push($('#emailAdd').val());
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
            for(let i=0;i<window.emailList.length;i++){
                if(i!==id){
                    temp_arr.push(window.emailList[i])
                }
            }
            window.emailList=temp_arr;
            render();
    });

});

function initialize(){
    window.emailList = [];
}

///////////////////////////////////////////////////////
//  Render                                           //
//////////////////////////////////////////////////////
function render(){
    createEmailList();
}

function createEmailList(){

    let tableRows="";
    for(let i=0;i<window.emailList.length;i++){
        tableRows+= '<tr><th>'+window.emailList[i]+'</th><th>'+
            '<button id="emailRemoveButton_'+i+'">'+
            '<i id="removeButtonIcon_'+i+ '" class="fas fa-user-minus"></i></button>' +
            '</th></tr>';
    }
    $('#emailList').html('<table class="table">'+tableRows+'</table>');
};

///////////////////////////////////////////////////////
// Validation                                        //
//////////////////////////////////////////////////////

function validateEmail($email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  return emailReg.test( $email );
}
