$(function() {
  /* Popup subscription form */
  $(".popup-subscription-form").fancybox({
    //width: '85%',
    //maxWidth: 640,
    autoSize: true,
    autoHeight: true,
    closeClick: false,
    fitToView: false,
    openEffect: 'fade',
    closeEffect: 'none',
    afterClose: function () {
      setHidePopUpCookie();
    }
  });

  // If users close pop up window, the light box will not show in 3 days.
  function setHidePopUpCookie () {
    var mc_popup_hide = Cookies.get('mc_popup_hide');
    if (!mc_popup_hide) {
      Cookies.set('mc_popup_hide', true, {
        expires: 3
      });
    }
  }

  /* Only display pop up subscription form if:
       1. the user is not a subscriber.
       2. the user didn't close the pop up windows in recent 3 days.
   */
  function showPopupForm () {
    var mc_popup_hide = Cookies.get('mc_popup_hide');
    var mc_subscribed = Cookies.get('mc_subscribed');
    if (!mc_popup_hide && !mc_subscribed) {
      $(".popup-subscription-form").click();
    }
  }

  // Show pop up subscription form in 3 seconds after the page is loaded.
  setTimeout(showPopupForm, 5000);

  /* Once users hit `subscribe` button, mark the users as our
     subscribers and not showing the pop up window again.
   */
  $("#mc-popup-subscribe").click(function (e) {
    e.preventDefault();
    var emailInput = $("#mcp-EMAIL");
    var email = emailInput.val().trim();
    if (!email) {
      emailInput.addClass("error");
    } else {
      emailInput.removeClass("error");
      Cookies.set('mc_subscribed', true);
      $("#mc-popup-subscribe-form").submit();
    }
  });
});
