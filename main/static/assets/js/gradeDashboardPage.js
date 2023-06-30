window.onload = gradeDashboardPageLoad();

var chart = null; // initialises the global variable chart that's used to store the chart object

/* 
    @Author: @DeanLogan123
    @Description: This function runs on load for the grade dashboard page, it initialises the dropdown, creates the bar chart and progress bar. It then resizes the grade dashboard page to ensure that all UI elements fit for the users screen resolution.  
*/
function gradeDashboardPageLoad() {
    resizeGradeDashboardPage();
    radioBtnStatusChange();
    listenersForGradeDashboardPage();
    progressBar('0');
    getGradeData();
}

/* 
    @Author: @DeanLogan123
    @Description: Makes the width of the progress bar the same as the users grade.
    @param: grade - value between 0-100 that is used to represent the grade for the students overall degree percentage.
*/
function progressBar(grade='0'){
    document.getElementById('current-progression').style.width = grade+'%';
    document.getElementById('grade').innerHTML = grade;
}

/* 
    @Author: @DeanLogan123
    @Description: This will resize the bottom bar div and the textarea widget to ensure they match for all screen resolutions, it will also check if the sidebar (nav) is open to ensure no UI elements overlap.
*/
function resizeGradeDashboardPage(){
    var bottomBarDiv = document.getElementsByClassName('bottom-bar')[0];
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;
    var progress = windowHeight * 0.078241;
    var barchartWidth = (((windowWidth - 55) * 0.95) * 0.64);
    var barchartHeight = (1130/2261.3) * barchartWidth;
    document.getElementsByClassName('content')[0].style.height = (windowHeight - progress) + 'px';
    document.getElementsByClassName('bottom-bar')[0].style.height =  progress + 'px';
    document.getElementsByClassName('stats')[0].style.height = barchartHeight+'px';

    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            bottomBarDiv.style.width = (windowWidth-145)+'px';
            bottomBarDiv.style.left = '145px';
        }
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        else{
            bottomBarDiv.style.width = windowWidth-(windowWidth*0.13)+'px';
            bottomBarDiv.style.left = windowWidth*0.13+'px';
        }
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        // this check is here because whenever the width of the browser is less than 1117.1px the sidebar becomes too small to use
        if(windowWidth < 1117.1){
            bottomBarDiv.style.width = (windowWidth-32)+'px';
            bottomBarDiv.style.left = '32px';
        }
        else{
            bottomBarDiv.style.width = windowWidth-(windowWidth*0.0286)+'px';
            bottomBarDiv.style.left = windowWidth*0.0286+'px';
        }
    }
}

/* 
    @Author: @DeanLogan123
    @Description: Toggles sidebar (nav) open and closed, different from default navToggle (seen in general.js) to ensure the bottom bar div and textarea are resized accordingly.
*/
function navToggleOnGradeDashboardPage(){
    navToggle();
    resizeGradeDashboardPage();
}

