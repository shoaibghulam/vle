//Program created by Ryan Tarson Updated 6.15.16, under this is my pure JS Version
jQuery(document).ready(function($) {
  var wHeight = window.innerHeight;
  //search bar middle alignment
  $('#mk-fullscreen-searchform').css('top', wHeight / 2);
  //reform search bar
  jQuery(window).resize(function() {
    wHeight = window.innerHeight;
    $('#mk-fullscreen-searchform').css('top', wHeight / 2);
  });
  // Search
  $('#search-button').click(function() {
    console.log("Open Search, Search Centered");
    $("div.mk-fullscreen-search-overlay").addClass("mk-fullscreen-search-overlay-show");
  });
  $('#search-button2').click(function() {
    console.log("Open Search, Search Centered");
    $("div.mk-fullscreen-search-overlay").addClass("mk-fullscreen-search-overlay-show");
  });
  $("a.mk-fullscreen-close").click(function() {
    console.log("Closed Search");
    $("div.mk-fullscreen-search-overlay").removeClass("mk-fullscreen-search-overlay-show");
  });
});

		// Preloader
		var overlay = document.getElementById("overlay");
			window.addEventListener('load', function(){
			  overlay.style.display = 'none';
		});
/* Don't Like jQuery or have a custom jQuery that's conflicting? Then you can use my Pure JS program Below. Runs exactly the same and so is the preformance just Pure JS*/
//Program made by Ryan Tarson
/*
 var wHeight = window.innerHeight;
 var sb = document.getElementById("search-button");
 var closeSB = document.getElementById("mk-fullscreen-close-button");
 var SearchOverlay = document.getElementById("mk-search-overlay");
 var searchBar = document.getElementById("mk-fullscreen-searchform");
 searchBar.style.top=wHeight/2 +'px';
  console.log(wHeight);
  window.addEventListener("resize", function(){
	  console.log(wHeight);
	   wHeight = window.innerHeight;
	   searchBar.style.top=wHeight/2 + 'px';
  }, true);
  document.addEventListener("click", function(){
  sb.onclick = function(){
	console.log("Opened Search for Element: ");
	SearchOverlay.classList.add("mk-fullscreen-search-overlay-show");
  };
  closeSB.onclick = function(){
	  console.log("Closed Search for Element: " + closeSB);
	  SearchOverlay.classList.remove("mk-fullscreen-search-overlay-show");
  };
  }, true);
  */
