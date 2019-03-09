/**
* CMS-133: 3-up Image
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

var pageTitle = "CMS-133: 3-up Image";

describe("CMS-133: 3-up Image", function () {

	var mainTitleBackgroundColor = "#EECCDD";
	var mainTitleText = "Something Unexpected";
	var mainTitleColor = "#4422EE";
	var mainTitleCSSClass = "";
	var mainTitleCSSStyle = "";
	var mainText = "Something Wonderful";
	var mainTextColor = "#FFEE00";
	var mainTextSize = "4";
	var mainTextAlignment = "C";

	var ttbTitle = new Array("Thing 1", "Thing 2", "Thing 3");
	var ttbTitleColor = new Array("#00AACC", "#8866CC", "#EECC00");
	var ttbTitleSize = new Array("1", "2", "3");
	var ttbText = new Array("This is first", "This is second", "This is third");
	var ttbTextColor = new Array("#444444", "#666666", "#888888");

	var ctaCSSClass = "";

	var ctaText = new Array("Larry", "Moe", "Curly", "Shemp");
	var ctaLink = new Array("http://www.larry.com", "http://www.moe.com", "http://www.curley.com", "http://www.shemp.com");

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
		// console.log("Creating a new Widgy page");
		CMS.newPage(pageTitle);
		expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
	});

	it("Can be dragged and dropped into the Main content area", function() {
		// console.log("Drag and drop a 3-up Image widget");

		//---------------------------------------------------------------
		// Note: to use CMS.dragAndDrop, find the class name for the
		// widget you're testing. You can leave the 'maincontent' target
		//---------------------------------------------------------------
		var item = element.all(by.className('threeupimage')).get(0);
		var target = element.all(by.className('maincontent')).get(0);

		CMS.dragAndDrop(item, target);
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets threeupimage"]')).isPresent()).toBe(true);
	});

	//---------------------------------------------------------------
	// Now you've got a new page, with a new widget to test!
	// See what you can do with it!
	//---------------------------------------------------------------

	it('Should have 3 Image content blocks', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets imagetitletextcta"]'));
		expect(blocks.count()).toEqual(3);
	});

	it('Should have 3 Title text blocks', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets titletextcta"]'));
		expect(blocks.count()).toEqual(3);
	});

	it('Should have one Single CTA block', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets singlecta"]'));
		expect(blocks.count()).toEqual(1);
	});

	it('Should have 4 CTAs', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets cta"]'));
		expect(blocks.count()).toEqual(4);
	});

	it('Allows editing of the 3-up image block', function() {
		element(by.css('[class*="node mp_widgets threeupimage"]')).all(by.className('edit')).first().click();
		CMS.wait(1);
		CMS.align();

		expect(element(by.css('[id$="-background_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-css_class"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-css_style"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_text"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_text_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_size"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_align"]')).isPresent()).toBe(true);

		// Set the background color
		CMS.wait(1);
		element(by.css('[id$="-background_color"]')).clear().sendKeys(mainTitleBackgroundColor);

		// Change the Main Title text
		element(by.css('[id$="-main_title"]')).clear().sendKeys(mainTitleText);

		// Change the Main title color
		element(by.css('[id$="-main_title_color"]')).clear().sendKeys(mainTitleColor);

		// Set the CSS class
		element(by.css('[id$="-css_class"]')).clear().sendKeys(mainTitleCSSClass);

		// Set the CSS style
		element(by.css('[id$="-css_style"]')).clear().sendKeys(mainTitleCSSStyle);

		// Change the Main text
		element(by.css('[id$="-main_text"]')).clear().sendKeys(mainText);

		// Change the Main text color
		element(by.css('[id$="-main_text_color"]')).clear().sendKeys(mainTextColor);

		// Change the Main Title Size form default 2 to 3
		element(by.css('[id$="-main_title_size"]')).click().sendKeys(mainTextSize).click();

		// Change the text alignment to Right
		element(by.css('[id$="-text_align"]')).click().sendKeys(mainTextAlignment).click();

		// And click the Save button
		// Bypassing this by clicking the ENTER button to save the current 'form'
		browser.driver.actions().sendKeys(protractor.Key.ENTER).perform();
		element(by.css('[value="Save"]')).click();
		CMS.wait(1);
	});

	it('Allows editing of the Title text blocks', function() {
		element.all(by.css('[class*="node mp_widgets titletextcta"]')).each(function(element, index) {
			CMS.align();
			element.all(by.className('edit')).first().click();
			CMS.wait(1);

			expect(element.element(by.css('[id$="-title"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-title_color"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-title_size"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-text"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-text_color"]')).isDisplayed()).toBe(true);

			var t = element.element(by.css('[id$="-title"]'));
			t.clear().sendKeys(ttbTitle[index]);

			var tc = element.element(by.css('[id$="-title_color"]'));
			tc.clear().sendKeys(ttbTitleColor[index]);

			var ts = element.element(by.css('[id$="-title_size"]'));
			ts.click().sendKeys(ttbTitleSize[index]);

			var tt = element.element(by.css('[id$="-text"]'));
			tt.clear().sendKeys(ttbText[index]);

			var ttc = element.element(by.css('[id$="-text_color"]'));
			ttc.sendKeys(ttbTextColor[index]);

			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
		});
	});

	it('Allows editing of the Single CTA block', function() {
		element(by.css('[class*="node mp_widgets singlecta"]')).all(by.className('edit')).first().click();
		CMS.align();
		CMS.wait(1);
		expect(element(by.css('[id$="-css_class"]')).isDisplayed()).toBe(true);

		// Set the CSS class
		element(by.css('[id$="-css_class"]')).clear().sendKeys(ctaCSSClass);
		element.all(by.css('[value="Save"]')).first().click();
		CMS.wait(1);
	});

	it('Allows editing of the CTA blocks', function() {
		element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
			CMS.align();
			element.all(by.className('edit')).first().click();
			CMS.wait(1);
			expect(element.element(by.css('[id$="-text"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-url"]')).isDisplayed()).toBe(true);

			var t = element.element(by.css('[id$="-text"]'));
			t.clear().sendKeys(ctaText[index]);

			var l = element.element(by.css('[id$="-url"]'));
			l.clear().sendKeys(ctaLink[index]);

			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
		});
	});

	it('Shows edited values in Preview mode', function() {
		browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		})

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {
				CMS.wait(1);

				// Check out the header stuff
				expect(element(by.xpath('.//*[.="' + mainTitleText + '"]')).isPresent()).toBe(true);
				expect(element(by.xpath('.//*[.="' + mainText + '"]')).isPresent()).toBe(true);

				// Verify the CTAs
				element.all(by.css('[class*="module-blurb"]')).each(function(element, index) {
					expect(element.getText()).toBe(ttbText[index]);
				});

				element.all(by.css('[class*="w-inline-block new-button"]')).each(function(element, index) {
					expect(element.getAttribute("href")).toContain(ctaLink[index]);
					expect(element.getText()).toEqual(ctaText[index]);
				});

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});

	it('Should be deleted', function() {
		var mainContent = browser.driver.findElement(By.className('maincontent'));
		var widget = mainContent.findElement(By.css('[class*="node mp_widgets threeupimage"]'));
		widget.findElement(By.className('delete')).click();

		// Pain in the @ss - there's a popup window
		CMS.wait(2);
		browser.driver.switchTo().alert().accept();
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets threeupimage"]')).isPresent()).toBe(false);	});

	//---------------------------------------------------------------
	// The last thing we want to do is remove the test page
	// Note: You *must* use the exact text you used to create it!
	//---------------------------------------------------------------

	it('Delete this page because we are done with it', function() {
		// console.log("Removing test page");
		CMS.removePage(pageTitle);
		CMS.wait(1);
		expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
