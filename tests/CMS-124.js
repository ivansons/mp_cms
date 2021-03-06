/***********************************************************************
 * CMS-124: Feature Section widget
 ***********************************************************************/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);

var pageTitle = "CMS-124: Feature Section";
var backgroundColor= "#f6f6f6";
var ttbTitle= "Uncharted Territory";
var titleColor= "#00AACC";
var titleSize= "3";
var ttbText= "This is a deceptive line you have written, good sir.";
var textColor= "#666666";
var ctaText = "Aardvark";
var ctaLink = "http://www.welcometointernet.org";

describe("CMS-124: Feature Section widget", function () {

  it('Needs a new widgy page', function () {
		CMS.newPage(pageTitle);
    expect(element(by.css('[id="id_title"]')).getAttribute("value")).toContain(pageTitle);
  });

  it("Can be dragged and dropped into the main content area", function() {
    var item = element(by.css('[class*="shelfItem mp_widgets featuresection"]'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));
    CMS.dragAndDrop(item, target);
    browser.driver.sleep(1000);
    expect(element(by.css('[class*="shelfItem mp_widgets featuresection"]')).isPresent()).toBe(true);
  });

	it("Feature section parent widget should be editable", function() {
		element(by.css('[class*="node mp_widgets featuresection"]')).element(by.className('edit')).click();
		CMS.wait(1);
    CMS.align();
		expect(element(by.css('[id$="-background_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_content_is_on_left"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-css_class"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-css_style"]')).isPresent()).toBe(true);

		element(by.css('[id$="-background_color"]')).clear().sendKeys(backgroundColor);

		element(by.css('[value="Save"]')).click();
		CMS.wait(1);


	});

	it("Title Text block should be editable", function() {
    var showElement = element(by.css('[class*="node page_builder maincontent"]')).getWebElement();
    browser.executeScript("arguments[0].scrollIntoView();", showElement);
		element(by.css('[class*="node mp_widgets titletextcta"]')).element(by.className('edit')).click();
    CMS.wait(1);
    CMS.align();
		expect(element(by.css('[id$="-title"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-title_color"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-title_size"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_is_raw_html"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text"]')).isPresent()).toBe(true);
		expect(element(by.css('[id$="-text_color"]')).isPresent()).toBe(true);

		 var t = element(by.css('[id$="-title"]'));
		 t.clear().sendKeys(ttbTitle);

		 var tc = element(by.css('[id$="-title_color"]'));
		 tc.clear().sendKeys(titleColor);

		 var ts = element(by.css('[id$="-text"]'));
		 ts.clear().sendKeys(ttbText);

		 var tt = element(by.css('[id$="-text_color"]'));
		 tt.clear().sendKeys(textColor);

		element.all(by.css('[value="Save"]')).first().click();
    CMS.wait(1);

	});


  it("CTA child widget should have editable text and url", function() {
    element(by.css('[class*="node mp_widgets cta"]')).element(by.className('edit')).click();
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
    browser.executeScript('window.scrollTo(0,0);');
        //browser.executeScript("arguments[0].scrollIntoView();", element(by.css('[class*="preview"]')).getWebElement());
		browser.driver.findElement(By.className("preview")).click();

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {
				// Verify the first CTA
				expect(element(by.xpath('//div[contains(text(), "' + ctaText + '")]')).isPresent()).toBe(true);
				expect(element(by.xpath('//a[contains(@href, "' + ctaLink + '")]')).isPresent()).toBe(true);

				// Close up the Preview window so we're back at the main page
				browser.driver.close().then(function() {
          CMS.wait(1);
					browser.switchTo().window(handles[0]);
				});
			});
		});
	});

  it('Can be deleted from the Main content section', function() {
    var mainContent = browser.driver.findElement(By.className('maincontent'));
    var widget = mainContent.findElement(By.css('[class*="node mp_widgets featuresection"]'));
    widget.findElement(By.className('delete')).click();

    // Pain in the @ss - there's a popup window
    browser.driver.switchTo().alert().accept();
    CMS.wait(1);
    expect(element(by.css('[class*="node mp_widgets featuresection"]')).isPresent()).toBe(false);
  });

  it('The containing Widgy page can be deleted', function(){
    CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
  });

});
