/**
* CMS-152: Drag a Title Text Block widget to the Main content of Default layout
*/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var pageTitle = "CMS-152: Title Text Block";
var ttbTitle  = "Wow";
var ttbText = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife";
var ctaText = "Texting";
var ctaLink = "http://www.google.com";
var titleColor = "#f6f6f6";
var textColor = "#4d4d4d";
var titleSize = "4";
var pageTitle = "CMS-152: Title text block widget";

describe("CMS-152: Title Text Block widget", function () {

  it('Needs a new widgy page', function () {
    CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped into the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets titletextcta"]'));
		var target = element(by.className('maincontent'));

		CMS.dragAndDrop(item, target);
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets titletextcta"]')).isPresent()).toBe(true);
  });

  it("Allows editing of the Title Text Blocks", function() {
    CMS.align();
    element.all(by.css('[class*="node mp_widgets titletextcta"]')).each(function(element, index) {
      element.all(by.className('edit')).first().click();
      element.all(by.css('[id$="-title"]')).first().clear().sendKeys(ttbTitle);
      element.all(by.css('[id$="-title_color"]')).first().clear().sendKeys(titleColor);
      element.all(by.css('[id$="-title_size"]')).first().click().sendKeys(titleSize);
      element.all(by.css('[id$="-text"]')).first().clear().sendKeys(ttbText);
      element.all(by.css('[id$="-text_color"]')).first().clear().sendKeys(textColor);
      element.all(by.css('[value="Save"]')).first().click();
      CMS.wait(1);
    });
  });

  it("Allows editing of the CTA blocks", function() {
    element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
      element.all(by.className('edit')).first().click();
      CMS.wait(1);
      element.all(by.css('[id$="-text"]')).first().clear().sendKeys(ctaText);
      element.all(by.css('[id$="-url"]')).first().clear().sendKeys(ctaLink);
      element.all(by.css('[value="Save"]')).first().click();
      CMS.wait(1);
    });
  });

  it('Should show edited fields in Preview mode', function() {
    browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		});
    
    // Switch out to the Preview window
    browser.getAllWindowHandles().then(function(handles) {
      var newWindowHandle = handles[1];
      browser.switchTo().window(newWindowHandle).then(function() {

        // Verify the title text block
        element.all(by.css('[class*="image-column-copy"]')).each(function(element, index) {
          expect(element.all(by.css('[style^="color:"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[style^="color:"]')).first().getAttribute("style")).toContain(ttbTitleColor[index]);
          expect(element.all(by.css('[style^="color:"]')).first().getText()).toEqual(ttbTitle);

          expect(element.all(by.css('[class*="module-blurb"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[class*="module-blurb"]')).first().getAttribute("style")).toContain(ttbTextColor[index]);
          expect(element.all(by.css('[class*="module-blurb"]')).first().getText()).toEqual(ttbText);

          expect(element.all(by.css('[class*="w-inline-block new-button"]')).first().isPresent()).toBe(true);
          // expect(element.all(by.css('[class*="w-inline-block new-button"]')).getAttribute("href")).toContain(ctaLink[index]);
          expect(element.all(by.css('[class*="w-inline-block new-button"]')).first().getText()).toContain(ctaText);
        });

        // Close up the Preview window so we're back at the main page
        browser.driver.close().then(function() {
          browser.switchTo().window(handles[0]);
        });
      });
    });
  });

  it('Delete this page because we are done with it', function() {
    CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
  });
});
