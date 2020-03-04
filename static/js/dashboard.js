$(document).ready(function(){

    $('.menu-icon').on('click', function(){
        $('.dashboard-navigation').toggleClass('menu-toggle');
        $('.menu-icon').toggleClass('icon-closed');
        $('.dashboard-header').toggleClass('menu-closed-header-style ');
    });

    $('.acc-user-dropdown').click(function(event){
        console.log("clicked");

        $('.acc-user-info').toggleClass('closed');
        if($('.acc-user-info').hasClass('closed')){
            $('.icon').html('+');
        } else {
            $('.icon').html('-');
        }
       


        event.preventDefault();
    });

});

