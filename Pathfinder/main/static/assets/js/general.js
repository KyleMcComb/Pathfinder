var visible = true;
var myTimer;
var myTimerTypeWriter;

//runs when the page is loaded
function pageLoad(){
    sessionStorage.setItem("navOpen","false"); //makes sure the nav is closed whenever the page loads
    checkTheme();
    checkFontSize()
    resizeContentDiv();
}

//checks what theme is in the local storage and updates the webpage accordingly 
function checkTheme(){
    var theme = localStorage.getItem('theme');
    let element = document.body;

    // removes the 2 none default themes to turn the page into the default dark mode
    element.classList.remove('light-mode');
    element.classList.remove('high-contrast-mode');

    // checks for new theme, if light mode or high contrast is not selected the default (dark mode) is then applied
    if(theme == 'light-mode'){ 
        element.classList.add("light-mode");
    }
    else if(theme == 'high-contrast-mode') {
        element.classList.add("high-contrast-mode");
    }
}

function checkFontSize(){
    var fontSize = localStorage.getItem('fontSize');
    let element = document.body;

    // checks for new font size, if small or large size is not selected the default (medium) is then applied
    if(fontSize == 'small'){ 
        element.style.fontSize  = "0.9rem";
    }
    else if(fontSize == 'large') {
        element.style.fontSize = "1.6rem";
        document.getElementsByClassName("menu-item")[1].innerHTML = "Grade <br />Dashboard";
        document.getElementsByClassName("menu-item")[3].innerHTML = "Queen's <br />Website";
    }
    else {
        element.style.fontSize  = "1.1rem";
    }
}

function navToggle() {
    // CLOSE THE NAV
    if(sessionStorage.getItem("navOpen") == "true"){
        document.getElementsByClassName('sidebar')[0].style.width = "55px";
        sessionStorage.setItem("navOpen","false");
    }
    // OPEN THE NAV
    else if(sessionStorage.getItem("navOpen") == "false"){
        document.getElementsByClassName('sidebar')[0].style.width = "250px";
        sessionStorage.setItem("navOpen","true");
    }
    resizeContentDiv();
}

function resizeContentDiv(){
    var contentDiv = document.getElementsByClassName("content")[0];
    var windowWidth = window.innerWidth;

    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        contentDiv.style.width = (windowWidth-250)+"px";
        contentDiv.style.left = "250px";
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        contentDiv.style.width = (windowWidth-55)+"px";
        contentDiv.style.left = "55px";
    }
}

function listeners(){
    window.addEventListener('resize', function(){resizeContentDiv()});
}

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

window.onload = pageLoad();

listeners();

