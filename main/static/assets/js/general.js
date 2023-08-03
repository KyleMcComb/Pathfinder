var pathwayData = ''; // global variable that will hold information on each of the pathways which is taken from the database

/* 
    @Author: @DeanLogan123
    @Description: Runs when any page is loaded, it will ensure the sidebar (nav) is closed on page load, then it check the theme and font size, along with getting all the pathway data and setting the stage options for the sign-up pop up.
*/
function pageLoad(){
    // makes sure the nav is closed whenever the page loads and ensures all UI elements are sized correctly according to the current window size
    sessionStorage.setItem('navOpen','true'); 
    navToggle();
    resizeContentDiv();
    // checks the theme and font size then resizes the page accordingly
    checkTheme();
    checkFontSize()
    // functions used to ensure the data on the sign-up pop up is correct
    updateStageOptions();
    getPathwayData();
    listeners();
}

/* 
    @Author: @DeanLogan123
    @Description: Sends get request to receive a JSON object that contains all of the pathway information within the database.
*/
function getPathwayData(){
    $.get('/listOfPathways/', function(data){
        pathwayData = data.pathwayList;
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Logs the user out of their session and sends a pop up to alert the user of this.
*/
function logout(){
    alert('You have successfully logged out of the system.');
    window.location.href = '/logout';
}

/* 
    @Author: @DeanLogan123
    @Description: Checks what theme is in the local storage and updates the webpage accordingly 
*/
function checkTheme(){
    var theme = localStorage.getItem('theme');
    let element = document.body;

    // removes the 2 none default themes to turn the page into the default dark mode
    element.classList.remove('light-mode');
    element.classList.remove('high-contrast-mode');

    // checks for new theme, if light mode or high contrast is not selected then the default (dark mode) remains in place
    if(theme == 'light-mode'){ 
        element.classList.add('light-mode');
    }
    else if(theme == 'high-contrast-mode') {
        element.classList.add('high-contrast-mode');
    }
}

/* 
    @Author: @DeanLogan123
    @Description: Checks what font size is in the local storage and updates the webpage accordingly 
*/
function checkFontSize(){
    var fontSize = localStorage.getItem('fontSize');
    var element = document.body;

    // checks for new font size, if small or large size is not selected the default (medium) is then applied
    if(fontSize == 'small'){ 
        element.style.fontSize  = '1.18vh';
    }
    else if(fontSize == 'large') {
        element.style.fontSize = '2.31vh';
    }
    else {
        element.style.fontSize  = '1.48vh'; 
    }
    resiveClosebtn(); // resizes the close button (burger icon for nav toggle) as the size of this icon depends on the sidebar width not what the user has selected as their font size
}

/* 
    @Author: @DeanLogan123
    @Description: Toggles the side bar (nav) open or closed, the state of the side bar is stored in session storage
*/
function navToggle() {
    var navOpen = sessionStorage.getItem('navOpen');
    // CLOSE THE NAV
    if(navOpen == 'true'){
        sessionStorage.setItem('navOpen','false'); // navOpen in session storage is a true or false string, the reason it is a string and not a boolean is because you can only store string variables within session storage.
    }
    // OPEN THE NAV
    else if(navOpen == 'false'){
        sessionStorage.setItem('navOpen','true');
    }
    resizeNav(sessionStorage.getItem('navOpen'));
    resizeContentDiv();
}

/* 
    @Author: @DeanLogan123
    @Description: Resizes the width of the nav based on whether it is open or closed and the current width of the viewport.
    @param: navOpen - A string that will either be true or false for that represents the state of the side bar (true for open, false for closed)
*/
function resizeNav(navOpen){
    var windowWidth = window.innerWidth;
    // CLOSE THE NAV
    if(navOpen == 'false'){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            document.getElementsByClassName('sidebar')[0].style.width = '32px';
        }
        else{
            document.getElementsByClassName('sidebar')[0].style.width = '2.864vw';
        }
    }
    // OPEN THE NAV
    else if(navOpen == "true"){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            document.getElementsByClassName('sidebar')[0].style.width = '145.22px';
        }
        else{
            document.getElementsByClassName('sidebar')[0].style.width = '13vw';
        }
    }
    resiveClosebtn();
    document.getElementsByClassName('sidebar')[0].style.height = '100vh';
}

/* 
    @Author: @DeanLogan123
    @Description: Ensures the close button (menu icon or often called "burger" icon that toggles the nav).
*/
function resiveClosebtn(){
    var windowWidth = window.innerWidth;
    var closebtn = document.getElementsByClassName('closebtn')[0];
    if(windowWidth < 1117.1){
        closebtn.style.fontSize = '20.1076px';
    }
    else {
        closebtn.style.fontSize = '1.8vw';
    }
}

/* 
    @Author: @DeanLogan123
    @Description: Ensures the close button (menu icon or often called "burger" icon that toggles the nav).
*/
function resizeContentDiv(){
    var contentDiv = document.getElementsByClassName('content')[0];
    var windowWidth = window.innerWidth;

    // NAV IS OPEN
    if(sessionStorage.getItem('navOpen') == 'true'){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            contentDiv.style.width = (windowWidth-145)+'px';
            contentDiv.style.left = '145px';
        }
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        else{
            contentDiv.style.width = windowWidth-(windowWidth*0.13)+'px';
            contentDiv.style.left = windowWidth*0.13+'px';
        }
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem('navOpen') == 'false'){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            contentDiv.style.width = (windowWidth-32)+'px';
            contentDiv.style.left = '32px';
        }
        else{
            contentDiv.style.width = windowWidth-(windowWidth*0.0286)+'px';
            contentDiv.style.left = windowWidth*0.0286+'px';
        }
    }
}

