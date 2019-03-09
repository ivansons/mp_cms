jQuery(document).ready(function($){
	var body_ = $('body');

	var wow = new WOW(
	  {
	    boxClass:     'move',  
	    animateClass: 'animated', 
	    offset:       0,          
	    mobile:       false,       
	    live:         true,       
	  }
	);
	wow.init();

	$('.video-bg, .industries-list li, .explore-space, .getting-started .list-classes .holder').each(function() {
		$(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')').find('> img').hide();
	});

	$('.nav-bar .top .search-opener').click(function() {
		$(this).parent('.search').addClass('opened');
		$('.search input#s').focus();
		return false;
	});
	$('body').click(function() {
		$('.nav-bar .top .search.opened').removeClass('opened');
		$('.nav-bar .top .search.opened input#s').addClass('opened');
	 });

	$(".navigation li").has(".drop").addClass("has-drop");
	$('<span class="fader"/>').appendTo('#header');
	$('.open-nav').click(function(){
		body_.toggleClass('nav-opened');
		return false;
	});
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


