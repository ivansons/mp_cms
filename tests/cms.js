'use strict';

var CMS = function () {

};

// The reason to use prototype is for faster performance since it's kind of like
// static method or singleton behavior: loaded once and used by all

CMS.prototype = Object.create({}, {

	newPage: {
	// get: function()  // use "get" whenever the function returns something

	value: function (pageTitle) {

			var url = process.env['CMS_HOST'] + "/admin/login";

			browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
			browser.get(url);

			// First, we need to log in
			browser.driver.findElement(By.name("username")).sendKeys(process.env['CMS_USERNAME']);
			browser.driver.findElement(By.name("password")).sendKeys(process.env['CMS_PASSWORD']);
			browser.driver.findElement(By.id("interface_admin")).click();
			browser.driver.findElement(By.name("password")).submit();
			this.wait(1);

			// Create a widgy page directly from a URL, bypassing the UI
			var url = process.env['CMS_HOST'] + "/admin/widgy_mezzanine/widgypage/add";
			browser.driver.get(url);
			this.wait(1);

			// Should be on the Add widy page
			browser.driver.findElement(By.name("title")).sendKeys(pageTitle);
			browser.driver.findElement(By.name("title")).submit();
			this.wait(1);
	}},

	// align() scrolls the main window so the widget is fully visible
	align: {
		value: function() {
			browser.executeScript('arguments[0].scrollIntoView()', element(by.css('[class="form-row field-root_node"]')).getWebElement());
	}},

	wait: {
		value: function(interval) {
			var tick = process.env['CMS_INTERVAL'];
			browser.driver.sleep(tick * interval);
	}},

 	removePage: {
	value: function() {
		// This routine assumes we're currently on the page
		// The Delete button is part of the bottom frame and should always be visible
		element(by.className('deletelink')).click();
		this.wait(1);
		element(by.className('default')).click();
		this.wait(1);

		// And we will log out, just to be on the safe side
		browser.driver.findElement(By.linkText("Log out")).click();
	}},

	dragAndDrop: {
	value: function(widget, target) {
		browser.executeScript("arguments[0].scrollIntoView();", widget.getWebElement());
		browser.executeScript("window.scrollBy(0, -200)");
		browser.actions().mouseDown(widget).perform();
		this.wait(1);

		var mainContent = element(by.css('[class*="node page_builder maincontent"]'));
		browser.driver.actions().mouseMove(mainContent, {x:300, y:50}).perform();
		this.wait(1);

		browser.actions().mouseUp().perform();

		this.wait(1);
	}}
});

module.exports = CMS;
