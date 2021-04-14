$(document).ready(function () {
    $("#username").on('input', function () {
        // console.log("haohaohasa")
        var name_send = $("#username").val();
        
        var n =$("#username").length;
        
        if(n>5){
            $.ajax({
                url: '/api_check_username',
                type: 'POST',  
                data: { 'data': name_send },
                success: function (data) {
                    var obj = JSON.parse(data);
                    if (obj.status == "1") {
                        $("#name_ok").text("availaible");
                        $("#name_ok").show();
                        $("#name_ok").css("color",'white');
                    }
                    else {
                        $("#name_ok").text("Unavailaible");
                        $("#name_ok").show();
                        $("#name_ok").css("color",'white');
                    }
                },
                error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
                    $('p').append('Error' + errorMessage);
                }
            });
        }
        else {
                $("#name_ok").text("too short");
                $("#name_ok").show();
                $("#name_ok").css("color",'white');
        }
        console.log(n);
        
    });
});