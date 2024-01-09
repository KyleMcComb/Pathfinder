/**
 * @Author - @DeanLogan
 * @Description - Executes when the chatbot page loads to initialize and display introductory messages.
 * Displays instructions and capabilities of the chatbot to help EEECS students.
 */
function chatbotPageLoad() {
    // Display introductory messages to the user
    displayText("Hello I am Pathfinder. A chatbot to help EEECS Students. Here is a list of commands to use: <br><br>- What do you do?<br>- What can you help me with? <br>- I'm in first year<br>- I'm in second year<br>- I'm in fourth year<br>- I'm in final year<br>","botText");
    displayText("I can recommend you modules based off your likes or dislikes. Try saying 'I like ai' or 'i hate ai' and I will recommend a module based off your response.","botText");
}

/**
 * @Author - @DeanLogan
 * @Description - Sets up event listeners for the chatbot page to handle user input and window resizing.
 */
function listenersForChatbotPage() {
    // Listen for the Enter key press event on the user input field
    var input = document.getElementById("userInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            usersInput = input.value;
            processUserInput(usersInput); // Process the user's input
            input.value = "";
            event.preventDefault();
            displayText(usersInput, "userText"); // Display the user's input as a message
        }
    });
}

/* START OF CHATBOT CODE */
/**
 * @Author - @DeanLogan
 * @Description - Displays a message in the chatbot interface with a specified sender.
 * Scrolls to the bottom of the chat content for viewing the new message.
 * @param {string} message - The message text to be displayed.
 * @param {string} sender - The sender of the message (either 'botText' or 'userText').
 */
function displayText(message, sender) {
    if (message.trim().length > 0) {
        // Append the message to the chatbot interface with the specified sender
        $(".chatbot").append('<div class=' + sender + '><p>' + message + '</p></div>');
        
        setTimeout(() => {
            $(window).scrollTop($(document).height());
        }, 30); // Wait 30ms for response from the chatbot and then scroll to the bottom of the screen
    }
}

/**
 * @Author - @KyleMcComb
 * @Description - Sends message to the chatbot, then passes the result of this message to the displatText functio
 * @param {string} inputMessage - a message in form of a string that will be sent to the chatbot
 */
function processUserInput(inputMessage) {
    // Make an AJAX request to your server to get the bot response
    $.get("/receive_message/", { message: inputMessage }, function (data) {
        displayText(data.message, "botText"); //display bot response 
    });
}




// Execute chatbotPageLoad function when the window finishes loading
window.onload = chatbotPageLoad();

// Set up event listeners for the chatbot page
listenersForChatbotPage();