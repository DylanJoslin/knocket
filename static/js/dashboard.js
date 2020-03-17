$(document).ready(function() {
	$('.menu-icon').click(function() {
		$('.dashboard-navigation').toggleClass('menu-toggle');
		$('.menu-icon').toggleClass('icon-closed');
		$('.dashboard-header').toggleClass('menu-closed-header-style ');
	});

	$('.dashboard-label > i').hover(function(event) {
		var icon = $(this).toggleClass('color');

		event.preventDefault();
	});

	$('.dashboard-label > i').click(function(event) {
		$(this)
			.parent()
			.parent()
			.find('.tooltip')
			.toggleClass('hidden');

		event.preventDefault();
	});

	(function($) {
		var allPanels = $('.acc-user-info');
		allPanels.hide();

		$('.acc-user-dropdown').click(function() {
			allPanels.slideUp();
			var content = $(this).siblings();
			content.slideDown();
			var iconPlus = $(this).find('.icon-plus');
			var iconMinus = $(this).find('.icon-minus');
		});
	})(jQuery);

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
});
