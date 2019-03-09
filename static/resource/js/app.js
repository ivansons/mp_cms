$(document).ready(function(){
  $.mainNavTop = $('#main-nav').offset().top;

  $('.dropdown').dropit();

  $('.dropit-submenu li').click(function(e){
    e.preventDefault();
    $(this).toggleClass('selected');

    if ($(this).hasClass('selected')) {
      $('.resource' + '.' + $(this).data('tag')).show();
    }
    else {
      $('.resource' + '.' + $(this).data('tag')).fadeOut();
    }
  });

  $('.dropit-submenu .button').click(function(e){
    $('.dropit-submenu').hide();
  });

  $( window ).scroll(function() {
    if ($(this).scrollTop() > $.mainNavTop) {
      $('#main-nav').addClass('stuck');
    }
    else {
      $('#main-nav').removeClass('stuck');
    }
  });
});
