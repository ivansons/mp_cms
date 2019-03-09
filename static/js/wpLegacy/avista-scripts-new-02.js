jQuery(document).ready(function($){

	$('.wins.real-estate-w .wins-cols .image,.info-gallery .slide, .showcase-section .video, .visual-block .frame, .visual-intro, .price-section').each(function() {
		$(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')');
	});

	$('.info-gallery').slick({
		fade: true,
		slide: '.slide'
	});

	$('.price-section li strong.price.annual').hide();

	$('.price-section .btn.annual').click(function(e) {
		$('.price-section .btn.annual').addClass('active');
		$('.price-section .btn.monthly').removeClass('active');
		$('.price-section li strong.price.month').hide();
		$('.price-section li strong.price.annual').show();
		e.preventDefault();
	});
	$('.price-section .btn.monthly').click(function(e) {
		$('.price-section .btn.monthly').addClass('active');
		$('.price-section .btn.annual').removeClass('active');
		$('.price-section li strong.price.annual').hide();
		$('.price-section li strong.price.month').show();
		e.preventDefault();
	});

	$('body.page-template-page-realestate-solution, body.page-template-page-realestate-photographer, body.page-template-page-realestate-brokerages,body.page-template-page-realestate-agent,body.page-template-page-realestate-customers, body.page-template-page-realestate-pricing, body.page-template-page-realestate-easy-3, body.page-template-page-realestate-easy-1, body.page-template-page-realestate-easy-2').addClass('inner-page real-estate');

	$('.info-gallery .slide, .visual-intro').css('height', $(window).height());

	$('.info-gallery .more-link').click(function(e){
		var offsetTop = $('.info-gallery').next().offset().top - $('#header').outerHeight();
		$('html, body').stop().animate({
			scrollTop: offsetTop
		}, 300);
		e.preventDefault();
	});

	$('.visual-intro .more-link').click(function(e){
		var offsetTop = $('.visual-intro').next().offset().top - $('#header').outerHeight();
		$('html, body').stop().animate({
			scrollTop: offsetTop
		}, 300);
		e.preventDefault();
	});

});

jQuery(window).resize(function(){
	jQuery('.info-gallery .slide, .visual-intro').css('height', jQuery(window).height());
});
