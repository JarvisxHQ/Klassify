function startGame() {
    loadingSpinner = document.getElementById("spinner");
    loadingSpinner.style = "color: #28a745";
    setTimeout(function() {
        window.open("../game.html","_self");
    }, 500);
    //console.log("StartGame");
}

function loadGame() {
    loadingSpinner = document.getElementById("spinner");
    loadingSpinner.style = "color: #ffc107";
    //console.log('LoadGame');
}

function multiplayer() {
    loadingSpinner = document.getElementById("spinner");
    loadingSpinner.style = "color: #17A2B8";
    //console.log('Multiplayer');
}