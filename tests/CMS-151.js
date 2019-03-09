/**
* CMS-151: Drag a Stats widget to the Main content of Default layout
*/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var MainTitle1 = "Pain Title One";
var pageTitle = "CMS-151: Stats widget";
var mainText1 = "blah blah blah";
var bgColor = "#0098ff";
var bgColorMainTitle = "#4d4d4d";
var bgColorMainText = "#d1d3d4";
var mainTitleSize = "1";
var mainTextAlign = "R";
var quoteTitle = new Array ("Jerry", "Larry", "Barry");
var quoteSubtitle = new Array ("Donkey", "Monkey", "Doggie");
var titleColor = "#f6f6f6";
var subtitleColor = "#4d4d4d";
var pageTitle = "CMS-151: Stats widget";

describe("CMS-151: Stats widget", function () {

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

	it("Can be dragged an dropped into to the main content area", function() {
		var item = element(by.css('[class*="shelfItem mp_widgets stats"]'));
		var target = element(by.className('maincontent'));

		CMS.dragAndDrop(item, target);
		CMS.wait(2);
		expect(element(by.css('[class*="node mp_widgets stats"]')).isPresent()).toBe(true);
	});

	it('Should allow the Main title and Main text to be edited', function() {
		element(by.css('[class*="node mp_widgets stats"]')).element(by.className('edit')).click();
		CMS.wait(1);
		element(by.css('[id$="-background_color"]')).clear().sendKeys(bgColor);
		element(by.css('[id$="-main_title"]')).clear().sendKeys(MainTitle1);
		element(by.css('[id$="-main_title_color"]')).clear().sendKeys(bgColorMainTitle);
		element(by.css('[id$="-main_text"]')).clear().sendKeys(mainText1);
		element(by.css('[id$="-main_text_color"]')).clear().sendKeys(bgColorMainText);
		element(by.css('[id$="-main_title_size"]')).click().sendKeys(mainTitleSize);
		element(by.css('[id$="-text_align"]')).click().sendKeys(mainTextAlign);
		CMS.wait(1);
		browser.executeScript('arguments[0].scrollIntoView()', element(by.css('[value="Save"]')).getWebElement());
		element(by.css('[value="Save"]')).click();
		CMS.wait(1);
		CMS.align();

		element.all(by.css('[class*="node mp_widgets singlequote"]')).each(function(element, index) {
			element.all(by.className('edit')).first().click();
			CMS.wait(1);
			element.all(by.css('[id$="-title"]')).first().clear().sendKeys(quoteTitle[index]);
			element.all(by.css('[id$="-title_color"')).first().clear().sendKeys(titleColor);
			element.all(by.css('[id$="-subtitle"]')).first().clear().sendKeys(quoteSubtitle[index]);
			element.all(by.css('[id$="-subtitle_color"]')).first().clear().sendKeys(subtitleColor);
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
				CMS.wait(3);
				// Verify the first CTA
				expect(element(by.xpath('//div[contains(text(), "' + MainTitle1 + '")]')).isPresent()).toBe(true);
				expect(element(by.xpath('//p[contains(text(), "' + mainText1 + '")]')).isPresent()).toBe(true);
				//expect(element(by.xpath('//a[contains(@href, "' + ctaLink1 + '")]')).isPresent()).toBe(true);

				element.all(by.css('[class*="stats-small"]')).each(function(element, index) {
					browser.executeScript('arguments[0].scrollIntoView()', element.getWebElement());
					expect(element.getText()).toBe(quoteTitle[index]);
				});

				element.all(by.css('[class*="stats-large"]')).each(function(element, index) {
					browser.executeScript('arguments[0].scrollIntoView()', element.getWebElement());
					expect(element.getText()).toBe(quoteSubtitle[index]);
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
