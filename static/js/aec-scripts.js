jQuery(document).ready(function ($) {
  $('.video-bg, .industries-list li, .explore-space, .getting-started .list-classes .holder').each(function() {
    $(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')').find('> img').hide();
  });

  $('.banner, .works-list li').each(function() {
    $(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')');
  });

  $('.contact-block').css('background-image', 'url(' + $('.contact-block').find('.bg-img').attr('src') + ')');

  $('.wins.real-estate-w .wins-cols .image,.info-gallery .slide, .showcase-section .video, .visual-block .frame, .visual-intro, .price-section').each(function() {
    $(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')');
  });
});
