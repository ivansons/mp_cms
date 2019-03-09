/**
* CMS-146: Customer Stories Widget
*/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var pageTitle = "CMS-146: Customer Stories";

var mainTitle1 = "Echo";
var mainText1 = "Hitchu wit a text";
var bgColor = "#0098ff";
var bgColorMainTitle = "#4d4d4d";
var mainCSSClass = "";
var mainCSSStyle = "";

var ttbTitle  = new Array ("Wow", "Major Key Alert");
var ttbText = new Array ("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife", "We are finishing up an interview with the biggest in the game DJ Khaled");
var ctaText = new Array ("Texting", "Honestly");
var ctaLink = new Array ("http://www.google.com", "http://www.yahoo.com");
var customerQuote1 = "Debra Levil and Wedgy Hudlin";
var customerQuote2 = "Uncle Ruckus reality show";
var customerColor1 = "#f6f6f6";
var customerColor2 = "#4d4d4d";
var customerVideo = "https://youtu.be/YQHsXMglC9A";
var titleColor = "#f6f6f6";
var textColor = "#4d4d4d";
var titleSize = "4";

describe("CMS-146: Customer Stories", function () {

  beforeEach(function () {
    // Timing is critical, so let the page catch up before each test
    CMS.wait(1);
  });

  afterEach(function () {
    // do nothing
  });

  it('Needs a new widgy page', function () {
    CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped into the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets customerstories"'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));
    CMS.dragAndDrop(item, target);
    CMS.wait(1);
    expect(element(by.css('[class*="node mp_widgets customerstories"]')).isPresent()).toBe(true);

  });

  it("Has one Customer story slide container", function() {
    var slides = element.all(by.css('[class*="node mp_widgets customerstoryslide"]'));
    expect(slides.count()).toEqual(1);
  });

  it("Has one Customer story video slide container", function() {
    var videos = element.all(by.css('[class*="node mp_widgets customerstoryvideoslide"]'));
    expect(videos.count()).toEqual(1);
  });

  it("Allows editing of the Customer stories container values", function() {
    element.all(by.className('edit')).first().click();
    CMS.wait(1);
    element(by.css('[id$="-background_color"]')).clear().sendKeys(bgColor);
    element(by.css('[id$="-main_title"]')).clear().sendKeys(mainTitle1);
    element(by.css('[id$="-main_title_color"]')).clear().sendKeys(bgColorMainTitle);
    element(by.css('[id$="-css_class"]')).clear().sendKeys(mainCSSClass);
    element(by.css('[id$="-css_style"]')).clear().sendKeys(mainCSSStyle);
    element(by.css('[value="Save"]')).click();
    //browser.driver.actions().sendKeys(protractor.Key.ENTER).perform();
    CMS.wait(1);
  });


  it("Allows editing of the Customer story slide container", function(){
    element(by.css('[class*="node mp_widgets customerstoryslide"]')).all(by.className('edit')).first().click();
    CMS.wait(1);
    element(by.css('[id$="-customer_quote"]')).clear().sendKeys(customerQuote1);
    element(by.css('[id$="-customer_quote_color"]')).clear().sendKeys(customerColor1);
    element(by.css('[value="Save"]')).click();
    CMS.wait(1);

  });


  it("Allows editing of the Customer story video slide container", function(){
    browser.executeScript('arguments[0].scrollIntoView()',element(by.css('[class*="node mp_widgets customerstoryvideoslide"]')).getWebElement());
    element(by.css('[class*="node mp_widgets customerstoryvideoslide"]')).all(by.className('edit')).first().click();
    CMS.wait(1);
    element(by.css('[id$="-customer_quote"]')).clear().sendKeys(customerQuote2);
    element(by.css('[id$="-customer_quote_color"]')).clear().sendKeys(customerColor2);
    element(by.css('[id$="-video"]')).clear().sendKeys(customerVideo);
    CMS.wait(1);
    element(by.css('[value="Save"]')).click();
    CMS.wait(1);
  });

  it("Allows editing of the Title text block containers", function() {
    CMS.align();
    element.all(by.css('[class*="node mp_widgets titletextcta"]')).each(function(element, index) {
      element.all(by.className('edit')).first().click();
      CMS.wait(1);
      element.all(by.css('[id$="-title"]')).first().clear().sendKeys(ttbTitle[index]);
      element.all(by.css('[id$="-title_color"]')).first().clear().sendKeys(titleColor);
      element.all(by.css('[id$="-title_size"]')).first().click().sendKeys(titleSize);
      element.all(by.css('[id$="-text"]')).first().clear().sendKeys(ttbText[index]);
      element.all(by.css('[id$="-text_color"]')).first().clear().sendKeys(textColor);
      element.all(by.css('[value="Save"]')).first().click();
      CMS.wait(1);
    });
  });

  it("Allows editing of the CTA containers", function() {
    element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
      CMS.align();
      element.all(by.className('edit')).first().click();
      CMS.wait(1);
      element.all(by.css('[id$="-text"]')).first().clear().sendKeys(ctaText[index]);
      element.all(by.css('[id$="-url"]')).first().clear().sendKeys(ctaLink[index]);
      element.all(by.css('[value="Save"]')).first().click();
      CMS.wait(1);
    });
  });


  it('Should show edited fields in Preview mode', function() {
    browser.executeScript('$("body").scrollTop(0)');
    element(By.css('[href*="preview-page"]')).click();

    // Switch out to the Preview window
    browser.getAllWindowHandles().then(function(handles) {
      var newWindowHandle = handles[1];
      browser.switchTo().window(newWindowHandle).then(function() {
        CMS.wait(1);
        // Verify the title text block
        element.all(by.css('[class*="image-column-copy"]')).each(function(element, index) {
          expect(element.all(by.css('[style^="color:"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[style^="color:"]')).first().getAttribute("style")).toContain(ttbTitleColor[index]);
          expect(element.all(by.css('[style^="color:"]')).first().getText()).toEqual(ttbTitle[index]);

          expect(element.all(by.css('[class*="module-blurb"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[class*="module-blurb"]')).first().getAttribute("style")).toContain(ttbTextColor[index]);
          expect(element.all(by.css('[class*="module-blurb"]')).first().getText()).toEqual(ttbText[index]);

          expect(element.all(by.css('[class*="w-inline-block new-button"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[class*="w-inline-block new-button"]')).getAttribute("href")).toContain(ctaLink[index]);
          expect(element.all(by.css('[class*="w-inline-block new-button"]')).first().getText()).toContain(ctaText[index]);
        });

        // Close up the Preview window so we're back at the main page
        browser.driver.close().then(function() {
          browser.switchTo().window(handles[0]);
        });
      });
    });
  });

  it('Can be deleted from the Main content section', function() {
		var mainContent = browser.driver.findElement(By.className('maincontent'));
		var widget = mainContent.findElement(By.css('[class*="node mp_widgets customerstories"]'));
		widget.findElement(By.className('delete')).click();

		// Pain in the @ss - there's a popup window
    CMS.wait(1);
		browser.driver.switchTo().alert().accept();
    CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets customerstories"]')).isPresent()).toBe(false);
	});

  it('Delete this page because we are done with it', function() {
		CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});

});
