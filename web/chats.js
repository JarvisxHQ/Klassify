function classify() {
    var chat = document.getElementById("chat").value;
    eel.classifyChats(chat);
}

function returnHome() {
    setTimeout(function() {
        window.open("index.html","_self");
    }, 500);
}