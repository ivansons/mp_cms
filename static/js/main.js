WebFont.load({
  google: {
    families: [
      "Open+Sans:400,400i,600,600i,800,800i",
      "Montserrat:400,700",
      "Titillium+Web:200,300,600"
    ]
  }
});

// Fix - Redraw background video when full screen mode exited
$(window).on("webkitfullscreenchange mozfullscreenchange fullscreenchange MSFullscreenChange", function(){
  if (document.webkitIsFullScreen || document.mozFullScreen || document.msFullscreenElement !== null) {
    $('.home-video-bg video').hide().fadeIn('fast');
  }
});

function adjustBuyButtonText() {
  if(window.innerWidth < 480) {
    $('#dropLogin').addClass('hidden');
    if(window.innerWidth <= 320) {
      $('.btn-buy').text('Buy');
    } 
  } else {
    $('.btn-buy').text('Buy');
    $('#dropLogin').removeClass('hidden');
  }
}

$(window).resize(adjustBuyButtonText);

function showLighthouse(lighthouse_id, iframe_div_id, close_button_id, primary_id) {
  $("#primary_id").hide();
  $(".page-cover").css("opacity",0.6).fadeIn(300, function () {
    $("#lighthouse_id").css({'position':'relative','z-index':1000});
    $("#iframe_div_id").firstChild.css({'position':'relative','z-index':1000});
    $("#close_button_id").css({'position':'relative','z-index':1000});
    $("#lighthouse_id").show();
  });
}

function hideLighthouse(lighthouse_id, primary_id, iframe_div_id) {
  //pause vimeo video play
  postIFrame(iframe_div_id,'pause');

  $("#lighthouse_id").hide();
  $("#primary_id").show();
}

function postIFrame(iframe_container_div_id, action, value) {
  var iFram = $("#iframe_container_div_id").firstChild;
  var url = iFram.src.split('?')[0];
  var data = { method: action };
  if (value) {
    data.value = value;
  }
  if(url !== undefined){
    iFram.contentWindow.postMessage(JSON.stringify(data), url);
  }
}

// Adjusted hash scrolling needed to prevent navigation blocking content
(function($, window) {
  //determine height of the header for offset
  var header_height = $("#header").height();

  //Scroll to a hashed anchor location on the current page
  $('a[href*=\\#]:not([href=\\#])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '')
        && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length && target.is(':visible')) {
        $('html,body').animate({
          scrollTop: target.offset().top - header_height
        }, 500);
        return false;
      }
    }
  });

  //Scroll to a location on window load
  $(window).on('load', function() {
    var $anchor = $(':target');
    if ($anchor.length > 0) {
      $('html, body').stop().animate({
        scrollTop: $anchor.offset().top - header_height
      }, 500);
    }
  });

  adjustBuyButtonText()
})(jQuery, window);
