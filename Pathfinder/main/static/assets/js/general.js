var visible = true;
var myTimer;
var myTimerTypeWriter;

//runs when the page is loaded
function pageLoad(){
    sessionStorage.setItem("navOpen","false"); //makes sure the nav is closed whenever the page loads
    checkTheme();
    resizeContentDiv();
}

//checks what theme is in the local storage and updates the webpage accordingly 
function checkTheme(){
    var theme = localStorage.getItem('theme');
    if(theme == 'light-mode'){
        let element = document.body;
        element.classList.toggle('light-mode');
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

