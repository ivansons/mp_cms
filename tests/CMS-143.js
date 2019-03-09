/**
* CMS-143: 6-Up
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
var bgColor = "#0098ff";
var bgColorMainTitle = "#4d4d4d";
var bgColorMainText = "#d1d3d4";
var mainTitle = "Seriously Cranked";
var mainText = "Talking about seriously cranked stuff";
var mainTitleSize = "1";
var mainTextAlign = "R";
var SixUpTitle = new Array ("Title 1", "Title 2", "Title 3", "Title 4", "Title 5", "Title 6");
var SixUpText = new Array ("Text 1", "Text 2", "Text 3", "Text 4", "Text 5", "Text 6");
var SixUpLink = new Array ("http://www.matterport.com/page1.html",
														"http://www.matterport.com/page2.html",
														"http://www.matterport.com/page3.html",
														"http://www.matterport.com/page4.html",
														"http://www.matterport.com/page5.html",
														"http://www.matterport.com/page6.html"
														);

var pageTitle = "CMS-143: 6-Up";
var mainContent = element(by.css('[class*="node page_builder defaultlayout"]'));

describe("CMS-143: 6-Up", function () {

	beforeEach(function () {
		// Timing is critical, so let the page catch up before each test
		CMS.wait(1);
	});

	afterEach(function () {
		// We don't really have any cleanup after each test
	});

	//---------------------------------------------------------------------------
	// Create a new page that will be used during this script
	// The last spec is to delete the page
	//---------------------------------------------------------------------------
	it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
		expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
	});

	it("Can be dragged and dropped into the Main Content area", function() {
		//---------------------------------------------------------------
		// Note: to use CMS.dragAndDrop, find the class name for the
		// widget you're testing. You can leave the 'maincontent' target
		//---------------------------------------------------------------
		var item = element.all(by.className('sixup')).get(0);
		var target = element.all(by.className('maincontent')).get(0);

		CMS.dragAndDrop(item, target);
		CMS.wait(1);
		expect(element(by.className('maincontent')).element(by.css('[class*="node mp_widgets sixup"]')).isPresent()).toBe(true);
	});

	//---------------------------------------------------------------
	// Now you've got a new page, with a new widget to test!
	// See what you can do with it!
	//---------------------------------------------------------------

	it('Has six 6-Up Content blocks', function() {
		var blocks = element.all(By.css('[class="node mp_widgets sixupcontent"]'));
		expect(blocks.count()).toEqual(6);
		CMS.wait(1);
	});

	it('Allows editing of the 6-Up header', function() {
		element(by.css('[class$="node mp_widgets sixup"]')).all(by.className('edit')).first().click();
		CMS.align();
		CMS.wait(1);

		// Expect all input fields to be present
		expect(element(by.css('[id$="-background_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_text"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_text_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_size"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_align"]')).isPresent()).toBe(true);

		element(by.css('[id$="-background_color"]')).clear().sendKeys(bgColor);
		element(by.css('[id$="-main_title"]')).clear().sendKeys(mainTitle);

		element(by.css('[id$="-main_title_color"]')).clear().sendKeys(bgColorMainTitle);
		element(by.css('[id$="-main_text"]')).clear().sendKeys(mainText);

		element(by.css('[id$="-main_text_color"]')).clear().sendKeys(bgColorMainText);
		element(by.css('[id$="-main_title_size"]')).sendKeys(mainTitleSize);
		element(by.css('[id$="-text_align"]')).sendKeys(mainTextAlign);

		element(by.css('[value="Save"]')).click();
		CMS.wait(1);
	});

	it('Allows all 6 content areas to be edited', function() {
		element.all(by.css('[class*="node mp_widgets sixupcontent"]')).each(function(element, index) {
			element.element(by.className('edit')).click();
			CMS.wait(2);
			CMS.align();

			// Expect all input fields to be present
			expect(element.element(by.css('[id$="-title"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[id$="-url_text"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[id$="-url"]')).isPresent()).toBe(true);

			element.element(by.css('[id$="-title"]')).clear().sendKeys(SixUpTitle[index]);
			element.element(by.css('[id$="-url_text"]')).clear().sendKeys(SixUpText[index]);
			element.element(by.css('[id$="-url"]')).clear().sendKeys(SixUpLink[index]);

			// Bypass the save button by pressing ENTER
			element.element(by.css('[value="Save"]')).click();
			//browser.driver.actions().sendKeys(protractor.Key.ENTER).perform();
			CMS.wait(1);
		});
	});

	it('Edited values appear in Preview mode', function() {
		browser.executeScript('window.scrollTo(0,0);').then(function () {
      element(By.css('[href^="/widgy/preview-page"]')).click();
    });

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {

				// Verify the Main title is present
				expect(element(by.xpath('//h1[contains(text(), "' + mainTitle + '")]')).isPresent()).toBe(true);
				expect(element(by.xpath('//p[contains(text(), "' + mainText + '")]')).isPresent()).toBe(true);

				// Verify the are 6 titles
				element.all(by.css('[class*="uses-title"]')).each(function(element, index) {
					expect(element.getText()).toBe(SixUpTitle[index]);
				});

				// Verify the are 6 URL texts
				element.all(by.css('[class*="uses-tab-cta"]')).each(function(element, index) {
					expect(element.getText()).toBe(SixUpText[index]);
				});

				// Verify the are 6 URL links
				element.all(by.css('[class*="w-inline-block uses-tab"]')).each(function(element, index) {
					expect(element.getAttribute('href')).toEqual(SixUpLink[index]);
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
		var widget = mainContent.findElement(By.css('[class*="node mp_widgets sixup"]'));
		widget.findElement(By.className('delete')).click();

		// Pain in the @ss - there's a popup window
		CMS.wait(1);
		browser.driver.switchTo().alert().accept();
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets sixup"]')).isPresent()).toBe(false);
	});

	//---------------------------------------------------------------
	// The last thing we want to do is remove the test page
	// Note: You *must* use the exact text you used to create it!
	//---------------------------------------------------------------

	it('Delete this page because we are done with it', function() {
		CMS.removePage(pageTitle);
		CMS.wait(1);
		expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
