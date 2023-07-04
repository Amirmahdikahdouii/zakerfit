/*=========

Template Name: Educater - Online Courses & Education HTML Template

=========*/

/*=========

----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Magnific Popup JS

=========*/

$(document).ready(function($) {

	// Whole Script Strict Mode Syntax
	"use strict";

    // Magnific Popup JS Start
    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });
    // Magnific Popup JS End
 
});