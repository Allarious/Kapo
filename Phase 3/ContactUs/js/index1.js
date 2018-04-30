window.onload = function () {
    document.getElementById("contact-submit").onclick = function (ev) {
        username = document.getElementById('username');
        email = document.getElementById('email');
        text = document.getElementById('message');
        if (username.value.length == 0)
        {
            document.getElementById("contact-text").style.color = "red";
            document.getElementById("contact-text").innerHTML = "Please Fill Name Field";
        } else if (email.value.length == 0){
            document.getElementById("contact-text").style.color = "red";
            document.getElementById("contact-text").innerHTML = "Please Fill Email Field";
        } else if (!validateEmail(email.value)){
            document.getElementById("contact-text").style.color = "red";
            document.getElementById("contact-text").innerHTML = "Please Enter Email Correctly";
        } else if (text.value.length == 0){
            document.getElementById("contact-text").style.color = "red";
            document.getElementById("contact-text").innerHTML = "Please Enter Text";
        } else {
            document.getElementById("contact-text").style.color = "#777";
            document.getElementById("contact-text").innerHTML = "Contact Form";
        }
    }
    document.getElementById()
    function validateEmail(email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
}