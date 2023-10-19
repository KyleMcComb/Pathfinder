window.onload = gradeDashboardPageLoad();

var chart = null; // initialises the global variable chart that's used to store the chart object

/**
 * @Author - @DeanLogan
 * @Description - Runs on load for the grade dashboard page. Initializes dropdown, bar chart, and progress bar.
 * Resizes the page to ensure UI elements fit the user's screen resolution.
 */
function gradeDashboardPageLoad() {
    resizeGradeDashboardPage();
    radioBtnStatusChange();
    listenersForGradeDashboardPage();
    progressBar('0');
    getGradeData();
}

/**
 * @Author - @DeanLogan
 * @Description - Updates the progress bar's width and displayed grade.
 * @param {string} [grade='0'] - The percentage value to set the progress bar width and display the grade.
 */
function progressBar(grade='0'){
    document.getElementById('current-progression').style.width = grade+'%';
    document.getElementById('grade').innerHTML = grade;
}

/**
 * @Author - @DeanLogan
 * @Description - Resizes the grade dashboard page's UI elements to fit the screen resolution.
 */
function resizeGradeDashboardPage() {
    try{
        var bottomBarDiv = document.getElementsByClassName('bottom-bar')[0];
        var windowWidth = window.innerWidth; // Get the current window width
        var windowHeight = window.innerHeight; // Get the current window height
        var progress = windowHeight * 0.078241; // Calculate the progress bar height
        var barchartWidth = (((windowWidth - 55) * 0.95) * 0.64); // Calculate the width of the bar chart
        var barchartHeight = (1130 / 2261.3) * barchartWidth; // Calculate the height of the bar chart
        document.getElementsByClassName('content')[0].style.height = (windowHeight - progress) + 'px'; // Set the content height
        document.getElementsByClassName('bottom-bar')[0].style.height = progress + 'px'; // Set the bottom bar height
        document.getElementsByClassName('stats')[0].style.height = barchartHeight + 'px'; // Set the bar chart height

        var navOpen = sessionStorage.getItem("navOpen");

        // NAV IS OPEN
        if (navOpen == "true") {
            // Check if the window width is smaller than 1117.1px
            if (windowWidth < 1117.1) {
                bottomBarDiv.style.width = (windowWidth - 145) + 'px'; // Set width for open sidebar
                bottomBarDiv.style.left = '145px'; // Set left position for open sidebar
            } else {
                bottomBarDiv.style.width = windowWidth - (windowWidth * 0.13) + 'px'; // Set responsive width for open sidebar
                bottomBarDiv.style.left = windowWidth * 0.13 + 'px'; // Set responsive left position for open sidebar
            }
        }
        // NAV IS NOT OPEN
        else if (navOpen == "false") {
            // Check if the window width is smaller than 1117.1px
            if (windowWidth < 1117.1) {
                bottomBarDiv.style.width = (windowWidth - 32) + 'px'; // Set width for closed sidebar
                bottomBarDiv.style.left = '32px'; // Set left position for closed sidebar
            } else {
                bottomBarDiv.style.width = windowWidth - (windowWidth * 0.0286) + 'px'; // Set responsive width for closed sidebar
                bottomBarDiv.style.left = windowWidth * 0.0286 + 'px'; // Set responsive left position for closed sidebar
            }
        }
    }
    catch (error) {
        // Handle any errors that might occur
        console.log("An error occurred: " + error.message);
    }
}


/**
 * @Author - @DeanLogan
 * @Description - Toggles the navigation sidebar open or closed and resizes the grade dashboard page accordingly.
 */
function navToggleOnGradeDashboardPage() {
    navToggle(); // Toggle the navigation sidebar
    resizeGradeDashboardPage(); // Resize the grade dashboard page UI elements
}


/**
 * @Author - @DeanLogan
 * @Description - Retrieves grade information for the student from the server using an AJAX GET request.
 * Updates progress bar, module averages, assessment averages, and the left-to-earn percentage.
 * Populates the stage selection dropdown with radio buttons corresponding to the student's stages.
 * Displays grade data for the 1st semester on page load.
 */
function getGradeData() {
    $.get("/gradeInfo/", function(data) {
        if(data.error == 'True'){
            document.getElementsByClassName('content')[0].innerHTML = '<h1>There was an error retrieving your grade data. Please try again later.<br /><br />It is possible that you are either not signed in, or you are signed in but do not have any modules connected to your account, please contact the admin to help solve this issue.</h1>';
            document.getElementsByClassName('bottom-bar')[0].style.display = 'none';
        }
        else {
            progressBar(data.currentPathwayMark); // Update progress bar
            document.getElementById('modAvg').innerHTML = data.moduleAvg + '%'; // Display module average
            document.getElementById('asAvg').innerHTML = data.assesmentAvg + '%'; // Display assessment average
            document.getElementById('leftToEarn').innerHTML = data.leftToEarn + '%'; // Display left-to-earn percentage

            var stages = data.stages;
            for (var i = 0; i < stages.length; i++) {
                stageNum = i + 1;
                var defaultChecked = 0;
                if (i == 0) {
                    defaultChecked = 'checked="true"';
                }
                // Add radio buttons to the stage selection dropdown for each of the student's stages
                document.getElementById('mySelectOptions').innerHTML += `
                    <label for="stage">&nbsp;&nbsp;<input name="stageSelect" type="radio" id="stage-${stageNum}" onchange="radioBtnStatusChange()" value="${stageNum}" ${defaultChecked}/>${stageNum}</label>
                `;
            }
            displayStage(1); // Display data for the 1st semester on page load
        }
    });
}


