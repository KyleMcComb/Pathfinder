window.onload = pageLoad();

/**
 * @Author - @DeanLogan
 * @Description - Initializes the page by fetching pathway list, module information, and setting up event listeners.
 */
function pageLoad() {
    getPathwayList(); // Fetches the list of pathways
    getModuleInfo(''); // Fetches module information with an empty filter initially
    checkboxStatusChange(); // Handles checkbox status change
    listenersForModuleInfoPage(); // Sets up event listeners for the module info page
}

/**
 * @Author - @DeanLogan
 * @Description - Fetches module information based on the provided search term and populates the modules container on the page.
 * @param {string} searchTerm - The term to search for modules. An empty string returns all modules.
 */
function getModuleInfo(searchTerm) {
    document.getElementsByClassName('modules-container')[0].innerHTML = ''; // Clear the modules container

    // If searchTerm is an empty string, the GET request below will return all modules
    $.get("/searchModules/", { moduleName: searchTerm }, function(data) {
        for (var i = 0; i < data.moduleList.length; i++) {
            var module = data.moduleList[i];
            assesments = module.assesments.split(','); // Split assessments into an array
            addModuleToPage(
                module.name,
                module.code,
                module.lecturer,
                module.stage,
                module.semester,
                module.weighting,
                module.pathways,
                assesments,
                module.description
            ); // Add module information to the page
        }
    });
}


/**
 * @Author - @DeanLogan
 * @Description - Fetches the list of pathways and populates the pathways section on the page with checkboxes.
 */
function getPathwayList() {
    $.get("/listOfPathways/", function(data) {
        var pathwayList = data.pathwayList;
        var htmlFormat = '';
        for (var i = 0; i < pathwayList.length; i++) {
            var pathwayNames = pathwayList[i].name;
            var pathwaysHtmlClassFormat = pathwayNames.replace(/\s/g, ''); // Remove spaces for HTML class format
            htmlFormat += `
                <label for="${pathwaysHtmlClassFormat}">
                    &nbsp;&nbsp;<input type="checkbox" id="${pathwaysHtmlClassFormat}" onchange="checkboxStatusChange()" value="${pathwaysHtmlClassFormat}" />
                    ${pathwayNames}
                </label>
            `;
        }
        document.getElementsByClassName('pathways')[0].innerHTML = htmlFormat; // Add checkboxes to the pathways section
    });
}


/**
 * @Author - @DeanLogan
 * @Description - Adds module information to the page by creating and appending HTML elements.
 * @param {string} name - The name of the module.
 * @param {string} code - The code of the module.
 * @param {string} lecturer - The lecturer(s) of the module.
 * @param {number} stage - The stage of the module.
 * @param {number} semester - The semester of the module.
 * @param {string} weighting - The weighting of the module.
 * @param {string} pathways - The pathways available for the module.
 * @param {Array} assessments - An array of assessment names for the module and the weighting of the assessments.
 * @param {string} description - The description of the module.
 */
function addModuleToPage(name, code, lecturer, stage, semester, weighting, pathways, assessments, description) {
    var pathwaysClasses = '';
    var arrayOfPathways = pathways.split(',');
    for (var i = 0; i < arrayOfPathways.length; i++) {
        pathwaysClasses += arrayOfPathways[i].replace(/\s/g, '') + ' ';
    }
    
    var htmlFormat = `
    <div class="module-table stage-${stage} semester-${semester} ${name.replace(/\s/g, '').toLowerCase()} ${pathwaysClasses}">
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
    
    // Adds each assessment detail to the htmlFormat string
    for (var i = 0; i < assessments.length; i++) {
        htmlFormat += `
            <div>
                <b class="heading">Assessment: </b><span> ${assessments[i]}</span></p>
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
    
    document.getElementsByClassName('modules-container')[0].innerHTML += htmlFormat; // Append the HTML to the modules container
}


/**
 * @Author - @DeanLogan
 * @Description - Adds event listeners to the module information page for search functionality and dropdown interaction.
 */
function listenersForModuleInfoPage() {
    // Adds a click event listener to the search button to trigger search
    document.getElementById('searchbutton').addEventListener("click", function(evt) {
        search();
    });

    // Adds a keypress event listener to the search input to trigger search on Enter key
    document.getElementById('search-input').addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            search();
        }
    });

    // Adds a click event listener to detect clicks inside or outside of the dropdown
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


/**
 * @Author - @DeanLogan
 * @Description - Initiates a search based on the provided search term and selected checkboxes.
 * Retrieves module information, updates the displayed modules, and applies filters if checkboxes are selected.
 */
function search() {
    var values = [];
    var searchTerm = document.querySelector('input[name="search"]').value;
    var checkedCheckboxes = document.getElementById("mySelectOptions").querySelectorAll('input[type=checkbox]:checked');

    for (const item of checkedCheckboxes) {
        var checkboxValue = item.getAttribute('value');
        values.push(checkboxValue);
    }
    
    getModuleInfo(searchTerm);

    if (values.length != 0) {
        // Waits 30ms for response from the get request and for the HTML page to update
        setTimeout(function() {
            hideAllItemsWithClassNames(['module-table']);
            showAllItemsWithClassNames(values);
        }, 30);
    }
}

/**
 * @Author - @DeanLogan
 * @Description - Formats an array of names into a string with dot-separated class names.
 * Replaces whitespace with empty strings to match class naming conventions.
 * @param {string[]} nameArray - Array of names to be formatted into class names.
 * @returns {string} - Dot-separated class names string.
 */
function formatClassNames(nameArray) {
    var names = '';
    for (var i = 0; i < nameArray.length; i++) {
        names += '.';
        names += nameArray[i].replace(/\s/g, '');
    }
    return names;
}

/**
 * @Author - @DeanLogan
 * @Description - Hides all HTML elements with specific class names.
 * Uses the provided array of names to generate dot-separated class names.
 * @param {string[]} nameArray - Array of names used to generate class names of elements to hide.
 */
function hideAllItemsWithClassNames(nameArray) {
    var names = formatClassNames(nameArray);
    document.querySelectorAll(names).forEach(item => {
        item.style.display = 'none';
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Shows all HTML elements with specific class names.
 * Uses the provided array of names to generate dot-separated class names.
 * @param {string[]} nameArray - Array of names used to generate class names of elements to show.
 */
function showAllItemsWithClassNames(nameArray) {
    var names = formatClassNames(nameArray);
    document.querySelectorAll(names).forEach(item => {
        item.style.display = 'grid';
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Handles the change in checkbox status for module filtering.
 * Updates the displayed modules based on the selected checkboxes.
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
    
    if (values.length > 0) {
        dropdownValue = values.join(', ');
        showAllItemsWithClassNames(values);
    } else {
        showAllItemsWithClassNames(['module-table']);
    }

    multiselectOption.innerText = dropdownValue; // updates the text shown to the user to tell them what filters have been applied
}

/**
 * @Author - @DeanLogan
 * @Description - Toggles the state of the checkbox area (dropdown) for selecting filters.
 * @param {boolean} [onlyHide=false] - If true, only hides the checkbox area without opening it.
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