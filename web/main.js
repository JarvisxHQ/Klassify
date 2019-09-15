function printData() {
    var type = document.getElementById("classificationType");
    var data = type.value;
    loadingSpinner = document.getElementById("spinner");
    if(data == "News") {
        loadingSpinner.style = "color: #ffc107";
    } else if(data == "Articles") {
        loadingSpinner.style = "color: #28a745";
    } else if(data == "Tweets") {
        loadingSpinner.style = "color: #007bff";
    } else if(data == "Emails") {
        loadingSpinner.style = "color: #17a2b8";
    } else if(data == "Chats") {
        loadingSpinner.style = "color: #f8f9fa";
    } else {
        type.placeholder = "Not valid"; 
        type.value = "";
        loadingSpinner.style = "color: 	#000000";
    }
}