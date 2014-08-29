function email(){ //function for sending info to the php file
var name = "Bug Report"; //subject
var email = "zorpixfang@gmail.com" //email to send to
var vardata = $("textarea").val(); //data from textbox

$.ajax({ //request to send data to PHP
    type: "POST",
    url: "email.php",
    data: {name:name, email:email, vardata:vardata}, 
    success: function() {
        alert("Your bug report was sent!");
    }
});
}


