$(document).ready(function(){

    $('.menu-icon').on('click', function(){
        $('.dashboard-navigation').toggleClass('menu-toggle');
        $('.menu-icon').toggleClass('icon-closed');
        $('.dashboard-header').toggleClass('menu-closed-header-style ');
    });

});

