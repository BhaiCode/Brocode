// console.log('hello brother');
// $(document).ready(function () {
//     for(var i=0;i<1000;i++) console.log("heheheheh")
    
// });
function getRemote(id) {
    // console.log(id,"kjaadbkcdbikasdbdui")
    $.ajax({
        type: 'POST',
        url: '/get_updates',
        async: false,
        data: {'data':id},
        success: function (data) {
            /* if result is a JSon object */
            // console.log(data," noonjnjnojn")
            var odj = JSON.parse(data)
            return obj.status;
        }
    });
}
$("#submit").click(function () {
    $('#submit_ques').submit(function () {
        var form = $('#submit_ques')[0];
        var data = new FormData(form);
        $.ajax({
            url: '/submit',
            type: 'POST',
            enctype: 'multipart/form-data',
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            success: function (data) {
                var obj = JSON.parse(data)
                // if(obj.status == '0'){
                //     // alert('Correct Answer');
                //     $('#state').text("queue");
                //     $('#state').show()
                // }
                if(obj.status == '2'){
                    // alert('Correct Answer');
                    $('#state').text("your not logged in");
                    $('#state').show()
                }
                else if(obj.status == '1'){
                    $('#state').text("server error");
                    $('#state').show()
                }
                else{
                    // var sub_id = obj.status;
                    // var text;
                    $('#state').text("queue");
                    $('#state').show()
                    // console.log(getRemote(sub_id),"ksjbncijbdibdasbjsaduijk");
                    // while(1){
                    //     text = getRemote(sub_id);
                    //     // console.log(text)
                    //     if(text == 'executed'){
                    //         $('#state').text(text);
                    //         $('#state').show();
                    //         break;
                    //     }
                    //     else{
                    //         $('#state').text(text);
                    //         $('#state').show();
                    //     }
                    // }
                }
            },
            error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
                $('p').append('Error' + errorMessage);
            }
        })
    });
});
$("#submit_ques").click(function () {
    $('#file').on('change', function () {
        var fileInput = $('#file').val();
        // var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        var allowedExtensions = /(\.py)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#file_ok').text("Wrong Extension");
            $('#file_ok').show();
            $('#file').val("");
        }
        else {
            $('#file_ok').hide();
        }
    });
});