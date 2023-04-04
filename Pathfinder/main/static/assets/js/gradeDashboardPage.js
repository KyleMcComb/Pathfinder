window.onload = gradeDashboardPageLoad();

function gradeDashboardPageLoad() {
    resizeGradeDashboardPage();
    createGradeBarChart();
    initMultiselect();
} 

function resizeGradeDashboardPage(){
    var bottomBarDiv = document.getElementsByClassName('bottom-bar')[0];
    var windowWidth = window.innerWidth;

    document.getElementsByClassName('content')[0].style.height = (window.innerHeight - 85) + 'px';
    // NAV IS OPEN
    if(sessionStorage.getItem('navOpen') == 'true'){
        bottomBarDiv.style.width = (windowWidth-250)+'px';
        bottomBarDiv.style.left = '250px';
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem('navOpen') == 'false'){
        bottomBarDiv.style.width = (windowWidth-55)+'px';
        bottomBarDiv.style.left = '55px';
    }
}

function navToggleOnGradeDashboardPage(){
    navToggle();
    resizeGradeDashboardPage();
}

//grade bar chart
function createGradeBarChart(modules=['Module 1', 'Module 2', 'Module 3', 'Module 4', 'Module 5', 'Module 6'], grades=[55, 49, 44, 24, 15, 22]) {
    var theme = localStorage.getItem('theme');
    var barColours = '#27AE60'; // defaults to dark-mode
    var axisAndGridColour = '#FFFFFF'; 
    if(theme == 'high-contrast-mode'){
        barColours = '#000000';
        axisAndGridColour = '#000000'; 
    }
    else if(theme == 'light-mode'){
        barColours = '#b92261';
        axisAndGridColour = '#000000'; 
    }
    
    Chart.defaults.color = axisAndGridColour;

    new Chart('stageGrades', {  
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


//filter code
function initMultiselect() {
    checkboxStatusChange();

    document.addEventListener('click', function(evt) {
        var flyoutElement = document.getElementById('myMultiselect'),
        targetElement = evt.target; // clicked element

        do {
            if (targetElement == flyoutElement) {
                // This is a click inside. Do nothing, just return.
                //console.log('click inside');
                return;
            }

            // Go up the DOM
            targetElement = targetElement.parentNode;
        } while (targetElement);

        // This is a click outside.
        toggleCheckboxArea(true);
        console.log('click outside');
    });
}


function checkboxStatusChange() {
    var multiselect = document.getElementById('mySelectLabel');
    var multiselectOption = multiselect.getElementsByTagName('option')[0];

    var values = [];
    var checkboxes = document.getElementById('mySelectOptions');
    var checkedCheckboxes = checkboxes.querySelectorAll('input[type=checkbox]:checked');

    for (const item of checkedCheckboxes) {
        var checkboxValue = item.getAttribute('value');
        values.push(checkboxValue);
    }

    var dropdownValue = 'Select Stage to Display';
    if (values.length > 0) {
        dropdownValue = values.join(', ');
    }

    multiselectOption.innerText = dropdownValue;
}

function toggleCheckboxArea(onlyHide = false) {
    var checkboxes = document.getElementById('mySelectOptions');
    var displayValue = checkboxes.style.display;

    if (displayValue != 'block') {
        if (onlyHide == false) {
        checkboxes.style.display = 'block';
        }
    } else {
        checkboxes.style.display = 'none';
    }
}

window.addEventListener('resize', function(){resizeGradeDashboardPage()});