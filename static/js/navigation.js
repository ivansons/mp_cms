$(function() {
  /* Mark the active nav menu */
  /*
  var markActiveNavItems = function () {
    var currentURL = window.location.pathname;
    $('.navigation li > a').each(function () {
      var navURL = $(this).attr('href');
      var re = new RegExp('^' + navURL);
      if (re.test(currentURL)) {
        $(this).parent().addClass('active');
      }
    });
    $('.menu ul li > a').each(function () {
      var navURL = $(this).attr('href');
      var re = new RegExp('^' + navURL);
      if (re.test(currentURL)) {
        $(this).parent().addClass('active');
        $(this).removeAttr('style');
      }
    });
  };

  markActiveNavItems();

  // Remove marked active nav menu when hovering
  $('.navigation').hover(
    function () {
      if (document.body.clientWidth >= 1024) {
        $('.navigation li').removeClass('active');
      }
    },
    markActiveNavItems
  );
  */

  /* Mobile navigation sub-menu items */
  $('div.menu-mobile').click(function () {
    var $subMenu = $(this).children('ul:first');
    var $title = $('#' + $(this).attr('id') + ' span:first');
    console.log($title);
    if (!$subMenu.hasClass('active')) {
      $title.css('color', '#facd00');
      $subMenu.addClass('active').css('display', 'block');
    } else {
      $title.css('color', 'inherit');
      $subMenu.removeClass('active').css('display', 'none');
    }
  });

  /* Match height of Bootstrap columns in row */
  var _matchHeight = function (selector) {
    $(selector).css('height', '');
    var height = Math.max.apply(null,
      $(selector).map(function(){
        return $(this).outerHeight();
      })
    );
    $(selector).css('height', height);
  };

  var matchHeight = function () {
    _matchHeight('#id-buy-dropdown .left > div:first-child');
    _matchHeight('#id-buy-dropdown .left');
  };

  $(window).resize(matchHeight);
  /* End Match height of Bootstrap columns in row */

  /* Hide / shown dropdown menu when click Buy button */
  var toggleBuyDropdown = function () {
    var modal = $('#id-buy-dropdown');
    var button = $('#id-navlink-buy');
    var win = $(window);

    modal.toggle();
    matchHeight();

    if (modal.is(':visible')) {
      button.removeClass('btn-buy');
      button.addClass('btn-buy-open');
    } else {
      button.removeClass('btn-buy-open');
      button.addClass('btn-buy');
    }

  };
  
  $(window).click(function () {
    $('#id-buy-dropdown').hide();
    $('#id-navlink-buy').removeClass('btn-buy-open');
    $('#id-navlink-buy').addClass('btn-buy');
  });
  $('#id-navlink-buy').click(function (e) {
    e.stopPropagation();
    toggleBuyDropdown();
  });
  $('#id-buy-dropdown').click(function (e){
    e.stopPropagation();
  });
  /* End Hide / shown dropdown menu when click Buy button */

  /* Smoothly scroll main nav */
  $(window).on('scroll touchmove', function () {
    // For homepage only
    if (!$('body').hasClass('inner') && !$("a.open-nav").is(":visible")) {
      var scrollTop = $(document).scrollTop();
      $('#header .navigation').css('top', Math.max(0, 44 - scrollTop));
      $('#header .navigation li .drop').css('top', Math.max(44, 88 - scrollTop));
    }
  });
  /* End Smoothly scroll main nav */
});
