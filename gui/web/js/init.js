var GUI_SELEC_BACKGROUND = "#DDD";
var PIA_SELEC_BACKGROUND = "#70206A";
var HIGHLIGHT_BACKGROUND = "#5656FF";
var ROOT_HIGH_BACKGROUND = "#CA2424";
var BTN_SELEC_BACKGROUND = "#534549";
var BTN_NORML_BACKGROUND = "#423438";


var searching_chords = true;
var mouse_on_context = false;
var mouse_on_tlb_dropdown = false;
var mouse_on_res_dropdown = false;
var mouse_on_chord_menu = false;
var selected_chord = "";

var drop_y_pos = 0;


eel.expose(finish_loading);
function finish_loading() {
  $("#loading_cover").hide();
}


// Call this function to check if eel is running


function test_func() {
  eel.test_func();
}



////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


// Create a single element, under the ID to
eel.expose(build_elem);
function build_elem(elem, to) {
  document.getElementById(to).innerHTML += elem;
  console.log("Built elem " + to)
}


// Create elements under all instances of class to
eel.expose(build_elems);
function build_elems(elem, to) {
  to_list = document.getElementsByClassName(to);
  for (let i = 0; i < to_list.length; i++) {
    to_list[i].innerHTML += elem;
  }
}


////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
//
//
// Finally we get to the interactive stuff
//
//


function change_instrument_view() {
  $(".instrument_view").hide();
  $("#" + document.getElementById("instrument_selector_select").value).show();
}


function change_search_type_guitar(clicker) {
  elems = document.getElementsByClassName("btn_wide_search_guitar");
  for (let i = 0; i < elems.length; i++) {
    elems[i].style = "";
  }
  document.getElementById(clicker.id).style = "background-color: " + BTN_SELEC_BACKGROUND + ";";
  switch(clicker.id) {
    case "search_select_chord_guitar":
      $(".search_results_container").hide();
      $("#search_results_guitar_chord").show();
      searching_chords = true;
      break;
    case "search_select_scale_guitar":
      $(".search_results_container").hide();
      $("#search_results_guitar_scale").show();
      searching_chords = false;
      break;
  }
}


function toolbar_dropdown(from_) {
  $(".tlb_dropdown").hide();
  let parent = from_.id + "_parent";
  $("#" + parent + " .tlb_dropdown").show();
}


// Interactive Instrument


function select_fret(master_fret) {
  if (document.getElementById(master_fret.id + "_name").style.display == "none") {
    $("#" + master_fret.id + ">div").show();
    if (master_fret.className != "nut_fret") {
      document.getElementById(master_fret.id).style = "background-color: #DDD;";
    } else {
      document.getElementById(master_fret.id).style = "border-right: 10px solid #FFF; color: #EEE;";
    }

  } else {
    $("#" + master_fret.id + ">div").hide();
    document.getElementById(master_fret.id).style = "";
  }
  eel.select_guitar_note(master_fret.id);
}


eel.expose(deselect_all_frets);
function deselect_all_frets() {
  $(".fret_name").hide();
  elems = document.getElementsByClassName("fret");
  for (let i = 0; i < elems.length; i++) {
    elems[i].style = "";
  }
  elems = document.getElementsByClassName("nut_fret");
  for (let i = 0; i < elems.length; i++) {
    elems[i].style = "";
  }

}


eel.expose(highlight_fret);
function highlight_fret(fret) {
  console.log(fret);
  $("#" + fret + ">div").show();
  if (fret.className != "nut_fret") {
    document.getElementById(fret).style = "background-color: " + HIGHLIGHT_BACKGROUND + ";";
  } else {
    document.getElementById(fret).style = "border-right: 10px solid #FFF; color: #EEE;";
  }
}


function reset_highlight() {
  $(".fret_name").hide();
  elems = document.getElementsByClassName("fret");
  for (let i = 0; i < elems.length; i++) {
    elems[i].style = "";
  }
  elems = document.getElementsByClassName("nut_fret");
  for (let i = 0; i < elems.length; i++) {
    elems[i].style = "";
  }
}


// search

eel.expose(search_append);
function search_append(result, type) {
  console.log("here");
  let div = $('<div id="' + result + '" class="search_result">')
    .css({
    })
    .append(result)
    .appendTo("#search_results_guitar_chord");
  $(div).click(function(){
    // get_info(result, type, this);
    show_side_dropdown(result, type, this);
  });
  $(div).append("<div class='search_result_dropdown' style='display: none;'><div class='search_result_dropdown_item'>Display</div></div>")
  $(div).on({
    mouseenter: function(){
      mouse_on_res_dropdown = true;
      mouse_on_chord_menu = true;
      console.log("test");
    },
    mouseleave: function(){
      mouse_on_res_dropdown = false;
      mouse_on_chord_menu = false;
    }
  });
}


function reset_search() {
  document.querySelectorAll('.search_result').forEach(e => e.remove());
}


function search(from_, type_) {
  reset_search();
  eel.search(from_, type_);
}


function get_info(obj_name, type, from_) {
  $(".search_result_dropdown").hide();
  //from_.id = "temp_id";
  $("#" + from_.id + ">div").show();
  selected_chord = from_.id;
  console.log(from_.id);
  //from_.removeAttribute("id");
}


