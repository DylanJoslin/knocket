$(document).ready(function(){

    $('.menu-icon').on('click', function(){
        $('.dashboard-navigation').toggleClass('menu-toggle');
        $('.menu-icon').toggleClass('icon-closed');
        $('.dashboard-header').toggleClass('menu-closed-header-style ');
    });

    (function($) {
    
        var allPanels = $('.acc-user-info');
        allPanels.hide();
        
        $('.acc-user-dropdown').click(function() {
            allPanels.slideUp();
            var content = $(this).siblings();
            content.slideDown();
        });
      
      })(jQuery);

    

    // function accordianClick(event){
    //     var user = $(this).siblings();
    //     user.toggleClass('closed');
    //     var icon = $(this).find('.icon');

    //     if(user.hasClass('closed')){
    //         icon.html('+');
    //     } else {
    //         icon.html('-');
    //     }

    //     event.preventDefault();
    // }

    $('.acc-user-dropdown').click(function(event){

    });

    $('.acc-new').click(function(event){
        console.log("new");

        event.preventDefault();
    });

    $('.acc-registered').click(function(event){
        console.log("registered");

        event.preventDefault();
    });

});

