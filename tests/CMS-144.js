/***********************************************************************
 * CMS-144: CTA widget
 ***********************************************************************/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var ctaText = "Superfluous";
var ctaLink = "http://www.xyzsuperfluous.com";

var pageTitle = "CMS-144: CTA widget";

describe("CMS-144: CTA widget", function () {

  it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped into the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets cta"]'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));
    CMS.dragAndDrop(item, target);
    CMS.wait(1);
    expect(element(by.css('[class*="node mp_widgets cta"]')).isPresent()).toBe(true);
  });

  it("Should have editable text and url", function() {
    element.all(by.className('edit')).first().click();
    CMS.align();
    CMS.wait(1);

    // Expect all inputs to be present
    expect(element(by.css('[id$="-text"]')).isPresent()).toBe(true);
    expect(element(by.css('[id$="-url"]')).isPresent()).toBe(true);

    element(by.css('[id$="-text"]')).clear().sendKeys(ctaText);
    element(by.css('[id$="-url"]')).clear().sendKeys(ctaLink);
    element(by.css('[value="Save"]')).click();
    CMS.wait(1);
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
				expect(element(by.xpath('//div[contains(text(), "' + ctaText + '")]')).isPresent()).toBe(true);
				expect(element(by.xpath('//a[contains(@href, "' + ctaLink + '")]')).isPresent()).toBe(true);

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});

  it('Can be deleted from the Main content section', function() {
    var mainContent = browser.driver.findElement(By.className('maincontent'));
    var widget = mainContent.findElement(By.css('[class*="node mp_widgets cta"]'));
    widget.findElement(By.className('delete')).click();

    // Pain in the @ss - there's a popup window
    CMS.wait(1);
    browser.driver.switchTo().alert().accept();
    CMS.wait(1);
    expect(element(by.css('[class*="node mp_widgets cta"]')).isPresent()).toBe(false);
  });

  it('The containing Widgy page can be deleted', function(){
    CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
  });

});
