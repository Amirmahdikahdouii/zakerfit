/*=========

Template Name: Fithub - Gym & Fitness HTML Template

=========*/

/*=========
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Portfolio Tabbing JS
=========*/

$(document).ready(function($) {

	// Whole Script Strict Mode Syntax
	"use strict";

	// Portfolio Tabbing JS Start
    $(function() {
    var filterList = {
        init: function() {
            // MixItUp plugin
            // http://mixitup.io
            $('#portfoliolist').mixItUp({
                selectors: {
                    target: '.portfolio-filter',
                    filter: '.filter'
                },
                load: {
                    filter: '.all, .weight-loss, .power-yoga, .weight-gain, .boxing'
                }
            });
        }
    };
    // Run the show!
    filterList.init();
    });
    // Portfolio Tabbing JS End
   
});