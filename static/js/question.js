// console.log('hello brother');
// $(document).ready(function () {
//     for(var i=0;i<1000;i++) console.log("heheheheh")
    
// });

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
                if(obj.status == '0'){
                    alert('Correct Answer');
                }
                else{
                    alert('Wrong Answer');
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