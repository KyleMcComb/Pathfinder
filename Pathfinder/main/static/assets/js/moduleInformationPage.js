window.onload = addModuleToPage("Module written using JS","code","lecture","stage","semester","weightin","req","1,2,3,4,5,","assesments","this is a description test");

function addModuleToPage(name, code, lecturer, stage, semester, weighting, required, pathways, assesments, description){
    htmlFormat = `
    <div class="module-table">
        <div class="top-of-table">
            <p><b class="heading">Module Name: </b><span> ${name} (${code})</span></p>
        </div>
        <div class="main-module-info">
            <div>
                <p><b class="heading">Lecturer</b><span> ${lecturer}</span></p>
            </div>
            <div>
                <p><b class="heading">Stage: </b><span> ${stage}</span></p>
            </div>
            <div>
                <p><b class="heading">Semester: </b><span> ${semester}</span></p>
            </div>
            <div>
                <p><b class="heading">Weighting: </b><span> ${weighting}</span></p>
            </div>
            <div>
                <p><b class="heading">Required: </b><span> ${required}</span></p>
            </div>
        </div>
        <div>
            <b class="heading">Pathways available on: </b><br />
            <p>${pathways}</p>
        </div>
        <div>
            <b class="heading">Assesment name: </b>
        </div>
        <div>
            <b class="heading">Description: </b><br />
            <p>${description}</p>
        </div>
    </div>
    `;

    document.getElementsByClassName('modules-container')[0].innerHTML += htmlFormat;

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