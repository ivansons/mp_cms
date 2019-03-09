/**************************************************************************
 * CMS-120: 3-up icon
 **************************************************************************/

/**************************************************************************
 This section contains run-level stuff, so please don't modify it
***************************************************************************/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE

browser.driver.manage().window().setSize(1920, 1080);


/**************************************************************************
 This section contains your test 'promises'
 There should be one top-level 'describe' section and any number of
 'it' descriptions, each of which is a testing function.

 I recommend having the first 'it' section create a new page for testing
 and the last 'it' should remove the page, cleaning up on our way out
***************************************************************************/
var pageTitle = "CMS-120: 3-up icon";

// These are are editable fields for 3-up icon (only 1 for this widget)
var mainBackgroundColor = "#FFEECC";
var mainTitleText = "Three Up Icons!";
var mainTitleColor = "#00CC44";
var mainTitleCSSClass = "";
var mainTitleCSSStyle = "";
var mainText = "We should see three icons and stuff";
var mainTextColor = "#EECCFF";
var mainTitleSize = "1";
var mainTitleAlignment = "R";

// This is where we will put variables to handle Image content blocks
// once we figure out how to deal with drag and drop images


// These are the editable fields for the Image content blocks (3 of them)
var ttbTitle = new Array("Single", "Double", "Triple");
var ttbTitleColor = new Array("#ccffbb", "#eeccdd", "#00ccdd");
var ttbTitleText = new Array("This is one", "This is two", "This is three");
var ttbText = new Array("Wooble", "Giggle", "Google");
var ttbTextColor = new Array("#eeffdd", "#8844cc", "#eedd88");
var ttbSize = new Array("4", "5", "6");

// These are the editable fields for the CTAs (3 of them)
var ctaText = new Array("CTA One", "CTA Two", "CTA Three");
var ctaLink = new Array("http://www.mercury.com", "http://www.venus.com", "http://www.earth.com");

describe("CMS-120: 3-up icon", function () {

		beforeEach(function () {
			// Timing is critical, so let the page catch up before each test
			CMS.wait(1);
	    });

	    afterEach(function () {
	      // do nothing
	    });

	it('Needs a new widgy page', function () {
		//console.log("Creating a new Widgy page");
		CMS.newPage(pageTitle);
		expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
	});

	it("Can be dragged and dropped into the main content area", function() {
		//console.log("Drag and drop a new 3-up Icon widget");

		//---------------------------------------------------------------
		// Note: to use CMS.dragAndDrop, find the class name for the
		// widget you're testing. You can leave the 'maincontent' target
		//---------------------------------------------------------------
		var item = element(by.css('[class*="shelfItem mp_widgets threeupicon"'));
		var target = element(by.css('[class*="node page_builder maincontent"]'));
		CMS.dragAndDrop(item, target);
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets threeupicon"]')).isPresent()).toBe(true);
	});

	//---------------------------------------------------------------
	// Now you've got a new page, with a new widget to test!
	// See what you can do with it!
	//---------------------------------------------------------------

	it('Has three image content blocks', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets imagetitletextcta"]'));
		expect(blocks.count()).toEqual(3);
	});

	it('Has three Title text blocks', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets titletextcta"]'));
		expect(blocks.count()).toEqual(3);
	});

	it('Allows editing of the 3-up icon main section', function() {
		element(by.css('[class*="node mp_widgets threeupicon"]')).all(by.className('edit')).first().click();
		CMS.wait(1);

		expect(element(by.css('[id$="-background_color"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-main_title"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-main_title_color"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-css_class"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-css_style"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-main_text"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-main_text_color"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-main_title_size"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[id$="-text_align"]')).isDisplayed()).toBe(true);
		expect(element(by.css('[value="Save"]')).isDisplayed()).toBe(true);

		element(by.css('[id$="-background_color"]')).clear().sendKeys(mainBackgroundColor);
		element(by.css('[id$="-main_title"]')).clear().sendKeys(mainTitleText);
		element(by.css('[id$="-main_title_color"]')).clear().sendKeys(mainTitleColor);
		element(by.css('[id$="-css_class"]')).clear().sendKeys(mainTitleCSSClass);
		element(by.css('[id$="-css_style"]')).clear().sendKeys(mainTitleCSSStyle);

		CMS.align();

		element(by.css('[id$="-main_text"]')).clear().sendKeys(mainText);
		element(by.css('[id$="-main_text_color"]')).clear().sendKeys(mainTextColor);
		element(by.css('[id$="-main_title_size"]')).click().sendKeys(mainTitleSize);
		element(by.css('[id$="-text_align"]')).click().sendKeys(mainTitleAlignment);
		element(by.css('[value="Save"]')).click();
		CMS.wait(1);
	});

	it('Allows editing of Title text blocks', function() {
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
			CMS.align();
			t.clear().sendKeys(ttbTitle[index]);

			var tc = element.element(by.css('[id$="-title_color"]'));
			tc.clear().sendKeys(ttbTitleColor[index]);

			var ts = element.element(by.css('[id$="-title_size"]'));
			ts.click().sendKeys(ttbSize[index]);

			var tt = element.element(by.css('[id$="-text"]'));
			tt.clear().sendKeys(ttbText[index]);

			var ttc = element.element(by.css('[id$="-text_color"]'));
			ttc.sendKeys(ttbTextColor[index]);

			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
		});
	});

	it('Allows editing of the CTAs', function() {
		element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
			//browser.executeScript('arguments[0].scrollIntoView()', element.getWebElement());
			CMS.align();
			element.all(by.className('edit')).first().click();
			CMS.wait(1);

			expect(element.element(by.css('[id$="-text"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-url"]')).isDisplayed()).toBe(true);

			var t = element.element(by.css('[id$="-text"]'));
			CMS.align();
			t.clear().sendKeys(ctaText[index]);

			var l = element.element(by.css('[id$="-url"]'));
			l.clear().sendKeys(ctaLink[index]);

			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
			});
		});

	it('Changes are reflected in Preview mode', function() {
		browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		})

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {

				// Verify the Main title is present
				CMS.wait(5);
				expect(element(by.xpath('//h' + mainTitleSize + '[contains(text(), "' + mainTitleText + '")]')).isPresent()).toBe(true);
				expect(element(by.xpath('//p[contains(text(), "' + mainText + '")]')).isPresent()).toBe(true);

				element.all(by.css('[class="module-blurb"]')).each(function(element, index) {
					expect(element.getText()).toBe(ttbText[index]);
				});

				element.all(by.css('[class="button-text"]')).each(function(element, index) {
					expect(element.getText()).toBe(ctaText[index]);
				});

				element.all(by.css('[class="w-inline-block new-button"]')).each(function(element, index) {
					expect(element.getAttribute('href')).toContain(ctaLink[index]);
				})

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});

	it('Can be deleted from the Main content section', function() {
		var mainContent = browser.driver.findElement(By.className('maincontent'));
		var widget = mainContent.findElement(By.css('[class*="node mp_widgets threeupicon"]'));
		widget.findElement(By.className('delete')).click();

		// Pain in the @ss - there's a popup window
		CMS.wait(2);
		browser.driver.switchTo().alert().accept();
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets threeupicon"]')).isPresent()).toBe(false);
	});


	//---------------------------------------------------------------
	// The last thing we want to do is remove the test page
	// Note: You *must* use the exact text you used to create it!
	//---------------------------------------------------------------

	it('The containing Widgy page can be deleted', function() {
		//console.log("Removing test page");
		CMS.removePage(pageTitle);
		browser.driver.sleep(1500);
		expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
