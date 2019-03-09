/***********************************************************************
 * CMS-148: Feature Section Video widget
 ***********************************************************************/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var pageTitle = "CMS-148: Feature Section Video";
var backgroundColor= "#f6f6f6";
var iFrameText = '<iframe src="https://player.vimeo.com/video/88954819?api=1" frameborder="0" seamless allowfullscreen width="918" height="514"></iframe>';
var ttbTitle= "The Unbearable Lightness of Being";
var titleColor= "#00AACC";
var titleSize= "3";
var ttbText= "Will a fan create a full-scale version of the game's city scanner drones?";
var textColor= "#666666";
var ctaText = "Hundred";
var ctaLink = "http://www.yahoo.com";

var expose = function(element) { arguments[0].scrollIntoView(); }

describe("CMS-148: Feature Section Video widget", function () {

  it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped into the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets featuresectionvideo"]'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));
    CMS.dragAndDrop(item, target);
    CMS.wait(1);
    expect(element(by.css('[class*="shelfItem mp_widgets featuresectionvideo"]')).isPresent()).toBe(true);
  });

	it("Feature section parent widget should be editable", function() {
		element(by.css('[class*="node mp_widgets featuresectionvideo"]')).element(by.className('edit')).click();
		CMS.wait(6);
    browser.executeScript(expose, element.all(by.css('[value="Save"]')).first().getWebElement());
		expect(element(by.css('[id$="-background_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_content_is_on_left"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-css_class"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-css_style"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-iframe_tag"]')).isPresent()).toBe(true);


		element(by.css('[id$="-background_color"]')).clear().sendKeys(backgroundColor);
    element(by.css('[id$="-iframe_tag"]')).clear().sendKeys(iFrameText);
		element(by.css('[value="Save"]')).click();
		CMS.wait(1);


	});

	it("Title Text block should be editable", function() {
    var showElement = element(by.css('[class*="node page_builder maincontent"]')).getWebElement();
    browser.executeScript("arguments[0].scrollIntoView();", showElement);
		element(by.css('[class*="node mp_widgets titletextcta"]')).element(by.className('edit')).click();

		CMS.wait(2);
    browser.executeScript(expose, element.all(by.css('[value="Save"]')).first().getWebElement());
		expect(element(by.css('[id$="-title"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-title_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-title_size"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_is_raw_html"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_color"]')).isPresent()).toBe(true);

		 var t = element(by.css('[id$="-title"]'));
		 browser.executeScript(expose, t.getWebElement());
		 t.clear().sendKeys(ttbTitle);

		 var tc = element(by.css('[id$="-title_color"]'));
		 tc.clear().sendKeys(titleColor);

		 var ts = element(by.css('[id$="-text"]'));
		 ts.clear().sendKeys(ttbText);

		 var tt = element(by.css('[id$="-text_color"]'));
		 tt.clear().sendKeys(textColor);

		element.all(by.css('[value="Save"]')).first().click();
		CMS.wait(1);

	});


  it("CTA child widget should have editable text and url", function() {
    element(by.css('[class*="node mp_widgets cta"]')).element(by.className('edit')).click();
    CMS.wait(2);

    // Expect all inputs to be present
    expect(element(by.css('[id$="-text"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-url"]')).isPresent()).toBe(true);

    element(by.css('[id$="-text"]')).clear().sendKeys(ctaText);
    element(by.css('[id$="-url"]')).clear().sendKeys(ctaLink);
    element(by.css('[value="Save"]')).click();
    CMS.wait(1);
  });


  it('Should show edited fields in Preview mode', function() {
    browser.executeScript('window.scrollTo(0,0);');
        //browser.executeScript("arguments[0].scrollIntoView();", element(by.css('[class*="preview"]')).getWebElement());
		browser.driver.findElement(By.className("preview")).click();

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {
				// Verify elements on preview page
        expect(element.all(by.css('[class*="no-flicker"]')).first().isPresent()).toBe(true);
        expect(element.all(by.css('[class*="no-flicker"]')).first().getText()).toEqual(ttbTitle);
        expect(element.all(by.css('[class*="module-blurb"]')).first().isPresent()).toBe(true);
        expect(element.all(by.css('[class*="module-blurb"]')).first().getText()).toEqual(ttbText);
        expect(element.all(by.css('[class*="button-text"]')).first().isPresent()).toBe(true);
        expect(element.all(by.css('[class*="button-text"]')).first().getText()).toEqual(ctaText);

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});

  it('Can be deleted from the Main content section', function() {
    var mainContent = browser.driver.findElement(By.className('maincontent'));
    var widget = mainContent.findElement(By.css('[class*="node mp_widgets featuresectionvideo"]'));
    widget.findElement(By.className('delete')).click();

    browser.driver.switchTo().alert().accept();
    CMS.wait(2);
    expect(element(by.css('[class*="node mp_widgets featuresectionvideo"]')).isPresent()).toBe(false);
  });

  it('The containing Widgy page can be deleted', function(){
    CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual('https://qa2-www-0.matterport.com/admin/logout/');
  });

});
