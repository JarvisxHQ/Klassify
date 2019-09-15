function printData() {
    var type = document.getElementById("classificationType");
    var data = type.value;
    loadingSpinner = document.getElementById("spinner");
    if(data == "News") {
        console.log("A")
        loadingSpinner.style = "color: #ffc107";
    } else if(data == "Article") {
        console.log("B");
        loadingSpinner.style = "color: #28a745";
    } else if(data == "Tweets") {
        console.log("C");
        loadingSpinner.style = "color: #007bff";
    } else if(data == "Emails") {
        console.log("D");
        loadingSpinner.style = "color: #17a2b8";
    } else if(data == "Chats") {
        console.log("E");
        loadingSpinner.style = "color: #f8f9fa";
    } else {
        type.placeholder = "Not valid"; 
        loadingSpinner.style = "color: 	#000000";
    }
}