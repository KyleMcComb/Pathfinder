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
            <h3>Assesment name: </h3>
        </div>
        <div>
            <h3>Assesment name: </h3>
        </div>
        <div>
            <b class="heading">Description: </b><br />
            <p>${description}</p>
        </div>
    </div>
    `;

    document.getElementsByClassName('content')[0].innerHTML += htmlFormat;

}