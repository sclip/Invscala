eel.expose(finish_loading)
function finish_loading() {
  $("#loading_cover").hide()
}


// Constants
var menuActive = true;
pianoSearches = [];


let SELECTED_NOTE_STYLE_1 = "background-color: #ff5656";  // Computer Selected
let SELECTED_NOTE_STYLE_2 = "background-color: #5656ff";  // User Selected
let SELECTED_NOTE_STYLE_3 = "background-color: #ca2424";  // Root note, computer selected

// A, Bb, B, C, C#, D, Eb, E, F, F#, G, G#
// 0, 1,  2, 3, 4,  5, 6,  7, 8, 9, 10, 11
// + 12
// + 24
let notes = ["A1", "Asharp1", "C1", "Csharp1", "D1", "Dsharp1", "E1", "F1", "Fsharp1", "G1", "Gsharp1", "A2", "Asharp2", "C2", "Csharp2", "D2", "Dsharp2", "E2", "F2", "Fsharp2", "G2", "Gsharp2", "A3", "Asharp3", "C3", "Csharp3", "D3", "Dsharp3", "E3", "F3", "Fsharp3", "G3", "Gsharp3"]
let selected_notes = [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]


function init() {

  document.getElementById("main").onclick = closeOpen;

  let toolbarButtons = document.getElementsByClassName("toolbarObj");
  // Loop through toolbar buttons
  for (let n = 0; n < toolbarButtons.length; n++) {
    let btn = toolbarButtons[n];
    let btnName = btn.innerHTML;
    console.log(btnName);
    btn.onclick = function()  { dropdown(btnName); };
  }

  // Hide content
  let toolbarButtonsContent = document.getElementsByClassName("toolbarObjDropdown");
  for (let n = 0; n < toolbarButtonsContent.length; n++) {
    let ctn = toolbarButtonsContent[n];
    ctn.style = "display: none;";
  }
}
window.onload = init;

// Close open windows

function closeOpen() {
  // Hide toolbar windows
  let toolbarButtonsContent = document.getElementsByClassName("toolbarObjDropdown");
  for (let n = 0; n < toolbarButtonsContent.length; n++) {
    let ctn = toolbarButtonsContent[n];
    ctn.style = "display: none;";
  }
}


// TOOLBAR DROPDOWN STUFF

function dropdown(obj) {
  let dropdownListName = obj + "Dropdown";
  console.log(dropdownListName);
  console.log(document.getElementById(dropdownListName).style.display);
  if (document.getElementById(dropdownListName).style.display == "none") {
    closeOpen();
    document.getElementById(dropdownListName).style = "";  // Remove display: none;
  }
  else {
    document.getElementById(dropdownListName).style = "display: none;";
    closeOpen();
  }

}


// TOOLBAR DROPDOWN STUFF: NOTES

function deselectAll() {
  for (n = 0; n < selected_notes.length; n++) {
    selected_notes[n] = false;
  }
}


//

function selectNote(note) {

    console.log("Selecting note " + note);

    let notes_to_highlight = document.getElementById(note);

    // get the index of the note and then check if it is true, if so, reset style and set to false
    if (selected_notes[notes.indexOf(note)] == true) {
        //for (n = 0; n < (notes_to_highlight.length); n++) {
        //    notes_to_highlight[n].style = "";
        //}
        notes_to_highlight.style = "";
        selected_notes[notes.indexOf(note)] = false;
    }
    else {
        //for (n = 0; n < (notes_to_highlight.length); n++) {
        //    notes_to_highlight[n].style = SELECTED_NOTE_STYLE_2;
        //}
        notes_to_highlight.style = SELECTED_NOTE_STYLE_2;
        selected_notes[notes.indexOf(note)] = true;
    }
}


eel.expose(highlight_notes);
function highlight_notes(notes_, root_note) {
    console.log("Highlighting notes " + notes_);
    console.log("Root Notes: " + root_note)

    for (n = 0; n < notes.length; n++) {
        document.getElementById(notes[n]).style = "";
    }

    for (n = 0; n < notes_.length; n++) {
        document.getElementById(notes_[n]).style = SELECTED_NOTE_STYLE_1;
    }

    for (n = 0; n < root_note.length; n++) {
        document.getElementById(root_note[n]).style = SELECTED_NOTE_STYLE_3;
        console.log("Highlighting root note " + root_note)
    }
}


function highlight_scale() {
    let selected_scale = document.getElementById("infoScaleNamePiano").innerHTML;
    console.log(selected_scale)
    eel.highlight_scale(selected_scale);
}


