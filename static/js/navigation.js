
$(document).ready(function() {
	$('.menu-icon').click(function() {
		$('.main-navigation').toggleClass('menu-toggle');
		$('.menu-icon').toggleClass('icon-closed');
		$('.main-header').toggleClass('menu-closed-header-style ');
	});
	
	$('.dropdown').click(function(event){
		console.log("clicked");
		$('.sub-menu').toggleClass('hidden');

		event.preventDefault();
	});

});
