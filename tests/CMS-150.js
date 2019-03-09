/**************************************************************************
 * CMS-150: Quotes
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
var pageTitle = "CMS-150: Quotes";
var htmlContent = "<ul> <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li> <li>Aliquam tincidunt mauris eu risus.</li> <li>Vestibulum auctor dapibus neque.</li> </ul>";
var singlequoteTitle = new Array("Holy Macaroni", "Life of Petey");
var titleColor = new Array("#00AACC", "#8866CC");
var singlequoteSubtitle = new Array("Can't get enough", "You must not win");
var subtitleColor = new Array("#444444", "#666666");

// This is where we will put variables to handle Image content blocks
// once we figure out how to deal with drag and drop images

describe("CMS-150: Quotes", function () {

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
		var item = element(by.css('[class*="shelfItem mp_widgets quotes"'));
		var target = element(by.css('[class*="node page_builder maincontent"]'));
		CMS.dragAndDrop(item, target);
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets quotes"]')).isPresent()).toBe(true);

	});

	it('Has HTML content block', function() {
		var blocks = element.all(By.css('[class*="node page_builder html"]'));
		expect(blocks.count()).toEqual(1);
	});

	it('Has two single quote blocks', function() {
		var blocks = element.all(By.css('[class*="node mp_widgets singlequote"]'));
		expect(blocks.count()).toEqual(2);
	});

	it('Allows editing of the HTML section', function() {
		element(by.css('[class*="node page_builder html"]')).all(by.className('edit')).first().click();
		CMS.align();
		CMS.wait(1);
		element(by.css('[class*="cke_button__source"]')).click();

		var ht = $('[class*="cke_source cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr"]');
		ht.click();
		ht.clear().sendKeys(htmlContent);

		element(by.css('[value="Save"]')).click();
		CMS.wait(1);
	});

	it('Allows editing of Single Quote blocks', function() {
		element.all(by.css('[class*="node mp_widgets singlequote"]')).each(function(element, index) {
			CMS.align();
			element.all(by.className('edit')).first().click();
			CMS.wait(1);

			expect(element.element(by.css('[id$="-title"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-title_color"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-subtitle"]')).isDisplayed()).toBe(true);
			expect(element.element(by.css('[id$="-subtitle_color"]')).isDisplayed()).toBe(true);

			var t = element.element(by.css('[id$="-title"]'));
			t.clear().sendKeys(singlequoteTitle[index]);

			var tc = element.element(by.css('[id$="-title_color"]'));
			tc.clear().sendKeys(titleColor[index]);

			var ts = element.element(by.css('[id$="-subtitle"]'));
			ts.clear().sendKeys(singlequoteSubtitle[index]);

			var tt = element.element(by.css('[id$="-subtitle_color"]'));
			tt.clear().sendKeys(subtitleColor[index]);

			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
		});
	});  // IT block


	it('Changes are reflected in Preview mode', function() {
		browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		})

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {

				// Verify HTML content and single quote blocks are present with correct text

				element.all(by.css('[class*="htmloutput"]')).each(function(element, index) {
									 expect(element.getText()).toBe(htmlContent);
							 });

							 // Deal with the first item first...
							 expect(element.all(by.css('[class*="testimonial-copy"]')).first().getText()).toBe(singlequoteTitle[0]);
							 expect(element.all(by.css('[class*="testimonial-attribute"]')).first().getText()).toBe(singlequoteSubtitle[0]);

							 // Click the dot to get to the next one...
							 element.all(by.css('[class*="w-slider-dot"]')).last().click();
							 CMS.wait(1);

							 expect(element.all(by.css('[class*="testimonial-copy"]')).last().getText()).toBe(singlequoteTitle[1]);
							 expect(element.all(by.css('[class*="testimonial-attribute"]')).last().getText()).toBe(singlequoteSubtitle[1]);

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});  // ends the IT block

	it('Can be deleted from the Main content section', function() {
		var mainContent = browser.driver.findElement(By.className('maincontent'));
		var widget = mainContent.findElement(By.css('[class*="node mp_widgets quotes"]'));
		widget.findElement(By.className('delete')).click();

		// Handle the popup notification
		CMS.wait(1);
		browser.driver.switchTo().alert().accept();
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets quotes"]')).isPresent()).toBe(false);
	});

	it('Delete this page because we are done with it', function() {
		CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
