/* 
    @Author: @DeanLogan123
    @Description: This function runs on load for the settings page, it checks the theme that is currently applied to the page then "checks" the corresponding option within the radio button to ensure that the theme matches with the option selected.
*/
function settingsPageLoad(){
    // check the current theme then select this within the radio button.
    var theme = localStorage.getItem('theme');
    if(theme == 'light-mode'){
        document.getElementById('light').checked = true;
    }
    else if(theme == 'high-contrast-mode') {
        document.getElementById('highContrast').checked = true;
    }
    else { // default option is dark mode
        document.getElementById('dark').checked = true;
    }

    // check the current fontSize then select this within the radio button.
    var theme = localStorage.getItem('fontSize');
    if(theme == 'small'){
        document.getElementById('small').checked = true;
    }
    else if(theme == 'large') {
        document.getElementById('large').checked = true;
    }
    else { // default option is dark mode
        document.getElementById('medium').checked = true;
    }
    getAccountInfo()
}

/* 
    @Author: @DeanLogan123
    @Description: Gets the account information for the logged in user then displays this information.
*/
function getAccountInfo(){
    $.get("/accountInfo/", function(data){
        console.log(data);
        if(data != null){
            document.getElementById('account-name').innerHTML = data.name;
            document.getElementById('account-email').innerHTML = data.email;
            document.getElementsByClassName('admin-email')[0].innerHTML = data.adminEmail;
            // if the information below is not in the JSON object it is safe to assume the logged in user is not a student so the information does not apply
            try{ 
                document.getElementById('account-student-number').innerHTML = data.studentNumber;
                document.getElementById('account-pathway').innerHTML = data.pathway;
                document.getElementById('account-semester').innerHTML = data.currentSemester;
                document.getElementById('account-stage').innerHTML = data.currentStage;
            }
            catch(e){}// pass
        }
        else{}// pass
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Changes the theme and font size based on the new value that has been "checked" within the corresponding radio button, updates this within local storage. 
*/
function updateAccessabilityOptions(){
    //change the theme based on what the user has selected
    var theme = document.querySelector('input[name="theme"]:checked').value;
    if(theme == 'light-mode'){
        localStorage.setItem('theme','light-mode');
    }
    else if(theme == 'high-contrast-mode') {
        localStorage.setItem('theme','high-contrast-mode');
    }
    else { // default option is dark mode
        localStorage.setItem('theme','dark-mode');
    }
    checkTheme();

    //change the font size based on what the user has selected
    var fontSize = document.querySelector('input[name="fontSize"]:checked').value;
    if(fontSize == 'small'){
        localStorage.setItem('fontSize','small');
    }
    else if(fontSize == 'large') {
        localStorage.setItem('fontSize','large');
    }
    else { // default option is medium
        localStorage.setItem('fontSize','medium');
    }
}

window.onload = settingsPageLoad();