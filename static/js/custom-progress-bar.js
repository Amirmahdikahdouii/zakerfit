/*==========

Template Name: Morbizz - SEO & Digital Marketing HTML Template
==========*/

/*==========
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Skill Progress Bar JS
==========*/



$(document).ready(function($) {

	// Whole Script Strict Mode Syntax
	"use strict";

	var a = 0;
	var b = 0;
	$(window).on('scroll', function() {

	// Skills Progress Bar JS Start
	var oTop2 = $('#progress_bar').offset().top - window.innerHeight;
	if (b === 0 && $(window).scrollTop() > oTop2) {
		$(".skill-bar").each(function(){
		  $(this).find(".skill-bar-inner").animate({
			width: $(this).attr("data-width")
		  },3000);
		});
	}
	// Skills Progress Bar JS End

	});

});