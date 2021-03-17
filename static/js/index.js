$(document).on( "click","#logout", function() {

    $.ajax({
        url:'/logout',
        type: 'POST',  // http method
        success: function (data) { // after success your get data
            var obj = JSON.parse(data);
            if(obj.status == "logout"){
                window.location.replace("http://localhost:5000/login");
            }
            else{
                console.log("Failed");
            }
        },
        error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
                $('p').append('Error' + errorMessage);
        }
    });
});

//   document.onreadystatechange = function() { 
//     if (document.readyState !== "complete") { 
//         document.querySelector("body").style.visibility = "hidden"; 
//         document.querySelector("#loader").style.visibility = "visible"; 
//     } else { 
//         document.querySelector("#loader").style.display = "none"; 
//         document.querySelector("body").style.visibility = "visible"; 
//     } 
// }; 






  return pub;
})(document, window);




