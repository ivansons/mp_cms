//jQuery(window).load(function($) {
//	jQuery('.logos .logo-list .item img').each(function() {
//		jQuery(this).wrap('<div style="display:inline-block;width:' + this.width + 'px;height:' + this.height + 'px;">').clone().addClass('gotcolors').css({'position': 'absolute', 'opacity' : 0 }).insertBefore(this);
//		this.src = grayscale(this.src);
//	}).animate({opacity: 1}, 500);
//});
jQuery(document).ready(function($){
	var body_ = $('body');

	resultHeight();

	//Greyscale
	$('.logos .logo-list .item').hover(
		function() {
			$(this).find('.gotcolors').stop().animate({opacity: 1}, 200);
		},
		function() {
			$(this).find('.gotcolors').stop().animate({opacity: 0}, 500);
		}
	);

	// Page Loader
	$(".animsition").animsition({
    inClass: 'fade-in',
    outClass: 'fade-out',
    inDuration: 1500,
    outDuration: 800,
    linkElement: '.animsition-link',
    // e.g. linkElement: 'a:not([target="_blank"]):not([href^=#])'
    loading: true,
    loadingParentElement: 'body', //animsition wrapper element
    loadingClass: 'animsition-loading',
    loadingInner: '', // e.g '<img src="loading.svg" />'
    timeout: false,
    timeoutCountdown: 5000,
    onLoadEvent: true,
    browser: [ 'animation-duration', '-webkit-animation-duration'],
    // "browser" option allows you to disable the "animsition" in case the css property in the array is not supported by your browser.
    // The default setting is to disable the "animsition" in a browser that does not support "animation-duration".
    overlay : false,
    overlayClass : 'animsition-overlay-slide',
    overlayParentElement : 'body',
    transition: function(url){ window.location.href = url; }
 	});

	// Try It Switching iframe embeds
	$('.model3d1').click(function(e){
          e.preventDefault();
          modelID = $(this).data('model-id');
          $('#player iframe').remove();
          $('#player').append('<iframe width="100%" height="540" src="https://my.matterport.com/show/?m=' + modelID + '&play=1" frameborder="0" allowfullscreen></iframe>');
          $('html, body').animate({scrollTop : 170},1500);
        });

	  $('.model3d1').click(function(e){
	    e.preventDefault();
	    modelID = $(this).data('model-id');
	    $('#emb-code p.emb-code').remove();
	    $('#emb-code').append('<p class="emb-code">&lt;iframe width="853" height="480" src="https://my.matterport.com/show/?m=' + modelID + '" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;</p>');
	  });

	// Toggling between Video BG and Module BG in the banner homepage
	$('#module-btn').click(function() {
		$('.video-background').toggleClass('hidden-video');
		$('.video-background-module').toggleClass('hidden-video');
	});
	$('#module-close').click(function() { 
		$('.video-background-module').addClass('hidden-video');
		$('.video-background').removeClass('hidden-video');
	});
	$('#module-close1').click(function() { 
		$('.video-background-module').addClass('hidden-video');
		$('.video-background').removeClass('hidden-video');
	});

	


	// Binding action to the arrow down button for the hero module 
	$(document).keydown(function(e) {
    switch(e.which) {
        case 40: // down
        $('.video-background-module').addClass('hidden-video');
		$('.video-background').removeClass('hidden-video');
        break;

        default: return; // exit this handler for other keys
    }
    //e.preventDefault(); // prevent the default action (scroll / move caret)
});

	if ( jQuery( "#video-background" ).length ) {
 
    // Cover video home screen 
	jQuery('#video-background').coverVid(1920, 1080);
 
	}
	

	// Try it Embed Code
	  $(".try-it-em").fancybox({
	    maxWidth  : 800,
	    maxHeight : 600,
	    fitToView : false,
	    width   : '70%',
	    height    : '50%',
	    autoSize  : false,
	    closeClick  : false,
	    openEffect  : 'none',
	    closeEffect : 'none'
	  });


	// Space Gallery Embed Code
	  $(".space-embed").fancybox({
	    maxWidth  : 800,
	    maxHeight : 600,
	    fitToView : false,
	    width   : '70%',
	    height    : '50%',
	    autoSize  : false,
	    closeClick  : false,
	    openEffect  : 'none',
	    closeEffect : 'none'
	  });

	// Century 21 Landing Page
    $('#msp-options').change(function(){
         $(this).val() == "la" ? $('#los-angeles').show(100).animate({height: '500px'}, 500) : $('#los-angeles').hide().css('height', '0px');
         $(this).val() == "mi" ? $('#miami').show(100).animate({height: '500px'}, 500) : $('#miami').hide().css('height', '0px');
      });

     $(".msp-contact").fancybox({
        maxWidth  : 800,
        maxHeight : 600,
        fitToView : false,
        width     : '60%',
        height    : '80%',
        autoSize  : false,
        closeClick  : false,
        openEffect  : 'none',
        closeEffect : 'none'
      });

     $(".bring-to-live").fancybox({
     	maxWidth  : 768,
	    maxHeight : 432,
        fitToView : false,
        width     : '80%',
        height    : '60%',
        autoSize  : false,
        closeClick  : false,
        openEffect  : 'none',
        closeEffect : 'none'
      });

     $(".bring-to-live1").fancybox({
     	maxWidth  : 768,
	    maxHeight : 432,
        fitToView : false,
        width     : '80%',
        height    : '60%',
        autoSize  : false,
        closeClick  : false,
        openEffect  : 'none',
        closeEffect : 'none'
      });

     $(".bring-to-live2").fancybox({
        fitToView : false,
        width     : '80%',
        height    : '100%',
        autoSize  : false,
        closeClick  : false,
        openEffect  : 'none',
        closeEffect : 'none'
      });

      $('.page-template-page-century-21 .gform_wrapper input').addClass('form-control'); 

	// Tabs on How it Use - Give active state

	 $('#tabs-camera .nav-tabs li:first-child').addClass('active'); 

	 $('#tabs-camera .tab-content div.tab-pane:first-child').addClass('active in'); 

	  $('#spaces .nav-tabs li:first-child').addClass('active'); 

	 $('#spaces .tab-content div.tab-pane:first-child').addClass('active in'); 

	// Disable scroll iframe map

        // you want to enable the pointer events only on click;

        $('#themap').addClass('scrolloff'); // set the pointer events to none on doc ready
        $('#map-photographers').on('click', function () {
            $('#themap').removeClass('scrolloff'); // set the pointer events true on click
        });

        // you want to disable pointer events when the mouse leave the canvas area;

        $("#map-photographers").mouseleave(function () {
            $('#themap').addClass('scrolloff'); // set the pointer events to none when mouse leaves the map area
        });



	// Main Nav icons

	// How it Works
	$('<i class="fa fa-cogs"></i>').prependTo('#menu-item-4022 a:first-child');

	// Uses / Industries
	$('<i class="fa fa-building"></i>').prependTo('#menu-item-4021 a:first-child');

	// Try it
	$('<i class="fa fa-street-view"></i>').prependTo('#menu-item-5914 a:first-child');

	// Careers
	$('<i class="fa fa-user-plus"></i>').prependTo('#menu-item-6046 a:first-child');

	// Contacts
	$('<i class="fa fa-pencil-square-o"></i>').prependTo('#menu-item-6152 a:first-child');

	// Photography
	$('<i class="fa fa-camera-retro"></i>').prependTo('#menu-item-4020 a:first-child');

	// Gallery
	$('<i class="fa fa-th"></i>').prependTo('#menu-item-6998 a:first-child');

	// Technology
	$('<i class="fa fa-flask"></i>').prependTo('#menu-item-4018 a:first-child');

	// News
	$('<i class="fa fa-newspaper-o"></i>').prependTo('#menu-item-4017 a:first-child');

	// FAQ
	$('<i class="fa fa-question-circle"></i>').prependTo('#menu-item-6260 a:first-child');

	// For the forms
	$('select#country_code').change(function(){

    var countryVal = $('select#country_code').val();

    switch(countryVal){
      
      case "CA":

        $('select#state_code').empty();
        $('select#state_code').append('<option value="AB">Alberta</option><option value="BC">British Columbia</option><option value="MB">Manitoba</option><option value="NB">New Brunswick</option><option value="NL">Newfoundland and Labrador</option><option value="NS">Nova Scotia</option><option value="NT">Northwest Territories</option><option value="NU">Nunavut</option><option value="ON">Ontario</option><option value="PE">Prince Edward Island</option><option value="QC">Quebec</option><option value="SK">Saskatchewan</option><option value="YT">Yukon Territories</option>');

      break;
      
      case "US":

        $('select#state_code').empty();
        $('select#state_code').append('<option value="">Choose a State</option><option value="AL">Alabama</option><option value="AK">Alaska</option><option value="AZ">Arizona</option><option value="AR">Arkansas</option><option value="CA">California</option><option value="CO">Colorado</option><option value="CT">Connecticut</option><option value="DE">Delaware</option><option value="DC">District Of Columbia</option><option value="FL">Florida</option><option value="GA">Georgia</option><option value="HI">Hawaii</option><option value="ID">Idaho</option><option value="IL">Illinois</option><option value="IN">Indiana</option><option value="IA">Iowa</option><option value="KS">Kansas</option><option value="KY">Kentucky</option><option value="LA">Louisiana</option><option value="ME">Maine</option><option value="MD">Maryland</option><option value="MA">Massachusetts</option><option value="MI">Michigan</option><option value="MN">Minnesota</option><option value="MS">Mississippi</option><option value="MO">Missouri</option><option value="MT">Montana</option><option value="NE">Nebraska</option><option value="NV">Nevada</option><option value="NH">New Hampshire</option><option value="NJ">New Jersey</option><option value="NM">New Mexico</option><option value="NY">New York</option><option value="NC">North Carolina</option><option value="ND">North Dakota</option><option value="OH">Ohio</option><option value="OK">Oklahoma</option><option value="OR">Oregon</option><option value="PA">Pennsylvania</option><option value="RI">Rhode Island</option><option value="SC">South Carolina</option><option value="SD">South Dakota</option><option value="TN">Tennessee</option><option value="TX">Texas</option><option value="UT">Utah</option><option value="VT">Vermont</option><option value="VA">Virginia</option><option value="WA">Washington</option><option value="WV">West Virginia</option><option value="WI">Wisconsin</option><option value="WY">Wyoming</option>');

      break;
      
      case "AU":

        $('select#state_code').empty();
        $('select#state_code').append('<option value="ACT">Australian Capital Territory</option><option value="NSW">New South Wales</option><option value="NT">Northern Territory</option><option value="QLD">Queensland</option><option value="SA">South Australia</option><option value="TAS">Tasmania</option><option value="VIC">Victoria</option><option value="WA">Western Australia</option>');

      break;
      

      $('select#state_code').removeAttr('disabled');
    }

    if(countryVal !== "US" && countryVal !== "CA" && countryVal !== "AU"){
      $('select#state_code').empty();
      $('select#state_code').append('<option value="">Choose a State/Province</option>');
      $('select#state_code').attr('disabled','disabled');
    }else{
      $('select#state_code').removeAttr('disabled');
      $('select#state_code').attr('required', true);
    }

  });

	// end of forms

	// Gallery accordation update 

	var hashstring = window.location.hash.substr(1);
  if(jQuery('#filter-3d-models').hasClass('wp3d-models-clearfix')){
       if(hashstring == 'arts-entertainment') {
         hashstring = 'Arts & Entertainment';
       } else if (hashstring == 'restaurants-bars') {
         hashstring = 'Restaurants & Bars';
       } else if (hashstring == 'travel-and-leisure') {
         hashstring = 'Travel & Leisure';
       } else if (hashstring == 'real-estate') {
         hashstring = 'Real Estate';
       } else if (hashstring === '') {
         hashstring = 'All';
       }
  jQuery('#filter-3d-models .drop-btn').html(hashstring);
  }


	// end of gallery accordation

	/* Changes */
	$('.arrow-down').click(function(e){
		var href = $(this).attr("href"),
		offsetTop = href === "#" ? 0 : $(href).offset().top;
		$('html, body').stop().animate({ 
		scrollTop: offsetTop 
		}, 600);
		e.preventDefault();
	});
	$('.arrow-down1').click(function(e){
		var href = $(this).attr("href"),
		offsetTop = href === "#" ? 0 : $(href).offset().top;
		$('html, body').stop().animate({ 
		scrollTop: offsetTop 
		}, 600);
		e.preventDefault();
	});

	$('.arrow-down11').click(function(e){
		var href = $(this).attr("href"),
		offsetTop = href === "#" ? 0 : $(href).offset().top -100;
		$('html, body').stop().animate({ 
		scrollTop: offsetTop 
		}, 600);
		e.preventDefault();
	});

	$('.slider').slick({
		arrows: false,
		dots: true,
		autoplay: true,
		autoplaySpeed: 5000
	});

	$('.slideshow').slick({
		dots: true,
		autoplay: true,
		fade: true,
		autoplaySpeed: 5000
	});

	$('[placeholder]').textPlaceholder();

	//$('.visual, .life-mages, .testimonials, .list-classes li, .list-possibilities .holder, .space-age, .vr, .capture, .wins-cols .image, .top-section, .statistics, .slideshow .slide .left, .perspective-list li a, .options-box').each(function() {
	//	$(this).css('background-image', 'url(' + $(this).find('> img').attr('src') + ')').find('> img').hide();
	//});

	$('.appear').each(function() {
		$(this).appear();
	});

	$(document.body).on('appear', '.appear', function() {
		$(this).addClass('appeared');
	});

	function mapInitialize(map_) {
		var coords_ = $('#'+ map_).data('coords');
			if (coords_){
				var latitude = coords_.split(',')[0];
				var longtitude = coords_.split(',')[1];
			}
		
		var latlng = new google.maps.LatLng(latitude,longtitude);
		
		var myOptions = {
			zoom: 9,
			center: latlng,
			disableDefaultUI: true,
			scrollwheel: false,
			zoomControl: true,
			disableDefaultUI: true,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
		
		var map = new google.maps.Map(document.getElementById(map_), myOptions);
		
		var marker = new google.maps.Marker({
			position: latlng,
			map: map
		});
	
	}
	$('.map').each(function(){
		var map_ = $(this).attr('id');
		mapInitialize(map_);
	});

});

jQuery(window).resize(function(){
	resultHeight();
});

jQuery(window).load(function() {
	resultHeight();
});

function resultHeight () {
	var height_ = jQuery(window).height();
	jQuery('.visual').css('height', height_ -55);
	if (jQuery('.visual').length) {
		jQuery('#wrapper').css('padding-top', height_);
	};
};

// Single Gallery height 
jQuery(window).resize(function(){
	resultHeightModel();
});

jQuery(window).load(function() {
	resultHeightModel();
});

function resultHeightModel () {
	var height1_ = jQuery(window).height();
	jQuery('.gallery-single').css('height', height1_ - 165);
};


// Jobs Positions 
// Replace "leverdemo" with your own company name
url = 'https://api.lever.co/v0/postings/matterport?group=team&mode=json'

//Functions for checking if the variable is unspecified
function cleanString(string) {
  if (string) {
    var cleanString = string.replace(/[^A-Z0-9]+/ig, "");
    return cleanString;
  } else {
    return "Uncategorized";
  }
}

function nullCheck(string) {
  if (!string) {
    var result = 'Uncategorized'
    return result;
  } else {
    return string;
  }
}

function createJobs(_data) {
  for (i = 0; i < _data.length; i++) {

    var team = nullCheck(_data[i].title)
    var teamCleanString = cleanString(team);
    jQuery('#jobs-container .jobs-teams').append(
      '<a href="#" class="btn ' + teamCleanString + '">' + team + '</a>'
    );
  }

  for (i = 0; i < _data.length; i++) {
    for (j = 0; j < _data[i].postings.length; j++) {
      var posting = _data[i].postings[j]
      var title = posting.text
      var description = posting.description
      //Making each job description shorter than 250 characters
      var shortDescription = jQuery.trim(description).substring(0, 250)
        .replace('\n', ' ') + "...";
      var location = nullCheck(posting.categories.location);
      var locationCleanString = cleanString(location);
      var commitment = nullCheck(posting.categories.commitment);
      var commitmentCleanString = cleanString(commitment);
      var team = nullCheck(posting.categories.team);
      var teamCleanString = cleanString(team);
      var link = posting.hostedUrl;

      jQuery('#jobs-container .jobs-list').append(
        '<div class="job ' + teamCleanString + ' ' + locationCleanString + ' ' + commitmentCleanString + '">' +
        //'<a class="btn" href="' + link + '">Learn more</a>' +
        '<a class="job-title" href="' + link + '"">' + title + '</a>' +

        //  fancy box version  '<a class="job-title fancybox" data-fancybox-type="iframe" href="' + link + '"">' + title + '</a>' +
        //'<p class="tags"><span>' + team + '</span><span>' + location + '</span><span>' + commitment + '</span></p>' +
        //'<p class="description">' + shortDescription + '</p>' +        
        '</div>'

      );
    }
  }
}

//Creating filter buttons for sorting your jobs
function activateButtons(_data) {
  jQuery('.jobs-teams').on("click", "a", function(e) {
    e.preventDefault();
    for (i = 0; i < _data.length; i++) {
      var teamRaw = _data[i].title;
      var team = cleanString(teamRaw);
      var jobs = jQuery(".jobs-list");
      if (jQuery(this).hasClass(team)) {
        if (jQuery(this).hasClass("active")) {
          jQuery(this).removeClass("active");
          jobs.find(".job").fadeIn("fast");
        } else {
          jQuery(".jobs-teams").find("a").removeClass("active");
          jQuery(this).addClass("active");
          jobs.find("." + team).fadeIn("fast");
          jobs.find(".job").not("." + team).fadeOut("fast");
        }
      }
    }
  })
}

//Fetching job postings from Lever's postings API
jQuery.ajax({
  dataType: "json",
  url: url,
  success: function(data) {
    createJobs(data);
    activateButtons(data);
  }
});

function thankYouMessage(){

  alert("Thank you for your submission!");

}
