function classify() {
    var email = document.getElementById("email").value;
    eel.classifyEmail(email);
}

function returnHome() {
    setTimeout(function() {
        window.open("index.html","_self");
    }, 500);
}