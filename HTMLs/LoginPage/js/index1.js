window.onload = function () {
  document.getElementById("login_button").onclick = function (ev) {
    // alert(document.getElementById("login_username").value + "   " + document.getElementById("login_password").value + "  ");
    if (document.getElementById("login_username").value == "Allarious" && document.getElementById("login_password").value == 12345)
    {
      document.getElementById("welcome").innerHTML = "Access Granted";
    }else {
        document.getElementById("welcome").innerHTML = "Access Denied";
    }
  }
    document.getElementById("forget-label").onclick = function (ev1) {
        document.getElementById("welcome").innerHTML = "Forgot your password? Oops! we cant give it back to you... yet! :P"
    }
}