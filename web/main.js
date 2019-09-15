function printData() {
    var type = document.getElementById("classificationType");
    var data = type.value;
    loadingSpinner = document.getElementById("spinner");
    if(data == "News") {
        loadingSpinner.style = "color: #ffc107";
        classifyNews();
    } else if(data == "Articles") {
        loadingSpinner.style = "color: #28a745";
        classifyArticle();
    } else if(data == "Tweets") {
        loadingSpinner.style = "color: #007bff";
        classifyTweet();
    } else if(data == "Emails") {
        loadingSpinner.style = "color: #17a2b8";
        classifyEmail();
    } else if(data == "Chats") {
        loadingSpinner.style = "color: #f8f9fa";
        classifyChat();
    } else {
        type.placeholder = "Not valid"; 
        type.value = "";
        loadingSpinner.style = "color: 	#000000";
    }
}

function classifyNews() {
    setTimeout(function() {
        window.open("news.html","_self");
    }, 500);
}

function classifyArticle() {
    setTimeout(function() {
        window.open("articles.html","_self");
    }, 500);
}

function classifyTweet() {
    setTimeout(function() {
        window.open("tweets.html","_self");
    }, 500);
}

function classifyEmail() {
    setTimeout(function() {
        window.open("emails.html","_self");
    }, 500);
}

function classifyChat() {
    setTimeout(function() {
        window.open("chats.html","_self");
    }, 500);
}