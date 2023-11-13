var pathwayData = ''; // global variable that will hold information on each of the pathways which is taken from the database

/**
 * @Author - @DeanLogan
 * @Description - Executes when the page loads to ensure proper initialization and sizing of UI elements.
 * Handles navigation, theme, font size, sign-up data, and sets up event listeners.
 */
function pageLoad() {
    // Ensure the navigation sidebar is closed whenever the page loads and adjust UI elements
    sessionStorage.setItem('navOpen', 'true');
    navToggle();

    // Check the theme and font size settings, and resize the page accordingly
    checkTheme();
    checkFontSize();

    // Update stage options, gather pathway data, and set up event listeners
    updateStageOptions();
    getPathwayData();
    listeners();
}


/**
 * @Author - @DeanLogan
 * @Description - Retrieves pathway data by making an AJAX request to the server's endpoint.
 */
function getPathwayData() {
    // Make an AJAX request to fetch the list of pathways from the server
    $.get('/listOfPathways/', function(data) {
        pathwayData = data.pathwayList; // Store the retrieved pathway data
    });
}


/**
 * @Author - @DeanLogan
 * @Description - Logs out the user from the system by displaying an alert message and redirecting to the logout page.
 */
function logout(){
    alert('You have successfully logged out of the system.');
    window.location.href = '/logout';
}

/**
 * @Author - @DeanLogan
 * @Description - Checks the user's selected theme and applies it to the page's body element.
 * Removes non-default themes to ensure only one theme is applied at a time.
 */
function checkTheme() {
    var theme = localStorage.getItem('theme'); // Get the user's selected theme from local storage
    let element = document.body; // Get the body element of the page

    // Remove non-default themes to ensure only one theme is applied at a time
    element.classList.remove('light-mode');
    element.classList.remove('high-contrast-mode');

    // Check the selected theme and apply it to the page's body element
    if (theme == 'light-mode') {
        element.classList.add('light-mode'); // Apply the light mode theme
    } else if (theme == 'high-contrast-mode') {
        element.classList.add('high-contrast-mode'); // Apply the high contrast mode theme
    }
}

/**
 * @Author - @RossMcAlliste + @DeanLogan
 * @Description - Checks the user's selected font size and applies it to the page's body element.
 * Adjusts the font size of the body element based on user preference.
 */
function checkFontSize() {
    var fontSize = localStorage.getItem('fontSize'); // Get the user's selected font size from local storage
    var element = document.getElementById('column2'); // Get the column 2 element of the page

    // Check the selected font size and apply it to the page's body element
    if (fontSize == 'small') {
        element.style.fontSize = '1.5vh'; // Apply the small font size
    } else if (fontSize == 'large') {
        element.style.fontSize = '3vh'; // Apply the large font size
    } else {
        element.style.fontSize = '2vh'; // Apply the default (medium) font size
    }
}


/**
 * @Author - @DeanLogan
 * @Description - Toggles the side bar (nav) open or closed, and updates its state in session storage.
 * Adjusts UI elements by calling resizeNav.
 */
function navToggle() {
    var navOpen = sessionStorage.getItem('navOpen'); // Get the current state of the navigation sidebar from session storage
    // Close the navigation sidebar if it's currently open
    if (navOpen == 'true') {
        sessionStorage.setItem('navOpen', 'false'); // Update the navigation state to closed
    }
    // Open the navigation sidebar if it's currently closed
    else if (navOpen == 'false') {
        sessionStorage.setItem('navOpen', 'true'); // Update the navigation state to open
    }

    // Resize the navigation and content elements based on the updated navigation state
    resizeNav(); // Resize the navigation sidebar
}


/**
 * @author - @RossMcAllister
 * @Description - Resizes the navigation sidebar based on its state (open or closed) and window width.
 * Adjusts the width and height of the sidebar and resizes the close button accordingly.
 */
function resizeNav() {
    var column1Ele = document.getElementById('column1');
    var column2Ele = document.getElementById('column2');

    //if column has closed class, then remove it and open nav
    if (column1Ele.classList.contains('col-1-closed')) {
        column1Ele.classList.add('col-1');
        column1Ele.classList.remove('col-1-closed');

        column2Ele.classList.add('col-2');
        column2Ele.classList.remove('col-2-closed');
    }
    else if (column1Ele.classList.contains('col-1')) { //or if it has regular class, remove ut and close nav
        column1Ele.classList.add('col-1-closed');
        column1Ele.classList.remove('col-1');

        column2Ele.classList.add('col-2-closed');
        column2Ele.classList.remove('col-2');
    }
    else {
        //error, column 1 does not have either of the correct classes.
        console.log("Error: Resize navigation bar not working. Column 1 does not contain either of the correct classes.");
    }
}

