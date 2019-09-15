function classify() {
    var tweet = document.getElementById("tweet").value;
    eel.classifyTweet(tweet);
}

function returnHome() {
    setTimeout(function() {
        window.open("index.html","_self");
    }, 500);
}