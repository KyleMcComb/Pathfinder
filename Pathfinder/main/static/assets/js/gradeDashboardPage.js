window.onload() = resizeChatbotPage();

function resizeGradeDashboardPage(){
    var bottomBarDiv = document.getElementsByClassName('bottom-bar')[0];
    var windowWidth = window.innerWidth;

    document.getElementsByClassName('content')[0].style.height = (window.innerHeight - 85) + "px";
    console.log(document.getElementsByClassName('content')[0].style.height);
    // NAV IS OPEN
    if(sessionStorage.getItem("navOpen") == "true"){
        bottomBarDiv.style.width = (windowWidth-250)+"px";
        bottomBarDiv.style.left = "250px";
    }
    // NAV IS NOT OPEN
    else if(sessionStorage.getItem("navOpen") == "false"){
        bottomBarDiv.style.width = (windowWidth-55)+"px";
        bottomBarDiv.style.left = "55px";
    }
}

function navToggleOnGradeDashboardPage(){
    navToggle();
    resizeGradeDashboardPage();
}

//filter code
window.onload = initMultiselect();


function initMultiselect() {
    checkboxStatusChange();

    document.addEventListener("click", function(evt) {
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
    var multiselect = document.getElementById("mySelectLabel");
    var multiselectOption = multiselect.getElementsByTagName('option')[0];

    var values = [];
    var checkboxes = document.getElementById("mySelectOptions");
    var checkedCheckboxes = checkboxes.querySelectorAll('input[type=checkbox]:checked');

    for (const item of checkedCheckboxes) {
        var checkboxValue = item.getAttribute('value');
        values.push(checkboxValue);
    }

    var dropdownValue = "No filters are applied";
    if (values.length > 0) {
        dropdownValue = values.join(', ');
    }

    multiselectOption.innerText = dropdownValue;
}

function toggleCheckboxArea(onlyHide = false) {
    var checkboxes = document.getElementById("mySelectOptions");
    var displayValue = checkboxes.style.display;

    if (displayValue != "block") {
        if (onlyHide == false) {
        checkboxes.style.display = "block";
        }
    } else {
        checkboxes.style.display = "none";
    }
}