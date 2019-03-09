/**
 * CMS-147: Drag a Single CTA widget to the Main content of Default layout
 */
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var ctaText1 = "Robocop"
var ctaLink1 = "http://www.google.com"
var pageTitle = "CMS-147: Single CTA widget";

describe("CMS-147: Drag a Single CTA widget tot he Main content of Default layout ", function () {

  it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
  });

  it("Can be dragged and dropped onto the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets singlecta"]'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));

    CMS.dragAndDrop(item, target);
    CMS.wait(1);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

it('CLick on parent edit button', function(){
  element(by.css('[class*="node mp_widgets singlecta"]')).element(by.className('edit')).click();
  CMS.wait(1);
  element(by.css('[value="Save"]')).click();
});

  it('Click on child edit button', function(){
    element(by.css('[class*="node mp_widgets cta"]')).element(by.className('edit')).click();
    CMS.wait(1);
    element(by.css('[id$="-text"]')).clear().sendKeys(ctaText1);
    element(by.css('[id$="-url"]')).clear().sendKeys(ctaLink1);
    element(by.css('[value="Save"]')).click();
  });

  it('Should show edited fields in Preview mode', function() {
    browser.executeScript('window.scrollTo(0,0);').then(function () {
      element(By.css('[href^="/widgy/preview-page"]')).click();
    });

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {
				// Verify the first CTA
				expect(element(by.xpath('//div[contains(text(), "' + ctaText1 + '")]')).isPresent()).toBe(true);
				expect(element(by.xpath('//a[contains(@href, "' + ctaLink1 + '")]')).isPresent()).toBe(true);

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
          CMS.wait(1);
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
