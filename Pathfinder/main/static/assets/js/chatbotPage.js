function chatbotPageLoad(){
    displayText("Where introduction can go","botText");
    resizeChatbotPage();
}

function listenersForChatbotPage(){
    // whenever a user enters text
    var input = document.getElementById("userInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            usersInput = input.value;
            input.value = "";
            event.preventDefault();
            displayText(usersInput,"userText");
        }
    });

    window.addEventListener('resize', function(){resizeChatbotPage()});
}

function resizeChatbotPage(){
    var textboxDiv = document.getElementsByClassName('textbox')[0];
    var textarea = document.getElementById("userInput");
    var windowWidth = window.innerWidth;

    document.getElementsByClassName('content')[0].style.height = (window.innerHeight - 85) + "px";
    console.log(document.getElementsByClassName('content')[0].style.height);
    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        textboxDiv.style.width = (windowWidth-250)+"px";
        textboxDiv.style.left = "250px";
        textarea.style.width = (windowWidth-370)+"px";
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        textboxDiv.style.width = (windowWidth-55)+"px";
        textboxDiv.style.left = "55px";
        textarea.style.width = (windowWidth-175)+"px";
    }
}

/* START OF CHATBOT CODE */

function displayText(message, sender) {
    if (message.trim().length > 0) {
        $(".chatbot").append('<div class=' + sender + '><p>' + message + '</p></div>');
        const element = $('.content');
        element.animate({
            scrollTop: element.prop("scrollHeight")
        }, 500);
    }
}

/*
function processUserInput(inputMessage) {
    // Make an AJAX request to your server to get the bot response
    $.ajax({
        type: 'GET',
        url: '/receive_message/',
        data: { message: inputMessage },
        success: function (data) {
            displayText(data.message, 'botText'); // Display the bot response
        }
    });
} */

function processUserInput(inputMessage) {
    // Make an AJAX request to your server to get the bot response
    $.get("/receive_message/", { message: inputMessage }, function (data) {
    displayText(data.message, "botText"); //display bot response 
});
}
// whenever a user enters text
var input = document.getElementById("userInput");
input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        usersInput = input.value.trim();
        if (usersInput.length > 0) {
            input.value = "";
            displayText(usersInput, "userText");
            processUserInput(usersInput); // Process the user input and get the bot response
        }
    }
});

/* END OF CHATBOT CODE */

window.onload = chatbotPageLoad();

listenersForChatbotPage();