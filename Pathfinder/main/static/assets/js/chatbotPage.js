/* 
    @Author: @DeanLogan123
    @Description: This function runs on load for the chatbot page, it sends a 2 messages to the user from the "chatbot" that gives the user instructions on how to use the system. It then resizes the chatbot page to ensure that all UI elements fit for the users screen resolution. 
*/
function chatbotPageLoad(){
    displayText("Hello I am Pathfinder. A chatbot to help EEECS Students. Here is a list of commands to use: <br><br>- What do you do?<br>- What can you help me with? <br>- I'm in first year<br>- I'm in second year<br>- I'm in fourth year<br>- I'm in final year<br>","botText");
    displayText("I can recommend you modules based off your likes or dislikes. Try saying 'I like ai' or 'i hate ai' and I will recommend a module based off your response.","botText");
    resizeChatbotPage();
}

/* 
    @Author: @DeanLogan123
    @Description: Holds all the event listeners for this page. 
*/
function listenersForChatbotPage(){
    // whenever a user enters text check if the enter key is pressed, then if pressed clear input and display users text
    var input = document.getElementById("userInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            usersInput = input.value;
            input.value = "";
            event.preventDefault();
            displayText(usersInput,"userText"); // Process the user input and get the bot response
        }
    });

    window.addEventListener('resize', function(){resizeChatbotPage()}); // checks whenever window is resized, when resized then UI elements will be resized
}

/* 
    @Author: @DeanLogan123
    @Description: This will resize the bottom bar div and the textarea widget to ensure they match for all screen resolutions, it will also check if the sidebar (nav) is open to ensure no UI elements overlap.
*/
function resizeChatbotPage(){
    var bottomBarDiv = document.getElementsByClassName('bottom-bar')[0];
    var textarea = document.getElementById("userInput");
    var windowWidth = window.innerWidth;

    document.getElementsByClassName('content')[0].style.height = (window.innerHeight - 85) + "px";
    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            bottomBarDiv.style.width = (windowWidth-145)+'px';
            bottomBarDiv.style.left = '145px';
            textarea.style.width = (windowWidth-(windowWidth*0.0625)-145)+"px"; // the 0.0625 in the equation is to compensate for the padding between the textarea and the sidebar
        }
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        else{
            bottomBarDiv.style.width = windowWidth-(windowWidth*0.13)+'px';
            bottomBarDiv.style.left = windowWidth*0.13+'px';
            textarea.style.width = windowWidth-(windowWidth*0.1925)+"px"; // the 0.1925 in the equation is to compensate for the padding between the textarea and the sidebar
        }
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            bottomBarDiv.style.width = (windowWidth-32)+'px';
            bottomBarDiv.style.left = '32px';
            textarea.style.width = (windowWidth-(windowWidth*0.0625)-32)+"px"; // the 0.0625 in the equation is to compensate for the padding between the textarea and the sidebar
        }
        else{
            bottomBarDiv.style.width = windowWidth-(windowWidth*0.0286)+'px';
            bottomBarDiv.style.left = windowWidth*0.0286+'px';
            textarea.style.width = windowWidth-(windowWidth*0.0911)+"px"; // the 0.0911 in the equation is to compensate for the padding between the textarea and the sidebar
        }
    }
}

/* 
    @Author: @DeanLogan123 
    @Description: Toggles sidebar (nav) open and closed, different from default navToggle (seen in general.js) to ensure the bottom bar div and textarea are resized accordingly.
*/
function navToggleOnChatbotPage(){
    navToggle();
    resizeChatbotPage();
}

/* START OF CHATBOT CODE */

/* 
    @Author: @DeanLogan123
    @Description: This will display text within a chat bubble either on the left side of the screen (sender is bot) or the right side of the screen (sender is user).
    @param: message - This is a string that's within html format that will be used to display the text within the chat bubble.
    @param: sender - This decides who the message will be sent from. Value will either be botText or userText as this will set the class of the div which in turn will display the message either from the chatbot or the user.
*/
function displayText(message, sender) {
    if (message.trim().length > 0) {
        $(".chatbot").append('<div class=' + sender + '><p>' + message + '</p></div>');
        const element = $('.content');
        element.animate({
            scrollTop: element.prop("scrollHeight")
        }, 30); // waits 30ms for response from chatbot
    }
}

/* 
    @Author: @KyleMcComb
    @Description: Sends message to the chatbot, then passes the result of this message to the displatText function
    @param: inputMessage - a message in form of a string that will be sent to the chatbot
*/
function processUserInput(inputMessage) {
    // Make an AJAX request to your server to get the bot response
    $.get("/receive_message/", { message: inputMessage }, function (data) {
        displayText(data.message, "botText"); //display bot response 
    });
}


/* END OF CHATBOT CODE */

window.onload = chatbotPageLoad();

listenersForChatbotPage();