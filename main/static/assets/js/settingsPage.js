/**
 * @Author - @DeanLogan
 * @Description - Initializes the settings page with the current theme and font size preferences.
 * Retrieves and displays the user's account information.
 */
function settingsPageLoad() {
    // Check the current theme and select it within the radio button.
    var theme = localStorage.getItem('theme');
    if (theme == 'light-mode') {
        document.getElementById('light').checked = true;
    } else if (theme == 'high-contrast-mode') {
        document.getElementById('highContrast').checked = true;
    } else { // Default option is dark mode
        document.getElementById('dark').checked = true;
    }

    // Check the current fontSize and select it within the radio button.
    var fontSize = localStorage.getItem('fontSize');
    if (fontSize == 'small') {
        document.getElementById('small').checked = true;
    } else if (fontSize == 'large') {
        document.getElementById('large').checked = true;
    } else { // Default option is medium font size
        document.getElementById('medium').checked = true;
    }
    
    getAccountInfo();

    displayQRCode();
}

/**
 * @Author - @DeanLogan
 * @Description - Retrieves and displays user account information.
 */
function getAccountInfo() {
    $.get("/accountInfo/", function(data) {
        console.log(data);
        if (data != null) {
            document.getElementById('account-name').innerHTML = data.name;
            document.getElementById('account-email').innerHTML = data.email;
            document.getElementsByClassName('admin-email')[0].innerHTML = data.adminEmail;
            
            // Check if the information below is in the JSON object, which indicates the logged-in user is a student
            try {
                document.getElementById('account-student-number').innerHTML = data.studentNumber;
                document.getElementById('account-pathway').innerHTML = data.pathway;
                document.getElementById('account-semester').innerHTML = data.currentSemester;
                document.getElementById('account-stage').innerHTML = data.currentStage;
            } catch (e) {
                // If the information is not present, the logged-in user is not a student
            }
        } else {
            // Handle case when data is not available
        }
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Updates the accessibility options chosen by the user (theme and font size) and applies them.
 */
function updateAccessabilityOptions() {
    // Change the theme based on what the user has selected
    var theme = document.querySelector('input[name="theme"]:checked').value;
    if (theme == 'light-mode') {
        localStorage.setItem('theme', 'light-mode');
    } else if (theme == 'high-contrast-mode') {
        localStorage.setItem('theme', 'high-contrast-mode');
    } else { // Default option is dark mode
        localStorage.setItem('theme', 'dark-mode');
    }
    checkTheme(); // Apply the updated theme

    // Change the font size based on what the user has selected
    var fontSize = document.querySelector('input[name="fontSize"]:checked').value;
    if (fontSize == 'small') {
        localStorage.setItem('fontSize', 'small');
    } else if (fontSize == 'large') {
        localStorage.setItem('fontSize', 'large');
    } else { // Default option is medium
        localStorage.setItem('fontSize', 'medium');
    }
}

function displayQRCode(){
    $.get('/displayQRCode/', function(data) {
        console.log(data);
        // Create an image element and set the source to the data URI
        var img = document.createElement('img');
        img.src = 'data:image/png;base64,' + data;
        
        // Get the element where you want to display the QR code
        var qrCodeContainer = document.getElementById('qr-code');
        
        // Clear the container and append the image
        qrCodeContainer.innerHTML = '';
        qrCodeContainer.appendChild(img);
    });
}

// Call settingsPageLoad function when the window loads
window.onload = settingsPageLoad();
