$(document).ready(function () {
    $("#submit").click(function () {
        $('#form').submit(function () {
            var form = $('#form')[0];
            // console.log(document.getElementById("name"))
            var data = new FormData(form);
            // console.log(data['name'])
            // console.log(document.getElementById("testcases"))
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
    $('#solution').on('change', function () {
        var fileInput = $('#solution').val();
        // var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        var allowedExtensions = /(\.py)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#sol_ok').text("Wrong Extension");
            $('#sol_ok').show();
            $('#solution').val("");
        }
        else {
            $('#sol_ok').hide();
        }
    });
    
    $('#testcases').on('change', function () {
        var fileInput = $('#testcases').val(); 
        var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#test_ok').text("Wrong Extension");
            $('#test_ok').show();
            $('#testcases').val("");
        }
        else {
            $('#test_ok').hide();
        }
    });
    
    $('#opcases').on('change', function () {
        var fileInput = $('#opcases').val(); 
        var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
        if (!allowedExtensions.exec(fileInput)) {
            $('#op_ok').text("Wrong Extension");
            $('#op_ok').show();
            $('#opcases').val("");
        }
        else {
            $('#op_ok').hide();
        }
    });
    // $('#file4').on('change', function () {
    //     var fileInput = $('#file4').val(); 
    //     var allowedExtensions = /(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;
    //     if (!allowedExtensions.exec(fileInput)) {
    //         $('#file4_ok').text("Wrong Extension");
    //         $('#file4_ok').show();
    //         $('#file4').val("");
    //     }
    //     else {
    //         $('#file4_ok').hide();
    //     }
    // });
    
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
    // $("#add").on('click',function(){
    //     console.log("HHHHHHH")
    //     const mylist = document.getElementsByClassName('content')[0];
    //     let newdiv = document.createElement("div")
    //     let newlist = document.createElement("textarea");
    //     var b = document.createElement("button");
    //     b.type = "button"
    //     b.innerHTML="Delete"
    //     b.setAttribute('class' , "btn btn-danger")
    //     b.addEventListener('click',function(){

    //     })
    //     // b.width = 100%
    //     newlist.placeholder="write here";
    //     newdiv.appendChild(newlist);
    //     newdiv.appendChild(b);
    //     mylist.appendChild(newdiv);
        
    // })
    // console.log("jhjnjo")
    // $("#submit2").on('click',function(){
    //     var x = document.getElementsByClassName('cke_editable cke_editable_themed cke_contents_ltr cke_show_borders');
    //     console.log("bbjhbjj",x)
    // })
    // let output = document.getElementById('output');
    // let buttons = document.getElementsByClassName('tool--btn');
    // for (let btn of buttons) {
    //     btn.addEventListener('click', () => {
    //         let cmd = btn.dataset['command'];
    //         if(cmd == 'createlink') {
    //             const output = document.getElementById('output');
    //             let url = prompt("Enter the link here: ", "http:\/\/");
    //             console.log(url)
    //             if(url != "http:\/\/"){
    //                 // let newlink = document.createElement('a')
    //                 // newlink.setAttribute('href',url)
    //                 // output.appendChild(newlink)
    //                 document.execCommand(cmd,false,url)
    //             }
    //         }
    //         else if(cmd == "insertImage"){
    //             let url = prompt("Enter the image link here: ", "");
    //             if(url!=""){
    //                 const mylist = document.getElementById('output');
    //                 let newimg = document.createElement("img")
    //                 newimg.setAttribute('src',url)
    //                 newimg.setAttribute("style","height:400px")
    //                 let brk = document.createElement('br');
    //                 mylist.appendChild(brk)
    //                 mylist.appendChild(newimg)
    //             } 
    //         }
    //         else{
    //             var x = document.getElementById('output')
    //             // alert(selectedText);
    //             var tag;
    //             if(cmd == 'bold') tag='b';
    //             var selectedText = window.getSelection();
    //             console.log(selectedText.text)
    //             if (selectedText != "") {
    //                 var newText = "<" + tag + ">" + selectedText + "</" + tag + ">";
    //                 window.getSelection = newText;
    //             }
    //         }
    //     })
    // }
    // function formatText(tag) {
    //     console.log("oaooadon")
    //     var selectedText = document.selection.createRange().text;

    //     if (selectedText != "") {
    //         var newText = "<" + tag + ">" + selectedText + "</" + tag + ">";
    //         document.selection.createRange().text = newText;
    //     }
    // }
});

