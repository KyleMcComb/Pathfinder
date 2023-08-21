/**
 * @Author - @DeanLogan123
 * @Description - Adds rows to a table for displaying backup file information. Each row contains a formatted date-time,
 * optional count of files with the same date-time, and links for restore and delete actions.
 * @param {string[]} fileNames - An array of backup file names.
 * @param {HTMLElement} tbody - The HTML <tbody> element to which rows will be added.
 */
function addBackupRowsToTable(fileNames, tbody) {
    const dateTimeCounts = {}; // To keep track of file counts with the same date-time
    // Create an array of HTML strings using the map function
    const htmlStrings = fileNames.map(fileName => {
        // Use regex to extract date-time information from the fileName
        const match = fileName.match(/-(\d{4}-\d{2}-\d{2})-(\d{6})(?:_(\w+))?\.dump/);
        if (match) {
            // Destructure values from the match array using specific indices
            const [_, datePart, timePart] = match;
            // Initialize the count for this date-time if not already set
            const dateTimeKey = datePart + timePart;
            dateTimeCounts[dateTimeKey] = (dateTimeCounts[dateTimeKey] || 0) + 1;
            const count = dateTimeCounts[dateTimeKey];
            // Format the time as HH:MM:SS
            const formattedTime = `${timePart.replace(/(\d{2})(\d{2})(\d{2})/, '$1:$2')}`;
            
            // Construct the name with count and hashValue if needed
            let formattedName = `${datePart} - ${formattedTime}`;
            if (count > 1) {
                formattedName += ` - ${count}`;
            }
            // Return the formatted row as an HTML string
            return `
                <tr class="model-group">
                    <th scope="row"><a href="">${formattedName}</a></th>
                    <td><a href="/admin/backups/restore/" class="addlink">Restore</a></td>
                    <td><a href="/admin/backups/delete/" class="deletelink">Delete</a></td>
                </tr>
            `;
        }
    });
    
    // Join the array of HTML strings and insert into the tbody
    tbody.insertAdjacentHTML('beforeend', htmlStrings.join(''));
}

/**
 * @Author - @DeanLogan123
 * @Description - Makes a request to fetch backup file information and updates the table with the results.
 * If there are backup files available, it adds rows with file details to the table.
 * If no files are found, it adds a single row indicating no files are available.
 * @param {string} request - The URL or endpoint for fetching backup file information.
 * @param {HTMLElement} tbody - The HTML <tbody> element of the table to be updated.
 */
function backupFilesRequestMaker(request, tbody) {
    // Make a GET request to fetch backup file information
    $.get(request, function(data) {
        if (data.fileNames.length > 0) {
            // If there are files, add rows with backup details to the table
            addBackupRowsToTable(data.fileNames, tbody);
        } else {
            // If no files found, add a row indicating no files are available
            tbody.insertAdjacentHTML('beforeend', `
                <tr class="model-group">
                    <th scope="row"><a href="">No Files Found</a></th><td></td>
                </tr>
            `);
        }
    });
}

/**
 * @Author - @DeanLogan123
 * @Description - Executes when the page loads to populate local and cloud backup tables with file information.
 * Fetches and displays backup file information in the respective tables.
 */
function pageLoad() {
    // Populate the local backup table with file information
    backupFilesRequestMaker("/listLocalBackupFiles/", document.getElementById("localBackupTable"));
    
    // Populate the cloud backup table with file information
    backupFilesRequestMaker("/listCloudBackupFiles/", document.getElementById("cloudBackupTable"));
}

// Set the pageLoad function to execute when the window finishes loading
window.onload = pageLoad();
