// const menuBtn = document.querySelector('.menu-toggle');
// const nav = document.querySelector('nav');
// const close = document.querySelector('.close-nav');
// const dropdown = document.querySelector('.dropdown');
// const subMenu = document.querySelector('.sub-menu');

// menuBtn.addEventListener('click', function(){
//     nav.classList.toggle('show-nav');
// });

// dropdown.addEventListener('click', function(){
//     subMenu.classList.toggle('show-sub-menu');
//     subMenu.classList.toggle('sub-menu')
// });


// close.addEventListener('click', function(){
//     nav.classList.remove('show-nav');
// });


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
