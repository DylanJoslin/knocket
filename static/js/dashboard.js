$(document).ready(function() {
	$('.menu-icon').click(function() {
		$('.dashboard-navigation').toggleClass('menu-toggle');
		$('.menu-icon').toggleClass('icon-closed');
		$('.dashboard-header').toggleClass('menu-closed-header-style ');
	});

	// $('.dashboard-label > i').hover(function(event) {
	// 	var icon = $(this).toggleClass('color');

	// 	event.preventDefault();
	// });

	// $('.dashboard-label > i').click(function(event) {
	// 	$(this).parent().parent().find('.tooltip').toggleClass('hidden');
	// 	event.preventDefault();
	// });

	(function($) {
		var allPanels = $('.acc-user-info');
		allPanels.hide();

		$('.acc-user-dropdown').click(function() {
			var content = $(this).siblings();
			if(!content.is(':visible')){
				allPanels.slideUp();
				content.slideDown();
				var accordian = $(this).parent().parent().parent();

				if(accordian.hasClass('users-acc') == true){
					$('.overview-background-second').addClass('overview-bgd-moved');
				} else if (accordian.hasClass('users-acc') == false){
					$('.overview-background-second').removeClass('overview-bgd-moved');
				}
			}

		});
	})(jQuery);


	function fixBackground(thisElement, accInfoSelector){

		if(thisElement.parent().parent().hasClass('users-acc') == true){

			if(!accInfoSelector.is(':visible') ){

				if($('.overview-background-second').hasClass('overview-bgd-moved') == true){
					$('.overview-background-second').removeClass('overview-bgd-moved');
				}

			} else if(accInfoSelector.is(':visible') ){
				if($('.overview-background-second').hasClass('overview-bgd-moved') == false){
					$('.overview-background-second').addClass('overview-bgd-moved');
				}
			}

		}

	}

	$('.acc-new-uploads').click(function(event) {
		$('#new-uploads').removeClass('hidden');
		$('#published-uploads').addClass('hidden');

		event.preventDefault();
	});

	$('.acc-published-uploads').click(function(event) {
		$('#published-uploads').removeClass('hidden');
		$('#new-uploads').addClass('hidden');

		event.preventDefault();
    });
    
    $('.acc-new-users').click(function(event) {




		$('#new-users').removeClass('hidden');
		$('#admin-users').addClass('hidden');
		$('#registered-users').addClass('hidden');
		$('#elder-users').addClass('hidden');
		$('#teacher-users').addClass('hidden');

		$thisElement = $(this);
		$accInfoSelector = $('.users-acc > #new-users > .acc-single > .acc-user-info');
		fixBackground($thisElement, $accInfoSelector);

		event.preventDefault();
	});

	$('.acc-registered-users').click(function(event) {
		$('#registered-users').removeClass('hidden');
		$('#new-users').addClass('hidden');
		$('#admin-users').addClass('hidden');
		$('#elder-users').addClass('hidden');
		$('#teacher-users').addClass('hidden');

		$thisElement = $(this);
		$accInfoSelector = $('.users-acc > #registered-users > .acc-single > .acc-user-info');
		fixBackground($thisElement, $accInfoSelector);

		event.preventDefault();
	});

	$('.acc-teachers').click(function (event) {
		$('#teacher-users').removeClass('hidden');
		$('#new-users').addClass('hidden');
		$('#registered-users').addClass('hidden');
		$('#elder-users').addClass('hidden');
		$('#admin-users').addClass('hidden');

		$thisElement = $(this);
		$accInfoSelector = $('.users-acc > #teacher-users > .acc-single > .acc-user-info');
		fixBackground($thisElement, $accInfoSelector);

		event.preventDefault();
	});

	$('.acc-elders').click(function (event) {
		$('#elder-users').removeClass('hidden');
		$('#new-users').addClass('hidden');
		$('#registered-users').addClass('hidden');
		$('#admin-users').addClass('hidden');
		$('#teacher-users').addClass('hidden');

		$thisElement = $(this);
		$accInfoSelector = $('.users-acc > #elder-users > .acc-single > .acc-user-info');
		fixBackground($thisElement, $accInfoSelector);

		event.preventDefault();
	});

	$('.acc-admins').click(function (event) {
		$('#admin-users').removeClass('hidden');
		$('#new-users').addClass('hidden');
		$('#registered-users').addClass('hidden');
		$('#elder-users').addClass('hidden');
		$('#teacher-users').addClass('hidden');

		$thisElement = $(this);
		$accInfoSelector = $('.users-acc > #admin-users > .acc-single > .acc-user-info');
		fixBackground($thisElement, $accInfoSelector);

		event.preventDefault();
	});
});
