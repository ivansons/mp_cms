/**
 * Borrowed from Thor, 09/29/2016.
 */
$(document).ready(function () {

  // Hide Header on on scroll down
  var didScroll;
  var lastScrollTop = 0;
  var delta = 5;
  var navbarHeight = $('.banneri').outerHeight();

  $(window).scroll(function (event) {
    didScroll = true;
  });

  // Hide banner on clicking
  $('.banneri').click(function () {
    $(this).addClass('hide');
  });

  setInterval(function () {
    if (didScroll) {
      hasScrolled();
      didScroll = false;
    }
  }, 250);

  function hasScrolled() {
    var st = $(this).scrollTop();

    // Make sure they scroll more than delta
    if (Math.abs(lastScrollTop - st) <= delta)
      return;

    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st > lastScrollTop && st > navbarHeight) {
      // Scroll Down
      $('.banneri').removeClass('nav-down').addClass('nav-up');
    } else {
      // Scroll Up
      if (st + $(window).height() < $(document).height()) {
        $('.banneri').removeClass('nav-up').addClass('nav-down');
      }
    }

    lastScrollTop = st;
  }
});
