$(function() {
  /*
  Use jQuery to dynamically set the height of embed model to make sure:
  1. The model has as max as possible height according to different window
  size
  2. The model should not take the whole height of visible screen
  */
  var setModelHeight = function() {
    var windowWidth = $(window).width();
    var windowHeight = $(window).height();
    var margin = $(".info-box-model").height() + $("#header").height();

    // Mobile browser address bar changes $(window).height(). This fix uses
    // screen width as `windowHeight` in landscape mode, giving maximum view
    // area for showcase.
    if ((/Android|iPhone|iPad|iPod|BlackBerry/i).test(navigator.userAgent ||
        navigator.vendor || window.opera) && windowWidth > windowHeight) {
      windowHeight = Math.min(screen.width, screen.height);
      windowHeight -= Math.max(0, (windowHeight - Math.min(
        $(window).width(), $(window).height())) / 2)
    }

    var modelWidth = $(".wp3d-embed-wrap").width();
    var aspectRatio = .5625;
    if (windowWidth <= 481) {
      aspectRatio = 1.5;
    } else if (windowWidth <= 767) {
      aspectRatio = .85;
    } else if (windowWidth <= 1023) {
      aspectRatio = .70;
    }
    var modelHeight = aspectRatio * modelWidth;
    modelHeight = Math.min(modelHeight, windowHeight - margin);

    $(".wp3d-embed-wrap").css("padding-bottom", "0").height(modelHeight);
  };

  setModelHeight();
  $(window).on('resize orientationchange', setModelHeight);

  /*
  Fix scroll model page. When scrolling up in model page,
  the page get stuck when the model iframe capture cursor.
   */
  (function() {
    var previousScroll = 0;
    var scrolling = false;

    $(window).scroll(function(e){
      if (scrolling) {
        e.preventDefault();
        return false;
      }
      var currentScroll = $(this).scrollTop();

      if (currentScroll < previousScroll && currentScroll < $(".wp3d-embed-wrap").height() / 2.) {
        scrolling = true;
        $('body').animate({scrollTop: 0}, 300, function(){
          scrolling = false;
          previousScroll = 0;
        });
      } else {
        previousScroll = currentScroll;
      }
    });
  })();

  /* Space Gallery Embed Code */
  $(".space-embed").fancybox({
    maxWidth: 800,
    maxHeight: 600,
    fitToView: false,
    width: '70%',
    height: '50%',
    autoSize: false,
    closeClick: false,
    openEffect: 'none',
    closeEffect: 'none'
  });
});
