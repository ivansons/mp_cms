/**
* CMS-nnn: [description of the tests - typically includes the widget name]
*/

/**************************************************************************
This section contains run-level stuff, so please don't modify it
***************************************************************************/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

/**************************************************************************
This section contains your test 'specs'
There should be one top-level 'describe' section and any number of
'it' descriptions, each of which is a test spec.
***************************************************************************/

var pageTitle = "CMS-nnn: Name of widget being tested";

describe("CMS-nnn: [widget name]", function () {

	beforeEach(function () {
		// Timing is critical, so let the page catch up before each test
		CMS.wait(1);
	});

	afterEach(function () {
		// We don't really have any cleanup after each test
	});

	it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
		expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

	it("Can be dragged and dropped into the Main content area", function() {
		//---> var item = element(by.css('[class*="shelfItem mp_widgets [twoupoverlay]"]'));
		var target = element(by.className('maincontent'));

		CMS.dragAndDrop(item, target);
		CMS.wait(2);
		//---> expect(element(by.css('[class*="node mp_widgets [twoupoverlay]"]')).isPresent()).toBe(true);
	});

	//---------------------------------------------------------------
	// Now you've got a new page, with a new widget to test!
	// See what you can do with it!
	//---------------------------------------------------------------








	//---------------------------------------------------------------
	// The last thing we want to do is remove the test page
	// Note: You *must* use the exact text you used to create it!
	//---------------------------------------------------------------

	it('Edited values are present in Preview mode', function() {
		browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		})

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {
				CMS.wait(1);


				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});

	it('Can be deleted', function() {
		var mainContent = browser.driver.findElement(By.className('maincontent'));
		//---> var twoUp = mainContent.findElement(By.className('[twoupoverlay]'));
		//twoUp.findElement(By.className('delete')).click();

		// Handle the popup notification
		CMS.wait(1);
		browser.driver.switchTo().alert().accept();
		CMS.wait(1);
		//---> expect(element(by.css('[class*="node mp_widgets [twoupoverlay]"]')).isPresent()).toBe(false);
	});

	it('Has its Widgey page deleted at the end of the test', function() {
		CMS.removePage(pageTitle);
		CMS.wait(1);
		expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
