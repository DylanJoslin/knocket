$(document).ready(function(){

    $('.menu-icon').click(function(){
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
            var iconPlus = $(this).find('.icon-plus');
            var iconMinus = $(this).find('.icon-minus');

            // console.log(iconPlus);
            // console.log(iconMinus);
            iconPlus.addClass('hidden');
            iconMinus.removeClass('hidden');
            
        });
      
      })(jQuery);

    $('.acc-new').click(function(event){
        console.log("new");
            
        $('#new-users').removeClass('hidden');
        $('#registered-users').addClass('hidden');

        event.preventDefault();
    });

    $('.acc-registered').click(function(event){
        console.log("registered");

        $('#new-users').addClass('hidden');
        $('#registered-users').removeClass('hidden');
        
        event.preventDefault();
    });

});