function show_side_dropdown(obj_name, type, from) {
  $("#res_context_menu").hide();
  drop_y_pos = mouseY(event) - 7;
  document.getElementById("res_context_menu").style.top = drop_y_pos + 'px';

  $("#res_context_menu_header").html("");
  $("#res_context_menu_header").html(obj_name);
  selected_chord = obj_name;

  switch(type) {
    case "Chords":
      $(".res_context_menu_chords").show();
  }

  $("#res_context_menu").show();
}


function on_search_input(from_) {
  val = document.getElementsByName(from_)[0].value;
  switch(searching_chords) {
    case true:
      search(val, "Chords");
      break;
    case false:
      search(val, "Scales");
      break;
  }
}


// Displaying Stuff


function display_lowest(chord_name) {
  reset_highlight();
  eel.display_lowest_chord(chord_name);
}


//

function mouseX(evt) {
  if (evt.pageX) {
    return evt.pageX;
  } else if (evt.clientX) {
    return evt.clientX + (document.documentElement.scrollLeft ?
      document.documentElement.scrollLeft :
      document.body.scrollLeft);
  } else {
    return null;
  }
}

function mouseY(evt) {
  if (evt.pageY) {
    return evt.pageY;
  } else if (evt.clientY) {
    return evt.clientY + (document.documentElement.scrollTop ?
      document.documentElement.scrollTop :
      document.body.scrollTop);
  } else {
    return null;
  }
}


////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
// Onload
$(function(){
  // Hide things that should not be visible by default.
  $(".hide_by_default").hide();
  $(".res_context_menu_subcategory").hide();
  $("#Piano").hide();
  $("#piano_left_menu_bar").hide();
  $("#search_results_guitar_scale").hide();
  $(".context_menu").hide();
  $(".tlb_dropdown").hide();
  $(".search_result_dropdown").hide();
  $("#res_context_menu").hide();
  document.getElementById("guitar_select_fretboard").style = "background-color: #534549;";
  document.getElementById("search_select_chord_guitar").style = "background-color: #534549;";

  // Start with a search done

  switch(searching_chords) {
    case true:
      search("", "Chords");
      break;
    case false:
      search("", "Scales");
      break;
  }

  // Overwrite default right-click function
  if (document.addEventListener) {
    document.addEventListener('contextmenu', function(e) {
      e.preventDefault();
      elems = document.getElementsByClassName("context_menu");
      for (let i = 0; i < elems.length; i++) {
        elems[i].style.display = "block";
        elems[i].style.top = mouseY(event) + 'px';
        elems[i].style.left = mouseX(event) + 'px';
      }
    }, false);
  } else {
    document.attachEvent('oncontextmenu', function() {
      window.event.returnValue = false;
    });
  }

  // Stop certain menus from being closed while the mouse is on top of it
  // TODO: find a way to make this smoother
  $(".context_menu").on({
    mouseenter: function(){
      mouse_on_context = true;
    },
    mouseleave: function(){
      mouse_on_context = false;
    }
  });

  $(".toolbar_button").on({
    mouseenter: function(){
      mouse_on_tlb_dropdown = true;
    },
    mouseleave: function(){
      mouse_on_tlb_dropdown = false;
    }
  });

  $(".search_result").on({
    mouseenter: function(){
      mouse_on_res_dropdown = true;
    },
    mouseleave: function(){
      mouse_on_res_dropdown = false;
    }
  });

  $("#res_context_menu").on({
    mouseenter: function(){
      mouse_on_chord_menu = true;
    },
    mouseleave: function(){
      mouse_on_chord_menu = false;
    }
  });






});


function init() {
  eel.setup();  // Call eel and let python modify the DOM after loading
}
window.onload = init;


// Finish setup is called when all the python code has finished loading
eel.expose(finish_setup);
function finish_setup() {
  $(".fret_name").hide();


  ////////////////////// JQuery Interactive Stuff //////////////////////////////

  $(".fret").click(function(){
    select_fret(this);
  });

  $(".nut_fret").click(function(){
    select_fret(this);
  });

  $(".btn_wide_search_guitar").click(function(){
    change_search_type_guitar(this);
  });

  $(".toolbar_button_name").click(function(){
    toolbar_dropdown(this);
  });

  $(".search_result_dropdown_item").click(function(){
    chord_name = selected_chord;
    display_lowest(chord_name);
  });

  $("#display_chord_btn").click(function(){
    $("#res_context_menu_display_chords").show();
  });

  $(".search_result").on({
    mouseenter: function(){
      mouse_on_res_dropdown = true;
    },
    mouseleave: function(){
      mouse_on_res_dropdown = false;
    }
  });

  // On clicking outside of the context menu
  $(document).bind("click", function(event) {
    if (!mouse_on_context) {  // Related to the function above
      $(".context_menu").hide();
    }
    if (!mouse_on_tlb_dropdown) {
      $(".tlb_dropdown").hide();
    }
    if (!mouse_on_res_dropdown) {
      $(".search_result_dropdown").hide();
    }
    if (!mouse_on_chord_menu) {
      $("#res_context_menu").hide();

      $("#res_context_menu_display_chords").hide();
    }
  });






  finish_loading();
}
