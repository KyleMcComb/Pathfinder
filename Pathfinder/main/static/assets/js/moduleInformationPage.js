window.onload = pageLoad();

function pageLoad(){
    getPathwayList();
    getModuleInfo('');
    checkboxStatusChange();
    listners();
}

function signUp(){
    $.get("/signUp/");
}

function getModuleInfo(searchTerm){
    document.getElementsByClassName('modules-container')[0].innerHTML = '';
    // if searchTerm is an empty string the get request below will return all of the modules
    $.get("/searchModules/", { moduleName: searchTerm }, function(data){
        for (var i=0; i<data.moduleList.length; i++){
            var module = data.moduleList[i];
            assesments = module.assesments.split(',');
            addModuleToPage(module.name, module.code, module.lecturer, module.stage, module.semester, module.weighting, module.pathways, assesments ,module.description);
        }
    });
}

function getPathwayList(){
    $.get("/listOfPathways/", function(data){
        var pathwayList = data.pathwayList;
        var htmlFormat = '';
        for(var i=0; i<pathwayList.length; i++){
            var pathwayNames = pathwayList[i].name;
            var pathwaysHtmlClassFormat = pathwayNames.replace(/\s/g,'');
            htmlFormat += `
                <label for="${pathwaysHtmlClassFormat}">&nbsp;&nbsp;<input type="checkbox" id="${pathwaysHtmlClassFormat}" onchange="checkboxStatusChange()" value="${pathwaysHtmlClassFormat}" /> ${pathwayNames}</label>
            `;
        }
        document.getElementsByClassName('pathways')[0].innerHTML = htmlFormat;
    });
}

function addModuleToPage(name, code, lecturer, stage, semester, weighting, pathways, assesments, description){
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


function listners(){
    document.getElementById('searchbutton').addEventListener("click", function(evt){
        search();
    });
    
    document.getElementById('search-input').addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            search();
        }
    });

    //init multiselet checboxes
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
    });
}

function search(){
    var values = [];
    var searchTerm = document.querySelector('input[name="search"]').value;
    var checkedCheckboxes = document.getElementById("mySelectOptions").querySelectorAll('input[type=checkbox]:checked');

    for (const item of checkedCheckboxes) {
        var checkboxValue = item.getAttribute('value');
        values.push(checkboxValue);
    }
    getModuleInfo(searchTerm);
    if(values.length != 0){
        // waits 30ms for response from the get request and for the html page to update
        setTimeout( function(){
            hideAllItemsWithClassNames(['module-table']);
            showAllItemsWithClassNames(values);
        },100);
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
    console.log(values);
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