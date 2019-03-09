/**
* CMS-145: Drag a CTA Button widget to the Main content of Default layout
*/
'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();
browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
browser.driver.manage().window().setSize(1920, 1080);


var pageTitle = "CMS-145: CTA Button";

var ctaText = "About";
var ctaLink = "a";

describe("CMS-145: CTA Button", function () {

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
    var item = element(by.css('[class*="shelfItem mp_widgets calltoaction"'));
    var target = element(by.css('[class*="node page_builder maincontent"]'));
    CMS.dragAndDrop(item, target);
    CMS.wait(1);
    expect(element(by.css('[class*="node mp_widgets calltoaction"]')).isPresent()).toBe(true);

  });

  it("Has one CTA Button", function() {
    expect(element(by.css('[class*="node mp_widgets calltoaction"]')).isPresent()).toBe(true);
  });


  it('Allows editing of the button text and link', function(){
    browser.driver.findElement(By.className("edit")).click();
    CMS.wait(1);
    element(by.css('[id$="-text"]')).click().sendKeys(ctaText);
    element(by.css('[id$="-link"]')).click().sendKeys(ctaLink).click();

    // Send ENTER to save changes
    //browser.driver.actions().sendKeys(protractor.Key.ENTER).perform();
    element.all(by.css('[value="Save"]')).first().click();
    CMS.wait(1);
  });

  it('Changes are reflected in Preview mode', function() {
		//console.log("Verifying from the Preview window");

		browser.executeScript('window.scrollTo(0,0);').then(function () {
			element(By.css('[href^="/widgy/preview-page"]')).click();
		});

		// Switch out to the Preview window
		browser.getAllWindowHandles().then(function(handles) {
			var newWindowHandle = handles[1];
			browser.switchTo().window(newWindowHandle).then(function() {

        // Verify the Main title is present
        var button = element(by.css('[class*="w-inline-block new-button"]'));
        expect(button.getText()).toEqual(ctaText);
        expect(button.getAttribute("href")).toContain("/about/");

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
    var widget = mainContent.findElement(By.css('[class*="node mp_widgets calltoaction"]'));
    widget.findElement(By.className('delete')).click();

    // Pain in the @ss - there's a popup window
    CMS.wait(1);
    browser.driver.switchTo().alert().accept();
    CMS.wait(1);
    expect(element(by.css('[class*="node mp_widgets calltoaction"]')).isPresent()).toBe(false);
  });

  it('Delete this page because we are done with it', function() {
		CMS.removePage(pageTitle);
    CMS.wait(1);
    expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
	});
});
