var visible = true;
var myTimer;
var myTimerTypeWriter;

//runs when the page is loaded
function pageLoad(){
    sessionStorage.setItem("navOpen","false"); //makes sure the nav is closed whenever the page loads
    checkTheme();
    checkFontSize()
    resizeContentDiv();
    updateStageOptions();
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
        element.style.fontSize  = "0.8rem";
    }
    else if(fontSize == 'large') {
        element.style.fontSize = "1.5rem";
        document.getElementsByClassName("menu-item")[1].innerHTML = "Grade <br />Dashboard";
        document.getElementsByClassName("menu-item")[3].innerHTML = "Queen's <br />Website";
    }
    else {
        element.style.fontSize  = "1rem";
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
    document.getElementsByClassName('sidebar')[0].style.height = "100vh";
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

/* Login and signup*/
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == document.getElementById('id01')| event.target == document.getElementById('id02')) {
        document.getElementById('id01').style.display = "none";
        document.getElementById('id02').style.display = "none";
    }
}

function updateStageOptions(){
    var fourStageCourse = false;
    var selectedPathway = document.querySelector('input[name="pathway"]:checked').value;
    // update this so that it will be able to see which modules have 4 stages, then apply the fourStageCourse to it
    if(selectedPathway == 'SE4'){
        fourStageCourse = true;
    }
    if(fourStageCourse){
        document.getElementsByClassName('stage-4')[0].style.display = '';
    }
    else {
        document.getElementsByClassName('stage-4')[0].style.display = 'none';
    }
}

function goToSignUp2(){
    document.getElementById('sign-up-1').style.display = 'none';
    document.getElementById('sign-up-3').style.display = 'none';
    document.getElementById('sign-up-2').style.display = 'block';
    var selectedPathway = document.querySelector('input[name="pathway"]:checked').value;
    var currentStage = document.querySelector('input[name="stage"]:checked').value;
    var currentSemester = document.querySelector('input[name="semester"]:checked').value;
    
    console.log(selectedPathway);

    var modulePickerDiv = document.getElementsByClassName('module-picker')[0];

    modulePickerDiv.innerHTML = `<p>Pathway: ${selectedPathway}, Stage ${currentStage}, Semester: ${currentSemester}</p>`;

    var stage = parseInt(currentStage);
    var semester = parseInt(currentSemester);

    // need to add logic to check and display the optional modules
    for(var i=0; i<stage; i++){
        modulePickerDiv.innerHTML += ` 
            <h3>Stage ${i+1}</h3>
        `;
        addCheckBoxesForModules((i+1), 1);
        if (!((stage-1) == i && semester == 1)) {
            addCheckBoxesForModules((i+1), 2);
        }
    }
}

function addCheckBoxesForModules(stage, semester){
    var listOfModulesToDisplay = ['module 1','module 2','module 3','module 4','module 5','module 6','module 7','module 8'];
    var modulePickerDiv = document.getElementsByClassName('module-picker')[0];
    var htmlCode = '';
    htmlCode += `<form><fieldset class="semesters">`;
    htmlCode += `<legend>Semester ${semester}</legend>`;
    for(var i=0; i<listOfModulesToDisplay.length; i++){
        htmlCode += `
            <input type="checkbox" id="${listOfModulesToDisplay[i]}" name="modules-${stage}-${semester}" value="${listOfModulesToDisplay[i]}">
            <label for="${listOfModulesToDisplay[i]}">${listOfModulesToDisplay[i]}</label>
        `;
    }
    htmlCode += `</fieldset></form>`;
    modulePickerDiv.innerHTML += htmlCode;
}

function goToSignUp1(){
    document.getElementById('sign-up-2').style.display = 'none';
    document.getElementById('sign-up-3').style.display = 'none';
    document.getElementById('sign-up-1').style.display = 'block';
}

function goToSignUp3(){
    document.getElementById('sign-up-1').style.display = 'none';
    document.getElementById('sign-up-2').style.display = 'none';
    document.getElementById('sign-up-3').style.display = 'block';
}

window.onload = pageLoad();

listeners();