function menuBtn(to) {
  var btns = document.getElementsByClassName("menuBtn");
  for (n = 0; n < (btns.length); n++) {
    btns[n].style = "";
  }
  document.getElementById(to + "Btn").style = "background-color: rgba(203, 198, 203, 0.10);";

  let cont = document.getElementsByClassName("content");
  for (n = 0; n < (cont.length); n++) {
    cont[n].style = "display: none;";
  }
  document.getElementById(to).style ="display: block;";
}

function switchSearch(to) {
  document.getElementById("selectSearchChords").style = "";
  document.getElementById("selectSearchScales").style = "";
  document.getElementById(to).style = "background-color: rgba(205, 199, 205, 0.15); text-decoration: underline;";

  if (to == "selectSearchChords") {
    // Reset chords search
    let chordsSearch = document.getElementsByClassName("chordsSearch");
    for (n = 0; n < (chordsSearch.length); n++) {
      chordsSearch[n].style = "";
    }

    document.getElementById("pianoSearchResultsChords").style = "";


    // Set to display:none; for scales search
    let scalesSearch = document.getElementsByClassName("scalesSearch");
    for (n = 0; n < (scalesSearch.length); n++) {
      scalesSearch[n].style = "display: none;";
    }

    document.getElementById("pianoSearchResultsScales").style = "display: none;";

  }
  else {
    // Set to display:none; for chords search
    let chordsSearch = document.getElementsByClassName("chordsSearch");
    for (n = 0; n < (chordsSearch.length); n++) {
      chordsSearch[n].style = "display: none;";
    }

    document.getElementById("pianoSearchResultsChords").style = "display: none;";


    // Reset scales search
    let scalesSearch = document.getElementsByClassName("scalesSearch");
    for (n = 0; n < (scalesSearch.length); n++) {
      scalesSearch[n].style = "";
    }
    document.getElementById("pianoSearchResultsScales").style = "";
  }
}



eel.expose(addPianoChordsResult);
function addPianoChordsResult(result) {
    let newResult = document.createElement("div");
    newResult.className = "newResultDiv";
    newResult.id = "tempId"  //  the new element will have a temporary ID to allow us to change it in this function

    document.getElementById('pianoSearchResultsChords').appendChild(newResult);

    // add the p element and the name of the element
    let newResult2 = document.createElement("p");
    newResult2.innerHTML = result;
    document.getElementById("tempId").appendChild(newResult2);
    newResult.removeAttribute("id");
    //newResult.addEventListener("click", getChord(result), false);
    newResult.addEventListener("click", function(){alert(result)}, false);
}

eel.expose(addPianoScalesResult);
function addPianoScalesResult(result) {
    console.log("here!");
    let newResult = document.createElement("div");
    newResult.className = "newResultDivScale";
    newResult.id = "tempId"  //  the new element will have a temporary ID to allow us to change it in this function
    document.getElementById('pianoSearchResultsScales').appendChild(newResult);
    let newResult2 = document.createElement("p");
    newResult2.innerHTML = result;
    document.getElementById("tempId").appendChild(newResult2);
    newResult.removeAttribute("id");
    newResult.addEventListener("click", function(){getScale(result)}, false);
}


function clearChordsResult() {
    document.querySelectorAll('.newResultDiv').forEach(e => e.remove());
    // select all results and delete them
}

function clearScalesResult() {
    document.querySelectorAll('.newResultDivScale').forEach(e => e.remove());
    // select all results and delete them
}


function getChord(chord) {

}


function getScale(scale) {
    eel.get_scale_info(scale);
}
eel.expose(setScaleInfo);
function setScaleInfo(info) {
    console.log(info)
    document.getElementById("infoScaleNamePiano").innerHTML = info[0];
    document.getElementById("infoScaleName2Piano").innerHTML = info[1];
    document.getElementById("infoScaleName3Piano").innerHTML = info[2];
    document.getElementById("infoScaleCardinality").innerHTML = info[3];
    document.getElementById("infoScaleModeCount").innerHTML = info[4];
    document.getElementById("infoScaleMode").innerHTML = info[5];
    document.getElementById("infoScaleFormulaInterval").innerHTML = info[6];
    document.getElementById("infoScaleFormula").innerHTML = info[7];
    document.getElementById("infoScaleTriadsPiano").innerHTML = info[8];
    document.getElementById("infoScaleChordsPiano").innerHTML = info[9];
    document.getElementById("infoScaleNotesPiano").innerHTML = info[10];
    highlight_scale();
}

function indexChordsPiano() {
    clearChordsResult();
    toIndex = document.getElementById("pianoChordsSearch").value;
    eel.index_chords(toIndex);
}

function indexScales() {
    clearScalesResult();
    toIndex = document.getElementById("pianoScalesSearch").value;
    eel.search_scales(toIndex, false);
}

// debug functions
function db() {
  addPianoChordsResult(document.getElementById("pianoChordsSearch").value);
}
function dbd() {
  clearPianoChordsResult();
}
