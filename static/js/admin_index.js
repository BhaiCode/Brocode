// $(document).ready(function(){
    
// });
function delete2(item){
    var data = item
    $.ajax({
        url: '/delete_question',
        type:'POST',
        data : data,
        success: function (data) {
            var obj = JSON.parse(data)
            if(obj.status=='1'){
                alert("Question deleted successfully")
                window.location = 'http://localhost:5000/admin';
            }
            else{
                alert('Failed Question is not Deleted');
                window.location = 'http://localhost:5000/admin';
            }
        },
        error: function (jqXhr, textStatus, errorMessage) { // if any error come then 
            $('p').append('Error' + errorMessage);
        }
    })
}