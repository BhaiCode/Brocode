$(document).ready(function () {
    $("#submit").click(function () {
        $('#form1').submit(function () {
            var form = $('#form1')[0];
            var data = new FormData(form);
            console.log(typeof(data),"hahahhhahahhah");
            $.ajax({
                url: '/api_question',
                type: 'POST',
                enctype: 'multipart/form-data',
                data: data,
                processData: false,
                contentType: false,
                cache: false,
                success: function (data) {
                    var obj = JSON.parse(data)
                    if(obj.status == '0'){
                        alert('Successfully uploaded');
                        window.location = 'http://localhost:5000/admin';
                    }
                    else{
                        alert('Failed Question is not uploaded');
                        window.location = 'http://localhost:5000/admin';
                    }
                },
                error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
                    $('p').append('Error' + errorMessage);
                }
            })

        });
    });
    $('#file1').on('change', function () {
        var fileInput = $('#file1').val();
        // var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        var allowedExtensions = /(\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#file1_ok').text("Wrong Extension");
            $('#file1_ok').show();
            $('#file1').val("");
        }
        else {
            $('#file1_ok').hide();
        }
    });
    
    $('#file2').on('change', function () {
        var fileInput = $('#file2').val(); 
        var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#file2_ok').text("Wrong Extension");
            $('#file2_ok').show();
            $('#file2').val("");
        }
        else {
            $('#file2_ok').hide();
        }
    });
    
    $('#file3').on('change', function () {
        var fileInput = $('#file3').val(); 
        var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#file3_ok').text("Wrong Extension");
            $('#file3_ok').show();
            $('#file3').val("");
        }
        else {
            $('#file3_ok').hide();
        }
    });
    
    
    $("#name").on('input', function () {
        var name_send = $("#name").val();
        $.ajax({
            url: '/api_check_name',
            type: 'POST',  
            data: { 'data': name_send },
            success: function (data) {
                var obj = JSON.parse(data);
                if (obj.status == "1") {
                    $("#name_ok").text("Correct name");
                    $("#name_ok").show();
                }
                else {
                    $("#name_ok").text("Name Already Exist");
                    $("#name_ok").show();
                }
            },
            error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
                $('p').append('Error' + errorMessage);
            }
        });
    });
});

