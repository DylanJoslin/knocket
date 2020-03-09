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
            
            // iconPlus.addClass('hidden');
            // iconMinus.removeClass('hidden');
            
        });
      
      })(jQuery);

    

    $('.acc-new-uploads').click(function(event){
        $('#new-uploads').removeClass('hidden');
        $('#published-uploads').addClass('hidden');

        event.preventDefault();
    });

    $('.acc-published-uploads').click(function(event){
        $('#published-uploads').removeClass('hidden');
        $('#new-uploads').addClass('hidden');
        
        event.preventDefault();
    });

});

