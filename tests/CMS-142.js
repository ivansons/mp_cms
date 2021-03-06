/**
 * CMS-142: Drag a 3-Up Overlay widget to the Main content of Default layout
 */
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var pageTitle = "CMS-142: 3-Up Overlay";
var mainTitle1 = "Tain Mitle";
var mainText1 = "Hitchu wit a text";
var bgColor = "#0098ff";
var bgColorMainTitle = "#4d4d4d";
var bgColorMainText = "#d1d3d4";
var mainTitleSize = "1";
var mainTextAlign = "R";
var childTitle  = new Array ("Wow", "LOL", "Benny Camer");
var childText = new Array ("If you smell what the Vince is cooking", "I cannot tell a lie", "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife");
var ctaText = new Array ("Texting", "Amiibo", "Wolf Gang");
var ctaLink = new Array ("http://www.google.com", "https://www.yahoo.com/", "http://www.aol.com/");
var titleColor = "#f6f6f6";
var textColor = "#4d4d4d";
var titleSize = "4";

describe("CMS-142: 3-up Overlay", function () {

  it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped onto the main content area", function() {
    //console.log("Drag and drop a 3-Up Overlay widget");
    var item = element(by.css('[class*="shelfItem mp_widgets threeupoverlay"]'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));

    CMS.dragAndDrop(item, target);
    CMS.wait(1);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Allows editing of the Main title and text", function() {
    //console.log("Edit 3-Up Overlay widget");
    element(by.css('[class*="node mp_widgets threeupoverlay"]')).all(by.className('edit')).first().click();
    CMS.align();
    CMS.wait(1);

    // Expect to find all inputs are present
    expect(element(by.css('[id$="-background_color"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-main_title"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-main_title_color"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-main_text"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-main_text_color"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-main_title_size"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-text_align"]')).isPresent()).toBe(true);

    element(by.css('[id$="-background_color"]')).clear().sendKeys(bgColor);
    element(by.css('[id$="-main_title"]')).clear().sendKeys(mainTitle1);

    element(by.css('[id$="-main_title_color"]')).clear().sendKeys(bgColorMainTitle);
    element(by.css('[id$="-main_text"]')).clear().sendKeys(mainText1);

    element(by.css('[id$="-main_text_color"]')).clear().sendKeys(bgColorMainText);
    element(by.css('[id$="-main_title_size"]')).click().sendKeys(mainTitleSize);
    element(by.css('[id$="-text_align"]')).click().sendKeys(mainTextAlign);

    element(by.css('[value="Save"]')).click();
    CMS.wait(1);
  });

  it("Allows the Title text blocks to be edited", function() {
    //console.log ("editing title text blocks");
    element.all(by.css('[class*="node mp_widgets titletextcta"]')).each(function(element, index) {
      element.all(by.className('edit')).first().click();
      CMS.align();
      CMS.wait(1);

      // Expect all input fields are present
      expect(element.element(by.css('[id$="-title"]')).isPresent()).toBe(true);
      expect(element.element(by.css('[id$="-title_color"]')).isPresent()).toBe(true);
      expect(element.element(by.css('[id$="-title_size"]')).isPresent()).toBe(true);
      expect(element.element(by.css('[id$="-text"]')).isPresent()).toBe(true);
      expect(element.element(by.css('[id$="-text_color"]')).isPresent()).toBe(true);

      element.element(by.css('[id$="-title"]')).clear().sendKeys(childTitle[index]);
      element.element(by.css('[id$="-title_color"]')).clear().sendKeys(titleColor);
      element.element(by.css('[id$="-title_size"]')).click().sendKeys(titleSize);

      element.element(by.css('[id$="-text"]')).clear().sendKeys(childText[index]);
      element.element(by.css('[id$="-text_color"]')).clear().sendKeys(textColor);

      element.element(by.css('[value="Save"]')).click();
      CMS.wait(1);
    });
  });

  it("Allows editing of the CTA blocks", function() {
    // console.log ("editing CTAs");
    element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
      element.all(by.className('edit')).first().click();
      CMS.align();
      CMS.wait(1);

      // Expect all input fields to be present
      expect(element.element(by.css('[id$="-text"]')).isPresent()).toBe(true);
      expect(element.element(by.css('[id$="-url"]')).isPresent()).toBe(true);

      element.element(by.css('[id$="-text"]')).clear().sendKeys(ctaText[index]);
      element.element(by.css('[id$="-url"]')).clear().sendKeys(ctaLink[index]);

      element.element(by.css('[value="Save"]')).click();
      CMS.wait(1);
    });
  });

  it('Should show edited fields in Preview mode', function() {
    // console.log("Verifying from the Preview window");

    browser.executeScript('window.scrollTo(0,0);').then(function () {
      element(By.css('[href^="/widgy/preview-page"]')).click();
    });

    // Switch out to the Preview window
    browser.getAllWindowHandles().then(function(handles) {
      var newWindowHandle = handles[1];
      browser.switchTo().window(newWindowHandle).then(function() {

        // Verify the intro block
        var header = element(by.css('[class*="w-container module-intro-container"]'));
        expect(header.element(by.css('[style^="color:"]')).isPresent()).toBe(true);
        // expect(header.element(by.css('[style^="color:"]')).getAttribute("style")).toContain(mainTextColor);
        expect(header.element(by.css('[style^="color:"]')).getText()).toEqual(mainTitle1);
        expect(header.element(by.className("module-intro")).isPresent()).toBe(true);
        expect(header.element(by.className("module-intro")).getText()).toEqual(mainText1);

        // Verify the two image blocks
        element.all(by.css('[class*="image-column-copy"]')).each(function(element, index) {
          expect(element.all(by.css('[style^="color:"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[style^="color:"]')).first().getAttribute("style")).toContain(ttbTitleColor[index]);
          expect(element.all(by.css('[style^="color:"]')).first().getText()).toEqual(childTitle[index]);

          expect(element.all(by.css('[class*="module-blurb"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[class*="module-blurb"]')).first().getAttribute("style")).toContain(ttbTextColor[index]);
          expect(element.all(by.css('[class*="module-blurb"]')).first().getText()).toEqual(childText[index]);

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
		var widget = mainContent.findElement(By.css('[class*="node mp_widgets threeupoverlay"]'));
		widget.findElement(By.className('delete')).click();

		// Pain in the @ss - there's a popup window
		browser.driver.switchTo().alert().accept();
    CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets threeupoverlay"]')).isPresent()).toBe(false);
	});

  it('Delete the page when we are done', function(){
    CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
  });
});