/**
 * @Author - @DeanLogan
 * @Description - Retrieves and displays grade data for a specific stage using an AJAX GET request.
 * Populates the UI with module names, assessment names, and grades for the selected stage.
 * Destroys the previous chart and creates a new bar chart for the selected semester's grades.
 * @param {number} stageSelected - The stage number for which the grade data should be displayed.
 */
function displayStage(stageSelected) {
    $.get("/gradeInfo/", function(data) {
        var modules = [];
        var grades = [];
        var stages = data.stages;

        // Retrieve module names and grades from the JSON object and push them to corresponding arrays
        for (var j = 0; j < stages[stageSelected - 1].length; j++) {
            modules.push(stages[stageSelected - 1][j].name);
            grades.push(stages[stageSelected - 1][j].mark);
        }

        document.getElementsByClassName('assesments')[0].innerHTML = ''; // Clear existing elements from the assessments div
        var stage = stages[stageSelected - 1];
        var htmlFormat = '';

        // Extract module names, assessment names, and grades from the JSON object and format them for display
        for (var i = 0; i < stage.length; i++) {
            htmlFormat += `
                <h3>${stage[i].name}</h3>
            `;
            assessments = stage[i].assessments;
            for (var j = 0; j < assessments.length; j++) {
                htmlFormat += `
                    <p>&nbsp;&nbsp;${assessments[j].name}: ${assessments[j].mark}%</p>
                `;
            }
        }

        document.getElementsByClassName('assesments')[0].innerHTML = htmlFormat;

        // Destroy the previous chart that was being displayed on the page
        if (chart != null) {
            chart.destroy();
        }

        createGradeBarChart(modules, grades); // Create a new chart with data for the selected semester
    });
}


/**
 * @Author - @DeanLogan
 * @Description - Creates a bar chart to display module grades for a specific stage.
 * The chart's appearance and colors are determined based on the current theme.
 * @param {Array} [modules=['Module 1', 'Module 2', 'Module 3', 'Module 4', 'Module 5', 'Module 6']]
 *        - An array of module names to be shown on the x-axis.
 * @param {Array} [grades=[55, 49, 44, 24, 15, 22]]
 *        - An array of grade values to be shown on the y-axis.
 */
function createGradeBarChart(modules=['Module 1', 'Module 2', 'Module 3', 'Module 4', 'Module 5', 'Module 6'], grades=[55, 49, 44, 24, 15, 22]) {
    // Check the current theme to determine bar chart colors
    var theme = localStorage.getItem('theme');
    var barColours = '#27AE60'; // Defaults to dark-mode
    var axisAndGridColour = '#FFFFFF'; 
    if (theme == 'high-contrast-mode') {
        barColours = '#000000';
        axisAndGridColour = '#000000'; 
    } else if (theme == 'light-mode') {
        barColours = '#b92261';
        axisAndGridColour = '#000000'; 
    }
    
    Chart.defaults.color = axisAndGridColour;

    chart = new Chart('stageGrades', {  
        type: 'bar',
        data: {
            labels: modules,
            datasets: [{
                backgroundColor: barColours,
                data: grades,
                label: 'Grade'
            }],
            hoverOffset: 4
        },
        options: {
            legend: {display: false},
            title: {
                display: true,
                text: 'Grades for each module during this stage'
            },
            scales: {
                y: {
                    max: 100,
                    min: 0,
                    grid: {
                        color: axisAndGridColour,
                    }
                },
            }
        }
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Sets up event listeners for the grade dashboard page.
 * Listens for clicks to close the dropdown and for window resizing to adjust UI elements.
 */
function listenersForGradeDashboardPage() {
    // Listen for click events to close the dropdown when clicked outside
    document.addEventListener('click', function(evt) {
        var flyoutElement = document.getElementById('myMultiselect'),
            targetElement = evt.target; // Clicked element

        do {
            if (targetElement == flyoutElement) {
                // Clicked inside the dropdown. Do nothing, just return.
                return;
            }

            // Move up the DOM
            targetElement = targetElement.parentNode;
        } while (targetElement);

        // Clicked outside the dropdown
        toggleRadioBtnArea(true);
    });

    // Listen for window resize events to adjust UI elements
    window.addEventListener('resize', function(){resizeGradeDashboardPage()});
}


/**
 * @Author - @DeanLogan
 * @Description - Updates the displayed dropdown option based on the selected stage.
 * Calls the displayStage function to update stage-related information.
 */
function radioBtnStatusChange() {
    var multiselect = document.getElementById('mySelectLabel');
    var multiselectOption = multiselect.getElementsByTagName('option')[0];

    var display = 'stage 1'; 
    var stageSelected = document.querySelector('input[name="stageSelect"]:checked');
    if (stageSelected != null) {
        display = 'stage ' + stageSelected.value;
        displayStage(stageSelected.value); // Update stage-related information
    }

    multiselectOption.innerText = display; // Update the displayed dropdown option
}

/**
 * @Author - @DeanLogan
 * @Description - Toggles the visibility state of the radio button options area.
 * If onlyHide is set to true, the options area is only hidden.
 * @param {boolean} [onlyHide=false] - Indicates whether to only hide the options area.
 */
function toggleRadioBtnArea(onlyHide = false) {
    try {
        var radioBtns = document.getElementById('mySelectOptions');
        var displayValue = radioBtns.style.display;

        if (displayValue != 'block') {
            if (!onlyHide) {
                radioBtns.style.display = 'block'; // Show the options area
            }
        } else {
            radioBtns.style.display = 'none'; // Hide the options area
        }
    } 
    catch (error) {
        // Handle any errors that might occur
        console.log("An error occurred: " + error.message);
    }
}

