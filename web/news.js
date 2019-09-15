function classify() {
    var title = document.getElementById("title").value;
    var article = document.getElementById("article").value;
    eel.classifyNewsArticle(title, article);
}

function returnHome() {
    setTimeout(function() {
        window.open("index.html","_self");
    }, 500);
}