/* 
    @Author: @DeanLogan123
    @Description: Gets the stats for the student who is logged into the system, then adds this to the page. Also adds how many stages they have completed to the radio button.
*/
function getGradeData(){
    $.get("/gradeInfo/", function(data){
        progressBar(data.currentPathwayMark);
        document.getElementById('modAvg').innerHTML = data.moduleAvg + '%';
        document.getElementById('asAvg').innerHTML = data.assesmentAvg + '%';
        document.getElementById('leftToEarn').innerHTML = data.leftToEarn + '%';

        var stages = data.stages;
        for(var i=0; i<stages.length; i++){
            stageNum = i+1;
            var defaultChecked = 0;
            if(i==0){
                defaultChecked = 'checked="true"';
            }
            document.getElementById('mySelectOptions').innerHTML += `
                <label for="stage">&nbsp;&nbsp;<input name="stageSelect" type="radio" id="stage-${stageNum}" onchange="radioBtnStatusChange()" value="${stageNum}" ${defaultChecked}/>${stageNum}</label>
            `; // adds the radio buttons to the dropdown for each of the stages the student has done
        }
        displayStage(1); // displays the data for the 1st semester, this happens on page load
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Creates the barchart displaying the students grades for modules and also displays the assessment grades for the modules in a list.
    @param: stageSelected - int value between 1-4 that represents the stages grade info that will be displayed. 
*/
function displayStage(stageSelected){
    $.get("/gradeInfo/", function(data){
        var modules = [];
        var grades = [];
        var stages = data.stages;

        // gets the name and grade for each of the modules from the JSON object then pushes them to the corresponding list
        for(var j=0; j<stages[stageSelected-1].length; j++){
            modules.push(stages[stageSelected-1][j].name);
            grades.push(stages[stageSelected-1][j].studentMark);
        }
        
        document.getElementsByClassName('assesments')[0].innerHTML = ''; // clears all elements that were in the assesments div to ensure that it's empty before adding new information to it
        var stage = stages[stageSelected-1];
        var htmlFormat = '';
        // extracts module names, assessment names and grades from the JSON object then displays them accordingly
        for(var i=0; i<stage.length; i++){
            htmlFormat += `
                <h3>${stage[i].name}</h3>
            `;
            assessments = stage[i].assessments
            for(var j=0; j<assessments.length; j++){
                htmlFormat += `
                    <p>&nbsp;&nbsp;${assessments[j].name}: ${assessments[j].mark}%</p>
                `;
            }
        }
        
        document.getElementsByClassName('assesments')[0].innerHTML = htmlFormat;
        
        // destroys the previous chart that was being displayed on the page
        if(chart != null){
            chart.destroy();
        }
        createGradeBarChart(modules, grades); // creates new chart with data for the selected semester
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Creates bar chart using Chart.js to show the module grades for the selected semester.
    @param: modules - Array of modules to be shown on the x-axis
    @param: grades - Array of grades to be shown on the y-axis 
*/
function createGradeBarChart(modules=['Module 1', 'Module 2', 'Module 3', 'Module 4', 'Module 5', 'Module 6'], grades=[55, 49, 44, 24, 15, 22]) {
    // checks the current theme applied to ensure the colour of the bar chart matches with the theme
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

/* 
    @Author: @DeanLogan123
    @Description: Holds all the event listeners for this page. 
*/
function listenersForGradeDashboardPage() {

    document.addEventListener('click', function(evt) {
        var flyoutElement = document.getElementById('myMultiselect'),
        targetElement = evt.target; // clicked element

        do {
            if (targetElement == flyoutElement) {
                // This is a click inside. Do nothing, just return.
                return;
            }

            // Go up the DOM
            targetElement = targetElement.parentNode;
        } while (targetElement);

        // This is a click outside.
        toggleRadioBtnArea(true);
    });

    window.addEventListener('resize', function(){resizeGradeDashboardPage()});
}

/* 
    @Author: @DeanLogan123
    @Description: Updates the information on the page based on the selection of the user within the dropdown. 
*/
function radioBtnStatusChange() {
    var multiselect = document.getElementById('mySelectLabel');
    var multiselectOption = multiselect.getElementsByTagName('option')[0];

    var display = 'stage 1' 
    var stageSelected = document.querySelector('input[name="stageSelect"]:checked');
    if(stageSelected != null){
        display = 'stage '+stageSelected.value;
        displayStage(stageSelected.value);
    }

    multiselectOption.innerText = display; // updates the text shown to the user to tell them what stage has been selected
}

/* 
    @Author: @DeanLogan123
    @Description: Toggles the state of the dropdown (open or closed).
*/
function toggleRadioBtnArea(onlyHide = false) {
    var radioBtns = document.getElementById('mySelectOptions');
    var displayValue = radioBtns.style.display;

    if (displayValue != 'block') {
        if (onlyHide == false) {
        radioBtns.style.display = 'block';
        }
    } else {
        radioBtns.style.display = 'none';
    }
}

