//window.onload = addModuleToPage("Module written using JS","code","lecture","stage","semester","weightin","req","1,2,3,4,5,","assesments","this is a description test");
window.onload = getModuleInfo();

function getModuleInfo(){
    $.get("/getModuleInfo/", function(data){
        for (var i=0; i<data.moduleList.length; i++){
            var module = data.moduleList[i];
            assesments = module.assesments.split(',');
            addModuleToPage(module.name, module.code, module.lecturer, module.stage, module.semester, module.weighting, 'true', module.pathways, assesments ,module.description);
        }
    });
}

function addModuleToPage(name, code, lecturer, stage, semester, weighting, required, pathways, assesments, description){
    pathwaysClasses = '';
    arrayOfPathways = pathways.split(',');
    for(var i=0; i<arrayOfPathways.length; i++){
        pathwaysClasses += arrayOfPathways[i].replace(/\s/g,'');
        pathwaysClasses += ' ';
    }
    htmlFormat = `
    <div class="module-table stage-${stage} semester-${semester} ${name.replace(/\s/g,'').toLowerCase()} ${pathwaysClasses}">
        <div class="top-of-table">
            <p><b class="heading">Module Name: </b><span> ${name} (${code})</span></p>
        </div>
        <div class="main-module-info">
            <div>
                <p><b class="heading">Lecturer(s):</b><span> ${lecturer}</span></p>
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
            <p><b class="heading">Pathways available on: </b><span> ${pathways}</span></p>
        </div>
    `;

    for(var i=0; i<assesments.length; i++){
        htmlFormat += `
            <div>
                <b class="heading">Assesment: </b><span> ${assesments[i]}</span></p>
            </div>
        `;
    }

    htmlFormat += `
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

document.getElementById('searchbutton').addEventListener("click", function(evt){
    search();
});

document.getElementById('search-input').addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        search();
    }
});

function search(){
    var values = [];
    var searchTerm = document.querySelector('input[name="search"]').value;
    var checkedCheckboxes = document.getElementById("mySelectOptions").querySelectorAll('input[type=checkbox]:checked');

    values.push(searchTerm.replace(/\s/g,'').toLowerCase());
    for (const item of checkedCheckboxes) {
        var checkboxValue = item.getAttribute('value');
        values.push(checkboxValue);
    }
    if(searchTerm == ""){
        showAllItemsWithClassNames(['module-table']);
    }
    else{
        hideAllItemsWithClassNames(['module-table']);
        if(values.length > 0){
            showAllItemsWithClassNames(values);
        }
    }
}

function formatClassNames(nameArray){
    var names = '';
    for(var i=0; i<nameArray.length; i++){
        names += '.';
        names += nameArray[i].replace(/\s/g,'');
    }
    return names
}

function hideAllItemsWithClassNames(nameArray){
    var names = formatClassNames(nameArray);
    document.querySelectorAll(names).forEach(item => {
        item.style.display = 'none';
    });
}

function showAllItemsWithClassNames(nameArray){
    var names = formatClassNames(nameArray);
    document.querySelectorAll(names).forEach(item => {
        item.style.display = 'grid';
    });
}

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

    hideAllItemsWithClassNames(['module-table']);
    var dropdownValue = "No filters are applied";
    if (values.length > 0) {
        dropdownValue = values.join(', ');
        showAllItemsWithClassNames(values);
    }
    else{
        showAllItemsWithClassNames(['module-table']);
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