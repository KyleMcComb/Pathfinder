var visible = true;
var myTimer;
var myTimerTypeWriter;

//runs when the page is loaded
function pageLoad(){
    checkTheme();
    var colourFound = false;
    var txt = document.getElementsByClassName('conversationArea')[0].textContent; //gets the text inside the HTML for the typewriter effect
    window.setInterval('cursor()',400); //used to make the underscore cursor blink
    document.getElementsByClassName('conversationArea')[0].innerHTML = '';
    myTimerTypeWriter = setTimeout(function(){
        typeWriter(txt, colourFound, 'conversationArea');
    },900); //waits for the transition to happen before starting the typewriter effect

    //helps make the animation look smoother if the certs and online courses for the about page load in after the transition animation
    if ( document.URL.includes("about") ) {
        myTimer = setInterval('imageLoad()', 550);
    }
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
}

function displayText(text){
    var conversationArea = document.getElementsByClassName('conversationArea')[0];
    conversationArea.innerHTML += '<p className="">';
    typeWriter(text, false, 'conversationArea');
    conversationArea.innerHTML += "";
}

window.onload = pageLoad();

listeners();
