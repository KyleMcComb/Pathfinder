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
}

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