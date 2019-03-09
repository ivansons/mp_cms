/**
 * CMS-412: Overlay widget
 */
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

// Here are some pre-defined values to use throughout the script
var pageTitle = "CMS-412: 2-up overlay";

var mainBackground = "#EECC00";
var mainTitleText = "Fancy Groovy Title";
var mainTitleColor = "#00CC44";
var mainCSSClass = "";
var mainCSSStyle = "";
var mainText = "But wait - there's more!";
var mainTextColor = "#AA44FF";
var mainTextSize = "3";
var mainTextAlign = "R";

var ttbTitle = new Array("Marvelous", "Fabulous");
var ttbTitleColor = new Array("#CCEE44", "#668800");
var ttbTitleSize = new Array("1", "2");
var ttbText = new Array("This is cool", "Really, it is cool");
var ttbTextColor = new Array("#004488", "#4488CC");

var ctaText = new Array("Amazing", "Outstanding");
var ctaLink = new Array("http://www.amazing.matterport.com", "http://www.outstanding.matterport.com");
var ctaTitle = new Array("Wicked", "Gruesome");
var ctaTitleText = new Array("Something wicked this way comes", "Bone chilling");

describe("CMS-412: 2-Up Overlay", function () {
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

	it("Can be dragged and dropped into the Main content area", function() {
		var item = element(by.css('[class*="shelfItem mp_widgets twoupoverlay"]'));
		var target = element(by.className('maincontent'));

		CMS.dragAndDrop(item, target);
		CMS.wait(2);
		expect(element(by.css('[class*="node mp_widgets twoupoverlay"]')).isPresent()).toBe(true);
	});

	it('Has two Image content blocks', function() {
		var blocks = element.all(By.css('[class="node mp_widgets imagetitletextcta"]'));
		expect(blocks.count()).toEqual(2);
	});

	it('Allows editing of the Main title and Main text', function() {
		element(by.css('[class*="node mp_widgets twoupoverlay"]')).all(by.className('edit')).first().click();
		CMS.wait(1);
		CMS.align();

		// Expect all the input elements to be present

		expect(element(by.css('[id$="-background_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="css_class"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="css_style"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_text"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-main_title_size"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_align"]')).isPresent()).toBe(true);

		CMS.align();
		element(by.css('[id$="-background_color"]')).clear().sendKeys(mainBackground);
		element(by.css('[id$="-main_title"]')).clear().sendKeys(mainTitleText);
		element(by.css('[id$="-main_title_color"]')).clear().sendKeys(mainTitleColor);

		CMS.align();
		element(by.css('[id$="css_class"]')).clear().sendKeys(mainCSSClass);
		element(by.css('[id$="css_style"]')).clear().sendKeys(mainCSSStyle);

		CMS.align();
		element(by.css('[id$="-main_text"]')).clear().sendKeys(mainText);
		element(by.css('[id$="-main_title_color"]')).clear().sendKeys(mainTextColor);
		element(by.css('[id$="-main_title_size"]')).click().sendKeys(mainTextSize);
		element(by.css('[id$="-text_align"]')).click().sendKeys(mainTextAlign);

		CMS.align();
		element(by.css('[value="Save"]')).click();
		CMS.wait(1);
	});

	it("Allows editing of the Title text blocks", function() {
		element.all(by.css('[class*="node mp_widgets titletextcta"]')).each(function(element, index) {
			element.all(by.className('edit')).first().click();
			CMS.wait(1);

			//Expect all the input elements to be present
			expect(element.element(by.css('[id$="-title"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[id$="-title_color"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[name$="-title_size"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[id$="-text"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[id$="-text_color"]')).isPresent()).toBe(true);

			CMS.align();
			var title = element.element(by.css('[id$="-title"]'));
			title.clear().sendKeys(ttbTitle[index]);

			var color = element.element(by.css('[id$="-title_color"]'));
			color.clear().sendKeys(ttbTitleColor[index]);

			CMS.align();
			var size = element.element(by.css('[name$="-title_size"]'));
			size.click().sendKeys(ttbTitleSize);

			var text = element.element(by.css('[id$="-text"]'));
			text.clear().sendKeys(ttbText[index]);

			CMS.align();
			var tcolor = element.element(by.css('[id$="-text_color"]'));
			tcolor.clear().sendKeys(ttbTextColor);

			CMS.align();
			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
		});
	});

	it('Allows editing of CTA text and links', function() {
		element.all(by.css('[class*="node mp_widgets cta"]')).each(function(element, index) {
			element.all(by.className('edit')).first().click();
			CMS.wait(1);

			// Expect all input elements to be present
			expect(element.element(by.css('[id$="-text"]')).isPresent()).toBe(true);
			expect(element.element(by.css('[id$="-url"]')).isPresent()).toBe(true);

			CMS.align();
			var text = element.element(by.css('[id$="-text"]'));
			text.clear().sendKeys(ctaText[index]);

			var link = element.element(by.css('[id$="-url"]'));
			link.clear().sendKeys(ctaLink[index]);

			CMS.align();
			element.all(by.css('[value="Save"]')).first().click();
			CMS.wait(1);
		});
	});

	it('Edited values are present in Preview mode', function() {
		browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		})

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {

				// Verify the intro block
				var header = element(by.css('[class*="w-container module-intro-container"]'));
				expect(header.element(by.css('[style^="color:"]')).isPresent()).toBe(true);
				// expect(header.element(by.css('[style^="color:"]')).getAttribute("style")).toContain(mainTextColor);
				expect(header.element(by.css('[style^="color:"]')).getText()).toEqual(mainTitleText);
				expect(header.element(by.className("module-intro")).isPresent()).toBe(true);
				expect(header.element(by.className("module-intro")).getText()).toEqual(mainText);

				// Verify the two image blocks
				element.all(by.css('[class*="image-column-copy"]')).each(function(element, index) {
					expect(element.all(by.css('[style^="color:"]')).first().isPresent()).toBe(true);
					// expect(element.all(by.css('[style^="color:"]')).first().getAttribute("style")).toContain(ttbTitleColor[index]);
					expect(element.all(by.css('[style^="color:"]')).first().getText()).toEqual(ttbTitle[index]);

					expect(element.all(by.css('[class*="module-blurb"]')).first().isPresent()).toBe(true);
					// expect(element.all(by.css('[class*="module-blurb"]')).first().getAttribute("style")).toContain(ttbTextColor[index]);
					expect(element.all(by.css('[class*="module-blurb"]')).first().getText()).toEqual(ttbText[index]);

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

	it('Can be deleted', function() {
		var mainContent = browser.driver.findElement(By.className('maincontent'));
		var twoUp = mainContent.findElement(By.className('twoupoverlay'));
		twoUp.findElement(By.className('delete')).click();

		// Pain in the @ss - there's a popup window
		browser.driver.switchTo().alert().accept();
		CMS.wait(1);
		expect(element(by.css('[class*="node mp_widgets twoupoverlay"]')).isPresent()).toBe(false);
	});

	it('Has its Widgey page deleted at the end of the test', function() {
		CMS.removePage(pageTitle);
		CMS.wait(1);
		expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
