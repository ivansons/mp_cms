$(function() {
  // auto increase textarea height
  autosize($('textarea'));

  // validate spaces' url
  $('#id_sids').change(function () {
    var i, url, uri, query;
    var errorMsgs = [];
    var errors = {
      notHTTPS: false,
      notMatterport: false,
      noSIDFound: false,
      exceededError: false
    };
    var self = $(this);
    var s = self.val();
    var urls = s.split('\n');
    var validURLs = [];
    for (i=0; i<urls.length; i++) {
      // validate urls
      url = urls[i];
      if (!!url.trim()) {
        if (!url.startsWith('https://')) {
          errors.notHTTPS = true;
        }
        uri = new URI(url);
        if (uri.host() != 'my.matterport.com') {
          errors.notMatterport = true;
        }
        query = URI.parseQuery(uri.query());
        if (!query.m) {
          errors.noSIDFound = true;
        }
        if (validURLs.indexOf(url) < 0) {
          validURLs.push(url);
        }
      }
    }
    if (validURLs.length > 70) {
      errors.exceededError = true;
    }
    self.val(validURLs.join('\n'));
    // add error messages according to validation
    if (errors.notHTTPS) {
      errorMsgs.push('Please include only valid URLs that begin with https://');
    }
    if (errors.notMatterport) {
      errorMsgs.push('Please include only my.matterport.com URLs');
    }
    if (errors.noSIDFound) {
      errorMsgs.push('Please include only URLs that have query like ?m=');
    }
    if (errors.exceededError) {
      errorMsgs.push('Please include up to 70 spaces');
    }
    self.siblings('.error-messages').html(
      errorMsgs.map(function (e) {
        return '<li>' + e + '</li>';
      }).join('')
    );
    autosize.update(self);
    updateGenerateButtonStatus();
  });

  // validate starting spaces' url
  $('#id_starting-space').change(function () {
    updateGenerateButtonStatus();
  });

  // click button to generate URL
  $('body').on('click', '#id_btn_generate:not(.invalid)', function () {
    generateURL();
  });

  // update status of generate url button
  var updateGenerateButtonStatus = function () {
    var sids = getSIDs('#id_sids');
    var startingSpace = getSIDs('#id_starting-space');
    var button = $('#id_btn_generate');
    if (sids.length > 0 && sids.length <= 70) {
      if (startingSpace.length < 1 || sids.indexOf(startingSpace[0]) > -1) {
        button.removeClass('invalid');
        $('#id_starting-space').siblings('.error-messages').html('');
        return;
      }
      $('#id_starting-space').siblings('.error-messages').html(
        '<li>' + 'Your starting space has to be in the list of your VR spaces' + '</li>'
      );
    }
    button.addClass('invalid');
  };

  // update status of QR code placeholder
  var updateQRCodeStatus = function () {
    var placeholder = $('#id_qrcode');
    if ($('#id_result p').text()) {
      placeholder.removeClass('hidden');
    } else {
      placeholder.addClass('hidden');
    }
  };

  // get list of SID from input
  var getSIDs = function (selector) {
    var i, url, uri, query;
    var urlListString = $(selector).val();
    var urls = urlListString.split('\n');
    var sids = [];
    for (i=0; i<urls.length; i++) {
      url = urls[i];
      if (!url.trim()) {
        continue;
      }
      uri = new URI(url);
      query = URI.parseQuery(uri.query());
      if (!!query.m && sids.indexOf(query.m) < 0) {
        sids.push(query.m);
      }
    }
    return sids;
  };

  // generate URL
  var generateURL = function () {
    var sids = getSIDs('#id_sids');
    var title = $('#id_title').val() || '';
    var description = $('#id_description').val() || '';
    var startingSpace = getSIDs('#id_starting-space');
    var ret = $('#id_ret').val() || '';
    var deepLink = new URI('https://my.matterport.com/vr/dlist/');
    if (!sids.length > 0) {
      return
    }
    if (title.trim()) {
      deepLink.setQuery('ln', title.trim());
    }
    if (description.trim()) {
      deepLink.setQuery('ld', description.trim());
    }
    if (startingSpace.length > 0) {
      deepLink.setQuery('lsid', startingSpace[0]);
    }
    if (ret.trim()) {
      deepLink.setQuery('ret', ret.trim());
    }
    var extraQuery = deepLink.query() ? '&' + deepLink.query() : '';
    var deepLinkString = 'https://my.matterport.com/vr/dlist/?sids='
      + sids.join(',') + extraQuery;
    $('#id_result p').text(deepLinkString);
    $('#id_qrcode>div:first-child').html('');
    $('#id_qrcode>div:first-child').qrcode({
      background: '#fff',
      text: deepLinkString,
      size: 512,
      quiet: 2
    });
    $('#id_btn_download').attr(
      'href', $('#id_qrcode canvas').get(0).toDataURL('image/png'));
    $('#id_btn_download').attr(
      'download',
      'Matterport-VR-Collection-' + (title.trim() || 'untitled') + '.png');
    updateQRCodeStatus();
  };
});
