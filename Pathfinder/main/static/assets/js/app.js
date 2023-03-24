var visible = true;
var myTimer;
var myTimerTypeWriter;

//runs when the page is loaded
function pageLoad(){
    sessionStorage.setItem("navOpen","true"); //makes sure the nav is closed whenever the page loads
    navToggle();
    checkTheme();
    resizeChatbotDiv();

    displayText("put instructions here?","botText");

    // uncomment the below code to add the typewrite affect for the intro text from the chatbot
    //var colourFound = false;
    //var txt = document.getElementsByClassName('conversationArea')[0].textContent; //gets the text inside the HTML for the typewriter effect
    //document.getElementsByClassName('conversationArea')[0].innerHTML = '';
    // myTimerTypeWriter = setTimeout(function(){
    //     typeWriter(txt, colourFound, 'conversationArea');
    // },400); 
    //window.setInterval('cursor()',400); //used to make the underscore cursor blink
}

//checks what theme is in the local storage and updates the webpage accordingly 
function checkTheme(){
    var theme = localStorage.getItem('theme');
    if(theme == 'light-mode'){
        let element = document.body;
        element.classList.toggle('light-mode');
    }
}

//this is responsible for the typewriter effect for the titles of each page
function typeWriter(txt, colourFound, className) {
    var i = 0;
    var timer = setInterval(function(){
        //uses the character ? to find where the colour should be swaped in the title (from primary to secondary colour and vise-versa)
        if(txt.charAt(i) == '?'){
            document.getElementsByClassName(className)[0].innerHTML += '<span class="colour"></span>';
            if(!colourFound){
                colourFound = true;
            }
            else{
                colourFound = false;
            }
        }
        else{
            if(!colourFound){
                document.getElementsByClassName(className)[0].innerHTML += txt.charAt(i);
            }
            else{
                document.getElementsByClassName('colour')[0].innerHTML += txt.charAt(i);
            }
        }
        i++;
        if(i > txt.length){
            clearInterval(timer);
        }
    }, 120);
}

//makes the cursor blink
function cursor() {
    if (visible === true) {
        document.getElementById('cursorId').className = 'hidden';
        visible = false;
    } 
    else {
        document.getElementById('cursorId').className = 'visable';
        visible = true;
    }
}

function navToggle() {
    // CLOSE THE NAV
    var chatbotDiv = document.getElementById('chatbot');
    var textboxDiv = document.getElementsByClassName('textbox')[0];
    var textarea = document.getElementById("usersInput");
    var windowWidth = window.innerWidth;
    if(sessionStorage.getItem("navOpen") == "true"){
        document.getElementsByClassName('sidebar')[0].style.width = "55px";
        chatbotDiv.style.width = (windowWidth-55)+"px";
        chatbotDiv.style.left = "55px";
        textboxDiv.style.width = (windowWidth-55)+"px";
        textboxDiv.style.left = "55px";
        textarea.style.width = (windowWidth-175)+"px";
        sessionStorage.setItem("navOpen","false");
    }
    // OPEN THE NAV
    else if(sessionStorage.getItem("navOpen") == "false"){
        document.getElementsByClassName('sidebar')[0].style.width = "250px";
        chatbotDiv.style.width = (windowWidth-250)+"px";
        chatbotDiv.style.left = "250px";
        textboxDiv.style.width = (windowWidth-250)+"px";
        textboxDiv.style.left = "250px";
        textarea.style.width = (windowWidth-370)+"px";
        sessionStorage.setItem("navOpen","true");
    }
}

function listeners(){
    //toggle theme
    var themeBtn = document.querySelector('.theme-btn');
    themeBtn.addEventListener('click', () =>{
        var theme = localStorage.getItem('theme');
        let element = document.body;
        element.classList.toggle('light-mode');
        if(theme == 'dark-mode'){
            localStorage.setItem('theme','light-mode');
        }
        else{
            localStorage.setItem('theme','dark-mode');
        }
    });

    var input = document.getElementById("userInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            userInput = input.value;
            input.value = "";
            event.preventDefault();
            displayText(userInput);
        }
    });

    window.addEventListener('resize', function(){resizeChatbotDiv()});
}

function displayText(message, sender){
    $("#chatbot").append('<div class='+sender+'><p>'+message+'</p></div>');
}

/*
function getResponse() {
    let userText = $("textbox").val();
    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';
    $("#userInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById('userInput').scrollIntoView({ block: 'start', behaviour: 'smooth' });
    $.get("/get", { msg: userText }).done(function (data) {
        var botHtml = '<p><span class="conversationArea">' + data + '</span></p>';
        $("#chatbox").append(botHtml);
        document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
    });
}

$("#userInput").keypress(function (e) {
    //if enter key is pressed
    if (e.which == 13) {
        getResponse();
    }
});
/* Placeholder if we add a button.
$("#buttonInput").click(function () {
    getResponse();
}); */

/*
$("#userInput").keypress(function (e) {
    //if enter key is pressed
    if (e.which == 13) {
        e.preventDefault();
        $.ajax({
            url: 'http://localhost:8000/message?message=' + encodeURIComponent($('#userInput').val()),
            type: 'GET',
            dataType: 'text', // specify the data type as text
            success: function (response) {
                $('<p>').text(response).appendTo('.conversationArea');
            }
        });
        /*$('#userInput').val('');
    }
}); */



function resizeChatbotDiv(){
    var chatbotDiv = document.getElementById("chatbot");
    var textboxDiv = document.getElementsByClassName('textbox')[0];
    var textarea = document.getElementById("usersInput");
    var windowWidth = window.innerWidth;

    chatbotDiv.style.height = (window.innerHeight - 85) + "px";
    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        chatbotDiv.style.width = (windowWidth-250)+"px";
        chatbotDiv.style.left = "250px";
        textboxDiv.style.width = (windowWidth-250)+"px";
        textboxDiv.style.left = "250px";
        textarea.style.width = (windowWidth-370)+"px";
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        chatbotDiv.style.width = (windowWidth-55)+"px";
        chatbotDiv.style.left = "55px";
        textboxDiv.style.width = (windowWidth-55)+"px";
        textboxDiv.style.left = "55px";
        textarea.style.width = (windowWidth-175)+"px";
    }
}

window.onload = pageLoad();

listeners();

/*menu animation */
const menu = document.getElementById("menu");

Array.from(document.getElementsByClassName("menu-item")).forEach((item, index) => {
    item.onmouseover = () => {
        menu.dataset.activeIndex = index;
    }
});

/* Login */
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}