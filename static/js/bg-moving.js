/*==========

Template Name: Educater - Online Courses & Education HTML Template

==========*/

/*==========
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Banner Moving JS
==========*/


$(document).ready(function($) {

	// Whole Script Strict Mode Syntax
	"use strict";
});

	// Banner Moving JS Start
	var lFollowX = 0,
		lFollowY = 0,
		x = 0,
		y = 0,
		friction = 1 / 30;

	function moveBackground() {
		x += (lFollowX - x) * friction;
		y += (lFollowY - y) * friction;

		//  translate = 'translateX(' + x + 'px, ' + y + 'px)';
		translate = 'translateX(' + x + 'px) translateY(' + y +'px)';

		$('.animate-this').css({
		'-webit-transform': translate,
		'-moz-transform': translate,
		'transform': translate
		});

		window.requestAnimationFrame(moveBackground);
	}

	$(window).on('mousemove click', function(e) {
		
		var isHovered = $('.animate-this:hover').length > 0;
		console.log(isHovered);
		
		//if(!$(e.target).hasClass('animate-this')) {
		if(!isHovered) {
			var lMouseX = Math.max(-100, Math.min(100, $(window).width() / 2 - e.clientX)),
					lMouseY = Math.max(-100, Math.min(100, $(window).height() / 2 - e.clientY));

			lFollowX = (20 * lMouseX) / 100;
			lFollowY = (10 * lMouseY) / 100;
		}
	});

	moveBackground();
	// Banner Moving JS End


	

