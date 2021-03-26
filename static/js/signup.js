$(document).ready(function () {
    $("#username").on('input', function () {
        // console.log("haohaohasa")
        var name_send = $("#username").val();
        // console.log(name_send);
        $.ajax({
            url: '/api_check_username',
            type: 'POST',  
            data: { 'data': name_send },
            success: function (data) {
                var obj = JSON.parse(data);
                if (obj.status == "1") {
                    $("#name_ok").text("Correct name");
                    $("#name_ok").show();
                    $("#name_ok").css("color",'white');
                }
                else {
                    $("#name_ok").text("Name Already Exist");
                    $("#name_ok").show();
                    $("#name_ok").css("color",'white');
                }
            },
            error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
                $('p').append('Error' + errorMessage);
            }
        });
    });
});