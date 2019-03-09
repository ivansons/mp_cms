/*******************************************************
 * CMS-134: 3 CTA widget
 *******************************************************/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

// Create arrays for CTA Text and CTA Links
var ctaText = new Array("Texting", "Amiibo", "Wolf Gang");
var ctaLink = new Array("http://www.xyztexting.com", "http://www.xyzamiibo.com", "http://www.xyzwolfgang.com");

var pageTitle = "CMS-134: 3 CTA";

describe("CMS-134: 3 CTA widget", function () {

  beforeEach(function () {
    // Timing is critical, so let the page catch up before each test
    CMS.wait(1);
  });

  afterEach(function () {
    // We don't really have any cleanup after each test
  });

  it('Needs a new widgy page for testing', function () {
		CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped into the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets threecta"'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));

    CMS.dragAndDrop(item, target);
    expect(element(by.css('[class*="node mp_widgets threecta"]')).isPresent()).toBe(true);
  });

  it("Allows CTA text and links to be edited", function() {
    element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
      CMS.align();
      element.all(by.className('edit')).first().click();
      CMS.wait(1);

      // Expect the input fields to be present
      expect(element.element(by.css('[id$="-text"]')).isPresent()).toBe(true);
      expect(element.element(by.css('[id$="-url"]')).isPresent()).toBe(true);

      element.element(by.css('[id$="-text"]')).clear().sendKeys(ctaText[index]);
      element.element(by.css('[id$="-url"]')).clear().sendKeys(ctaLink[index]);

      element.all(by.css('[value="Save"]')).first().click();
      CMS.wait(1);
    });
  });

  it('Edited values appear in Preview mode', function() {
    // Scroll to the top of the page and click the Preview button
    browser.executeScript('window.scrollTo(0,0);').then(function () {
      browser.driver.findElement(By.className("preview")).click();
    });

    // Switch out to the Preview window
    browser.getAllWindowHandles().then(function(handles) {
      var newWindowHandle = handles[1];
      browser.switchTo().window(newWindowHandle).then(function() {

        // Verify the 3 CTA text labels
        element.all(by.css('[class="button-text"]')).each(function(element, index) {
          browser.executeScript('arguments[0].scrollIntoView()', element.getWebElement());
          expect(element.getText()).toBe(ctaText[index]);
        });

        // Verify the 3 CTA links
        element.all(by.css('[class="w-inline-block new-button"]')).each(function(element, index) {
          browser.executeScript('arguments[0].scrollIntoView()', element.getWebElement());
          expect(element.getAttribute('href')).toContain(ctaLink[index]);
        });
      });

      // Close up the Preview window so we're back at the main page
      browser.driver.close().then(function() {
        browser.switchTo().window(handles[0]);
      });
    });
  });

  it('The Widgey page is deleted at the end of this test', function(){
    // console.log('Deleting the page');
    CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
  });

});
