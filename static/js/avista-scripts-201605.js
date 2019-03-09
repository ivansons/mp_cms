jQuery(document).ready(function($){
	var body_ = $('body');

	$('.video-bg, .industries-list li, .explore-space, .getting-started .list-classes .holder').each(function() {
		$(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')').find('> img').hide();
	});

	$('.nav-bar .top .search-opener').click(function() {
		$(this).parent('.search').addClass('opened');
		return false;
	});

	$(".navigation li").has(".drop").addClass("has-drop");
	$('<span class="fader"/>').appendTo('#header');
	
	$('.fader').click(function(){
		body_.removeClass('nav-opened');
	});
	$('.close-nav').click(function() {
		body_.removeClass('nav-opened');
		return false;
	});

	$(window).on("scroll touchmove", function () {
		$('#header').toggleClass('scrolled', $(document).scrollTop() > 100);
	});

});
