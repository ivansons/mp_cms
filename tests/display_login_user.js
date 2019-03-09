/**
 * Created by ukyo on 5/25/16.
 */

/*******************************************************************************************
 This script verifies that you can log into the site and read back the user name on the site.
 *******************************************************************************************/

'use strict';
var CMS = require("./cms.js");
var CMS = new CMS();

describe("Display_login_user:", function () {

    beforeEach(function () {
        browser.ignoreSynchronization = true;
    });

    it('Basic check to see if website is up running.', function () {

        browser.getCurrentUrl().then(function (url) {
            console.log("The URL is: ", url);
        });


        var login_button = element(by.id('login-form'));
        login_button.isPresent().then(function (pres) {
            console.log("The login button presence is : ", pres);
            expect(pres).toEqual(true);
        });

        // First, we need to log in
        browser.driver.findElement(By.name("username")).sendKeys(process.env['CMS_USERNAME']);
        browser.driver.findElement(By.name("password")).sendKeys(process.env['CMS_PASSWORD']);
        browser.driver.findElement(By.id("interface_admin")).click();
        browser.driver.findElement(By.name("password")).submit();
        CMS.wait(2);

        browser.driver.getTitle().then(function (title) {
            console.log("Title is: ", title)
        });
        CMS.wait(1);

        browser.driver.getCurrentUrl().then(function (url) {
            console.log("The URL is: ", url);
        });
        CMS.wait(1);

        var whoami = element(by.css('[id="user-tools"] li:nth-child(1) strong'));
        whoami.getText().then(function (user) {
            console.log("User is : ", user);
        });

        browser.driver.findElement(By.css('a[href="/admin/logout/"]')).click();
        CMS.wait(2);
        expect(browser.getCurrentUrl()).toEqual(process.env['CMS_HOST'] + '/admin/logout/');
    });

});