/* 
    @Author: @DeanLogan123
    @Description: Holds event listeners that are applied to every web page. 
*/
function listeners(){
    window.addEventListener('resize', function(){resizeContentDiv()}); // checks whenever window is resized, when resized then UI elements will be resized
    window.addEventListener('resize', function(){resizeNav(sessionStorage.getItem('navOpen'))}); // checks whenever window is resized, then resizes the side bar (nav) to ensure it's proportional with the rest of the web page

    // below is code for the menu animation - gets the index of the html tag that is being hovered over within menu-items, then sets this index as the active index which will then apply the correct animation according to the CSS 
    const menu = document.getElementById('menu');

    Array.from(document.getElementsByClassName('menu-item')).forEach((item, index) => {
        item.onmouseover = () => {
            menu.dataset.activeIndex = index;
        }
    });

    /* Login and signup */
    // When the user clicks anywhere outside of the modal (pop up), close it
    window.onclick = function(event) {
        if (event.target == document.getElementById('id01')| event.target == document.getElementById('id02')) {
            document.getElementById('id01').style.display = "none";
            document.getElementById('id02').style.display = "none";
        }
    }
}

/* 
    @Author: @DeanLogan123
    @Description: Displays the sign-up pop up, adds all the pathways to the radio buttons that are in the sign-up pop up 
*/
function displaySignUpPage(){
    var pathwayList = pathwayData;
    var htmlFormat = '';
    for(var i=0; i<pathwayList.length; i++){
        var checked = '';
        if(i==0){
            checked = 'checked="true"';
        }
        var pathwayNames = pathwayList[i].name;
        var pathwaysHtmlClassFormat = pathwayNames.replace(/\s/g,'');
        htmlFormat += `
            <label for="${pathwaysHtmlClassFormat}"><input type="radio" ${checked} id="${pathwaysHtmlClassFormat}" name="pathway" onchange="updateStageOptions()" value="${pathwayNames}" /> ${pathwayNames}</label><br />
        `; // html to create a radio button for the pathway at i index within pathwayList 
    }
    document.getElementsByClassName('Pathway')[0].innerHTML = htmlFormat;
    document.getElementById('id02').style.display='block';
    updateStageOptions(); // this will change how many stages appear for the stage radio buttons depending on the stages that are within the selected module
}

/* 
    @Author: @DeanLogan123
    @Description: Change how many stages appear for the stage radio buttons depending on the stages that are within the selected module 
*/
function updateStageOptions(){
    document.getElementsByClassName('stage-4')[0].style.display = 'none';
    var selectedPathway = document.querySelector('input[name="pathway"]:checked').value;
    // update this so that it will be able to see which modules have 4 stages, then apply the fourStageCourse to it
    for(var i=0; i<pathwayData.length; i++){
        var pathwayName = pathwayData[i].name;
        if(selectedPathway == pathwayName && pathwayData[i].stages == 4){
            document.getElementsByClassName('stage-4')[0].style.display = '';
        }
    }
}

/* 
    @Author: @DeanLogan123
    @Description: Displays the next part for sign-up, it will gather the information that the user has enetered in sign-up-1 and send a GET request with this information, then if the request is a success then sign-up-2 will be displayed if not an alert is sent.
*/
function goToSignUp2(){
    document.getElementById('sign-up-1').style.display = 'none';
    document.getElementById('sign-up-2').style.display = 'block';

    var studentNumber = document.querySelector('input[name="student-number-sign-up"]').value;
    var name = document.querySelector('input[name="name"]').value;
    var email = document.querySelector('input[name="email"]').value;
    var selectedPathway = document.querySelector('input[name="pathway"]:checked').value;
    var currentStage = document.querySelector('input[name="stage"]:checked').value;
    var currentSemester = document.querySelector('input[name="semester"]:checked').value;

    signUpInfo = {
        'studentNumber':studentNumber,
        'name':name,
        'email':email,
        'selectedPathway':selectedPathway,
        'currentStage':currentStage,
        'currentSemester':currentSemester
    }

    $.get('/signUp/', signUpInfo, function (data) {
        if(data.success == 'true'){
            document.getElementById('sign-up-1').style.display = 'none';
            document.getElementById('sign-up-2').style.display = 'block';
        }
        else{
            alert('Sign up failed, try again.');
        }
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Gathers the information entered within the login then sends a GET request to verify the login credentials entered, if successful the user is logged in if not the user will be alerted that authentication failed.
*/
function login(){
    var username = document.querySelector('input[name="student-number-login"]').value;
    var password = document.getElementById('password-login').value;
    $.get('/verify/', { username: username, password: password }, function (data) {
        if(data.loggedIn == 'true'){
            alert('Login success');
            location.reload();
        }
        else{
            alert("Login failed, either student number or password is incorrect");
        }
    });
}

window.onload = pageLoad();
