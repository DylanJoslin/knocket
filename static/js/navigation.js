const menuBtn = document.querySelector('.menu-toggle');
const nav = document.querySelector('nav');
const close = document.querySelector('.close-nav');
const dropdown = document.querySelector('.dropdown');
const subMenu = document.querySelector('.sub-menu');

menuBtn.addEventListener('click', function(){
    nav.classList.toggle('show-nav');
});

dropdown.addEventListener('click', function(){
    subMenu.classList.toggle('show-sub-menu');
    subMenu.classList.toggle('sub-menu')
});


close.addEventListener('click', function(){
    nav.classList.remove('show-nav');
});
