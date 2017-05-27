/*
Template: AdForest | Largest Classified Portal
Author: ScriptsBundle
Version: 1.0
Designed and Development by: ScriptsBundle
*/
/*
====================================
[ CSS TABLE CONTENT ]
------------------------------------
    1.0 -  Page Preloader
	2.0 -  Page Scrolling Plugin
    3.0 -  Jquery Parallex
	4.0 - Back To Top
-------------------------------------
[ END JQUERY TABLE CONTENT ]
=====================================
*/
(function($) {
    "use strict";

    /* ======= Preloader ======= */
    setTimeout(function() {
        $('body').addClass('loaded');
    }, 3000);
	
	/* ======= Page Scrolling Plugin ======= */
    $('a.page-scroll').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 60
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
   
   /* ======= Jquery Parallex ======= */
	if ( $( "body.parallax" ).length > 0 ) {
		$.stellar( {
			scrollProperty: 'scroll',
			verticalOffset: 0,
			horizontalOffset: 0,
			horizontalScrolling: false,
			responsive: true
		} );
	}

    /*==========  Back To Top  ==========*/
    	var offset = 300,
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.cd-top');
		//hide or show the "back to top" link
		$(window).scroll(function() {
			($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
			if ($(this).scrollTop() > offset_opacity) {
				$back_to_top.addClass('cd-fade-out');
			}
		});
    	//smooth scroll to top
		$back_to_top.on('click', function(event) {
	
			event.preventDefault();
			$('body,html').animate({
				scrollTop: 0,
			}, scroll_top_duration);
		});

})(jQuery);