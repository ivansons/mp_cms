// conf.js
// This file has properties about the run environment and is to be called by Protractor, e.g., protractor conf.js

var date = new Date();
var HtmlReporter = require('protractor-jasmine2-html-reporter');
var jasmine_reporters_dir = 'jasmine-reporters';
var SpecReporter = require('jasmine-spec-reporter');

// WARNING:  DO NOT REMOVE '/tmp' ***************************************************

var date_no_space = (date.toString()).replace(/[\s()-]/g, "_").substring(0,24);
// add '/' slash so that images folder is created inside report dir
var log_dir = '/tmp/mp_cms/' + process.env['CIRCLE_BUILD_NUM'] + '/';

// ********** WARNING ************

exports.config = {

    'seleniumAddress': 'http://ukyo2:NSQXQzYb5Cr2NWyqgYXG@hub.browserstack.com/wd/hub',

    specs: [
        'display_login_user.js',
        'CMS-412.js',   // 2-up Overlay
        'CMS-134.js',   // 3 CTA
        'CMS-120.js',   // 3-up Icon
        'CMS-133.js',   // 3-up image
        'CMS-141.js',   // 3-up Long Text
        'CMS-142.js',   // 3-up Overlay
        'CMS-143.js',   // 6-Up
        'CMS-144.js',   // CTA
        'CMS-145.js',   // CTA Button
        'CMS-146.js',   // Customer Stories
        'CMS-124.js',   // Feature Section
        'CMS-148.js',   // Feature Section Video
        'CMS-122.js',   // Hero
        'CMS-149.js',   // Image Content Block
        'CMS-150.js',   // Quotes
        'CMS-147.js',   // Single CTA
        'CMS-151.js',   // Stats
        'CMS-152.js',   // Title Text Block
    ],

    multiCapabilities: [

        {'browserName': 'chrome',
            'browserstack.local' : 'true',
            'javascriptEnabled': 'true',
            'os' : 'OS X',
            'os_version' : 'EL Capitan',
            'resolution' : '1920x1080'
        },

        //{'browserName': 'firefox',
        // 'javascriptEnabled': true,
        //},
        //
        //{'browserName': 'safari',
        //'javascriptEnabled': true,
        //},

        //{'browserName': 'phantomjs'}  //runs 10 times slower
    ],

    reporters: ['html'],
    framework: 'jasmine2',  // jasmine2 => generate junit_report.xml

    // this timeout is actually verifiable in the script when I print it out
    jasmineNodeOpts: {
        defaultTimeoutInterval: 30000,  //DEFAULT is 30 seconds
        isVerbose: true,
        showColors: true,
        includeStackTrace: true,
        print: function () { }
    },

    onPrepare: function() {

        //Add a screenshot reporter and store screenshots to `/temp/screnshots`:

        var myBrowser;

        return browser.getCapabilities().then(function (cap) {
            myBrowser = cap.caps_.browserName;
            console.log('Browser name: ' + myBrowser);

            var url = process.env['CMS_HOST'] + "/admin/login";
            browser.ignoreSynchronization=true;
            browser.driver.get(url);  // DO NOT REMOVE this please regardless ...
            browser.driver.sleep(3000); // needs to use "driver" or else it fail

            //Add a screenshot reporter and store screenshots to `/temp/screnshots`:
            jasmine.getEnv().addReporter(new HtmlReporter({
                savePath: log_dir
                , screenshotsFolder: '/images'
                , takeScreenshots: true  // screenshot for spec
                , takeScreenshotsOnlyOnFailures: false
                , docTitle: 'Matterport: CMS Automation Report'
                , preserveDirectory: true
                , filePrefix: 'report_' + myBrowser // yield chrome.html for example
                , consolidate: true
                , consolidateAll: true
                , displayStacktrace: 'summary'  // {none, all, specs, summary}
            }));

            var jasmineReporters = require(jasmine_reporters_dir);
            //var jasmineReporters = require('jasmine-reporters');
            jasmine.getEnv().addReporter(new jasmineReporters.JUnitXmlReporter({
                consolidateAll: true,
                // must put file to project/workspace
                savePath: log_dir,
                //savePath: '/Users/Shared/Jenkins/Home/jobs/Portal_Automation/workspace',
                filePrefix: 'report_' + myBrowser  // yield junit style xml
            }));

            jasmine.getEnv().addReporter(new SpecReporter({
                displayStacktrace: 'all',     // display stacktrace for each failed assertion, values: (all|specs|summary|none)
                displayFailuresSummary: true,  // display summary of all failures after execution
                displayPendingSummary: true,   // display summary of all pending specs after execution
                displaySuccessfulSpec: true,   // display each successful spec
                displayFailedSpec: true,       // display each failed spec
                displayPendingSpec: true,      // display each pending spec
                displaySpecDuration: true,     // display each spec duration
                displaySuiteNumber: true       // display the suite number
            }));

        });

    } //onPrepare
};
