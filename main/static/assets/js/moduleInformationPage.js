window.onload = pageLoad();

/* 
    @Author: @DeanLogan123
    @Description: This function runs on load for the grade dashboard page, it initialises the dropdown, gets all the pathways within the database for the filter and gets the information for all modules to display to the user.
*/
function pageLoad(){
    getPathwayList();
    getModuleInfo('');
    checkboxStatusChange();
    listenersForModuleInfoPage();
}

/* 
    @Author: @DeanLogan123
    @Description: Sends a GET request with the search term entered by the user which will then return a JSON object with all the module information for the modules that meet that search term. Then displayes these to the user.
*/
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

/* 
    @Author: @DeanLogan123
    @Description: Gets all pathways within the database then adds these to the filter dropdown.
*/
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

/* 
    @Author: @DeanLogan123
    @Description: Displays the information for a given module to the user.
    @param: name - string containing the name of the module
    @param: code - string containing the code for the module
    @param: lecturer - string containing the names of the lecturers for the module
    @param: stage - string containing the stage the module is available in
    @param: semester - string containing the semester the module is available in
    @param: weighting - string containing the weighting for the module (also known as CAT points)
    @param: pathways - string containing the pathways the module is available in
    @param: assesments - array containing the name of the assesments and their weighting that are on the module
    @param: description - string containing the description for the module
*/
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
    
    // adds each of the details for the assesment to the htmlFormat string
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

/* 
    @Author: @DeanLogan123
    @Description: Holds all the event listeners for this page. 
*/
function listenersForModuleInfoPage(){
    // checks to see if the user has pressed the search button, then searches if this is the case
    document.getElementById('searchbutton').addEventListener("click", function(evt){
        search();
    });
    
    // checks to see if the user has pressed the enter key within the search bar, then searches if this is the case
    document.getElementById('search-input').addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            search();
        }
    });

    // checks to see if the user has clicked inside or outside of the dropdown, then changes the state of the dropdown depending on which the user clicked
    document.addEventListener("click", function(evt) {
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
        toggleCheckboxArea(true);
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Gets the text entered into the search bar then searches for matches within the database, then once the result is returned any filters selected are applied. 
*/
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

/* 
    @Author: @DeanLogan123
    @Description: Formats the "properties" of modules (the options within the filter) into class names for html. This is so when a filter is applied then all the class names that match the filter can be hidden from the user.
    @param: nameArray - array of strings that contain the names that need to be formatted into an html class name
    @return: names - arrray of strings that contain the names formatted into format suitable for an html class name  
*/
function formatClassNames(nameArray){
    var names = '';
    for(var i=0; i<nameArray.length; i++){
        names += '.';
        names += nameArray[i].replace(/\s/g,'');
    }
    return names
}

/* 
    @Author: @DeanLogan123
    @Description: Formats the nameArray into html class names, then "hides" all of the divs with these class names from the user. 
    @param: nameArray - array of strings that contain the names that need to be "hidden" from the user
*/
function hideAllItemsWithClassNames(nameArray){
    var names = formatClassNames(nameArray);
    document.querySelectorAll(names).forEach(item => {
        item.style.display = 'none';
    });
}

/* 
    @Author: @DeanLogan123
    @Description: Formats the nameArray into html class names, then "displays" all of the divs with these class names from the user. 
    @param: nameArray - array of strings that contain the names that need to be "displayed" from the user
*/
function showAllItemsWithClassNames(nameArray){
    var names = formatClassNames(nameArray);
    document.querySelectorAll(names).forEach(item => {
        item.style.display = 'grid';
    });
}


/* 
    @Author: @DeanLogan123
    @Description: Updates the information on the page based on the selection of the user within the dropdown. 
*/
function checkboxStatusChange() {
    var multiselect = document.getElementById("mySelectLabel");
    var multiselectOption = multiselect.getElementsByTagName('option')[0];

    var values = [];
    var checkboxes = document.getElementById("mySelectOptions");
    var checkedCheckboxes = checkboxes.querySelectorAll('input[type=checkbox]:checked'); // gets all filters that are ticked

    for (const item of checkedCheckboxes) {
        var checkboxValue = item.getAttribute('value');
        values.push(checkboxValue);
    }

    // hides all the modules, then starts to show each of the modules that meet the conditions set by the filter
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

    multiselectOption.innerText = dropdownValue; // updates the text shown to the user to tell them what filters have been applied
}

/* 
    @Author: @DeanLogan123
    @Description: Toggles the state of the dropdown (open or closed).
*/
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