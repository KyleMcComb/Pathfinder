window.onload = gradeDashboardPageLoad();

var chart = null;

function gradeDashboardPageLoad() {
    resizeGradeDashboardPage();
    initMultiselect();
    progressBar('50');
    getGradeData();
} 

function progressBar(grade='0'){
    document.getElementById('current-progression').style.width = grade+'%';
    document.getElementById('grade').innerHTML = grade;
}

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

    

    console.log(document.getElementsByClassName('filter-container')[0].style.height);
    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        //bottomBarDiv.style.width = (windowWidth-250)+"px";
        bottomBarDiv.style.width = windowWidth-(windowWidth*0.13)+"px";
        //bottomBarDiv.style.left = "250px";
        bottomBarDiv.style.left = windowWidth*0.13+"px";
        //textarea.style.width = (windowWidth-370)+"px";
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        // bottomBarDiv.style.width = (windowWidth-55)+"px";
        // bottomBarDiv.style.left = "55px";
        // textarea.style.width = (windowWidth-175)+"px";
        bottomBarDiv.style.width = windowWidth-(windowWidth*0.0286)+"px";
        bottomBarDiv.style.left = windowWidth*0.0286+"px";
    }
}

function navToggleOnGradeDashboardPage(){
    navToggle();
    resizeGradeDashboardPage();
}

function getGradeData(){
    $.get("/gradeInfo/", function(data){
        console.log(data);
        progressBar(data.currentPathwayMark);
        document.getElementById('modAvg').innerHTML = data.moduleAvg + '%'
        document.getElementById('asAvg').innerHTML = data.assesmentAvg + '%'
        document.getElementById('leftToEarn').innerHTML = data.leftToEarn + '%'

        var stages = data.stages;
        for(var i=0; i<stages.length; i++){
            var defaultChecked = 0;
            if(i==0){
                defaultChecked = 'checked="true"';
            }
            document.getElementById('mySelectOptions').innerHTML = `
                <label for="stage">&nbsp;&nbsp;<input name="stageSelect" type="radio" id="stage-${i+1}" onchange="checkboxStatusChange()" value="stage-${i+1}" ${defaultChecked}/>1</label>
            `;
        }
        displayStage(1);
    });
}

function displayStage(stageSelected){
    $.get("/gradeInfo/", function(data){
        var modules = [];
        var grades = [];
        var stages = data.stages;
        for(var i=0; i<stages.length; i++){
            for(var j=0; j<stages[i].length; j++){
                modules.push(stages[i][j].name);
                grades.push(stages[i][j].studentMark);
            }
        }

        document.getElementsByClassName('assesments')[0].innerHTML = '';
        var stage = stages[stageSelected-1];
        var htmlFormat = '';
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

        if(chart != null){
            chart.destroy();
        }
        createGradeBarChart(modules, grades);
    });
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