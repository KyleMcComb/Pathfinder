var visible = true;
var myTimer;
var myTimerTypeWriter;

//runs when the page is loaded
function pageLoad(){
    sessionStorage.setItem("navOpen","true"); //makes sure the nav is closed whenever the page loads
    navToggle();
    checkTheme();
    resizeChatbotDiv();

    var colourFound = false;
    var txt = document.getElementsByClassName('conversationArea')[0].textContent; //gets the text inside the HTML for the typewriter effect
    window.setInterval('cursor()',400); //used to make the underscore cursor blink


    document.getElementsByClassName('conversationArea')[0].innerHTML = '';
    myTimerTypeWriter = setTimeout(function(){
        typeWriter(txt, colourFound, 'conversationArea');
    },400); 
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

//makes the curosr blink
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
    var chatbotDiv = document.getElementsByClassName('chatbot')[0];
    var textboxDiv = document.getElementsByClassName('textbox')[0];
    var textarea = document.getElementById("usersText");
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

function updateChatbotDivWidth(){

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

    var input = document.getElementById("usersText");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            usersText = input.value;
            input.value = "";
            event.preventDefault();
            displayText(usersText);
        }
    });

    window.addEventListener('resize', function(){resizeChatbotDiv()});
}

function displayText(text){
    var conversationArea = document.getElementsByClassName('conversationArea')[0];
    conversationArea.innerHTML += '<p>'+text;
    //typeWriter(text, false, 'conversationArea');
    conversationArea.innerHTML += "</p>";
}

function resizeChatbotDiv(){
    var chatbotDiv = document.getElementsByClassName("chatbot")[0];
    var textboxDiv = document.getElementsByClassName('textbox')[0];
    var textarea = document.getElementById("usersText");
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
