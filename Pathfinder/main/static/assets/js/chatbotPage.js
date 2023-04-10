function chatbotPageLoad(){
    displayText("Hello I am Pathfinder. A chatbot to help EEECS Students. Here is a list of commands to use: <br><br>- What do you do?<br>- What can you help me with? <br>- I'm in first year<br>- I'm in second year<br>- I'm in fourth year<br>- I'm in final year<br>","botText");
    displayText("I can recommend you modules based off your likes or dislikes. Try saying 'I like ai' or 'i hate ai' and I will recommend a module based off your response.","botText");
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
    var bottomBarDiv = document.getElementsByClassName('bottom-bar')[0];
    var textarea = document.getElementById("userInput");
    var windowWidth = window.innerWidth;

    document.getElementsByClassName('content')[0].style.height = (window.innerHeight - 85) + "px";
    console.log(document.getElementsByClassName('content')[0].style.height);
    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        bottomBarDiv.style.width = (windowWidth-250)+"px";
        bottomBarDiv.style.left = "250px";
        textarea.style.width = (windowWidth-370)+"px";
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        bottomBarDiv.style.width = (windowWidth-55)+"px";
        bottomBarDiv.style.left = "55px";
        textarea.style.width = (windowWidth-175)+"px";
    }
}

function navToggleOnChatbotPage(){
    navToggle();
    resizeChatbotPage();
}

/* START OF CHATBOT CODE */

function displayText(message, sender) {
    if (message.trim().length > 0) {
        $(".chatbot").append('<div class=' + sender + '><p>' + message + '</p></div>');
        const element = $('.content');
        element.animate({
            scrollTop: element.prop("scrollHeight")
        }, 30);
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