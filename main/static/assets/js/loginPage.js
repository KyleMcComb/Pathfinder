/**
 * @Author - @DeanLogan
 * @Description - Executes when the page loads to ensure set up of event listeners.
 */
function loginPageLoad() {
    loginListeners(); // Add event listeners to the page
}

/**
 * @Author - @DeanLogan
 * @Description - Holds event listeners that are applied to the login page.
 */
function loginListeners() {
    document.addEventListener("keypress", function(event) {
        if (event.key == "Enter" && (event.target.id == "username" || event.target.id == "password")) {
            checkTotpDevices();
        }
    });

    document.getElementById("authForm").addEventListener("submit", function(event) {
        document.getElementById('code').disabled=true;
        event.preventDefault();
        login();
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

/**
 * @Author - @DeanLogan
 * Checks if two-factor authentication (2FA) is enabled for the user and takes appropriate action.
 * Sends a POST request with user credentials and 2FA code, then displays a modal if 2FA is enabled, or logs in if not.
 */
function checkTotpDevices() {
    $.post('/hasTwoFactorEnabled/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        'g-recaptcha-response': document.getElementsByName('g-recaptcha-response')[0].value, // Include reCAPTCHA response
        'code': document.getElementById('code').value // Include 2FA code
    }, function (data) {
        if (data.hasTwoFactorEnabled == 'true') {
            document.getElementById('id01').style.display = 'block';
        } else {
            login();
        }
    });
}

/**
 * @Author - @DeanLogan
 * Sends a GET request to initiate the password reset process by providing the student number and email.
 * Displays an alert with the response status.
 */
function forgotPassword() {
    $.get("/forgotPassword/", {
        'studentNumber': document.getElementById('usernameForgotPassword').value,
        'studentEmail': document.getElementById('emailForgotPassword').value,
    
    }, function(data) {
        alert(data.status);
    });
}

// Run the pageLoad function when the window is fully loaded
window.onload = loginPageLoad();