/**
 * @Author - @DeanLogan
 * @Description - Holds event listeners that are applied to every web page.
 */
function listeners() {    
    // Menu animation code
    const menu = document.getElementById('menu');
    Array.from(document.getElementsByClassName('menu-item')).forEach((item, index) => {
        // When hovering over a menu item, set the active index for CSS animation
        item.onmouseover = () => {
            menu.dataset.activeIndex = index;
        }
    });

    /* Login and signup */
    // When the user clicks anywhere outside of the modal (pop-up), close it
    window.onclick = function(event) {
        if (event.target == document.getElementById('id01')) {
            document.getElementById('id01').style.display = "none";
        }
        else if (event.target == document.getElementById('id02')) {
            document.getElementById('id02').style.display = "none";
        }
        else if(event.target == document.getElementById('id03')) {
            document.getElementById('id03').style.display = "none";
        }
    }
}

/**
 * @Author - @DeanLogan
 * @Description - Displays the sign-up pop-up, adds pathway options to radio buttons.
 */
function displaySignUpPage() {
    var pathwayList = pathwayData;
    var htmlFormat = '';
    for (var i = 0; i < pathwayList.length; i++) {
        var checked = (i == 0) ? 'checked="true"' : ''; // Mark the first pathway as checked
        var pathwayNames = pathwayList[i].name;
        var pathwaysHtmlClassFormat = pathwayNames.replace(/\s/g, '');
        htmlFormat += `
            <label for="${pathwaysHtmlClassFormat}">
                <input type="radio" ${checked} id="${pathwaysHtmlClassFormat}" name="pathway" onchange="updateStageOptions()" value="${pathwayNames}" /> 
                ${pathwayNames}
            </label><br />
        `;
    }
    document.getElementsByClassName('Pathway')[0].innerHTML = htmlFormat;
    document.getElementById('id02').style.display = 'block';
    updateStageOptions(); // Update stages based on selected module
}

/**
 * @Author - @DeanLogan
 * @Description - Updates stage options depending on the selected module's stages.
 */
function updateStageOptions() {
    document.getElementsByClassName('stage-4')[0].style.display = 'none';
    var selectedPathway = document.querySelector('input[name="pathway"]:checked').value;
    
    // Check if selected module has 4 stages and show the corresponding stage option
    for (var i = 0; i < pathwayData.length; i++) {
        var pathwayName = pathwayData[i].name;
        if (selectedPathway == pathwayName && pathwayData[i].stages == 4) {
            document.getElementsByClassName('stage-4')[0].style.display = '';
        }
    }
}


/**
 * @Author - @DeanLogan
 * @Description - Displays the next part for sign-up. Sends a GET request with user-entered information from sign-up-1.
 * If the request is successful, displays sign-up-2; otherwise, shows an alert.
 */
function goToSignUp() {
    // Hide sign-up-1 and show sign-up-2
    document.getElementById('sign-up-1').style.display = 'none';
    document.getElementById('sign-up-2').style.display = 'block';

    // Gather user-entered information
    var studentNumber = document.querySelector('input[name="student-number-sign-up"]').value;
    var name = document.querySelector('input[name="name"]').value;
    var email = document.querySelector('input[name="email"]').value;
    var selectedPathway = document.querySelector('input[name="pathway"]:checked').value;
    var currentStage = document.querySelector('input[name="stage"]:checked').value;
    var currentSemester = document.querySelector('input[name="semester"]:checked').value;

    // Create an object with sign-up information
    var signUpInfo = {
        'studentNumber': studentNumber,
        'name': name,
        'email': email,
        'selectedPathway': selectedPathway,
        'currentStage': currentStage,
        'currentSemester': currentSemester
    };

    // Send a GET request to the server to process sign-up information
    $.get('/signUp/', signUpInfo, function (data) {
        if (data.success == 'true') {
            // If sign-up is successful, show sign-up-2
            document.getElementById('sign-up-1').style.display = 'none';
            document.getElementById('sign-up-2').style.display = 'block';
        } else {
            // If sign-up fails, display an alert
            alert('Sign up failed, try again.');
        }
    });
}

// Run the pageLoad function when the window is fully loaded
window.onload = pageLoad();