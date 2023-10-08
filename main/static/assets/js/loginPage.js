var pathwayData = ''; // global variable that will hold information on each of the pathways which is taken from the database

/**
 * @Author - @DeanLogan
 * @Description - Executes when the page loads to ensure set up of event listeners.
 */
function loginPageLoad() {
    loginListeners(); // Add event listeners to the page
}

/**
 * @Author - @DeanLogan
 * @Description - Holds event listeners that are applied to every web page.
 */
function loginListeners() {
    document.addEventListener("keypress", function(event) {
        if (event.key == "Enter" && (event.target.id == "username" || event.target.id == "password")) {
            console.log("Enter pressed");
            login();
        }
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Gathers the entered login information and sends a POST request to verify the credentials.
 * If successful, the user is logged in; if not, an alert is displayed.
 */
function login() {
    // Send a POST request to verify login credentials
    $.post('/verify/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        'g-recaptcha-response': document.getElementsByName('g-recaptcha-response')[0].value, // Include reCAPTCHA response
        'code': document.getElementById('code').value // Include 2FA code
    }, function (data) {
        if (data.loggedIn == 'true') {
            // If login is successful, display a success alert and reload the page
            alert('Login success');
            window.location.href = '/';
        } else {
            // If login fails, display an alert
            alert(data.errors);
            location.reload();
        }
    });
}


// Run the pageLoad function when the window is fully loaded
window.onload = loginPageLoad();