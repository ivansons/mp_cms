// conf.js
// This file has properties about the run environment and is to be called by Protractor

var HtmlReporter = require('protractor-jasmine2-html-reporter');
var SpecReporter = require('jasmine-spec-reporter');
var date = new Date();
var jasmine_reporters_dir = 'jasmine-reporters';
var test_url = process.env['CMS_HOST'] + '/admin/login';
//var test_url = "https://qa2-www-0.matterport.com/admin/login";


// WARNING:  DO NOT SET log_dir TO YOUR HOME DIRECTORY **********************************
//           BECAUSE IT WILL WIPE OUT YOUR COMPUTER
// ********** WARNING ************

var date_no_space = (date.toString()).replace(/[\s()-]/g, "_").substring(0,24);
// var log_dir = '/tmp/' + date_no_space + '_CMS' + '/';  // add '/' slash so that images folder is created inside report dir
var log_dir = process.env['BUILD_LOG'] + '/' + date_no_space + '/';

exports.config = {

    // Note: Download standalone selenium jar from: https://selenium-release.storage.googleapis.com/index.html?path=2.53/
    // Start the server in a terminal and kick off your test: java -jar selenium-server-standalone.jar

    //'seleniumAddress': 'http://localhost:4444/wd/hub',
    'seleniumAddress': 'http://ukyo2:NSQXQzYb5Cr2NWyqgYXG@hub.browserstack.com/wd/hub',


  specs: [
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
      'os' : 'OS X',
      'javascriptEnabled': true,
      'os_version' : 'El Capitan',
      'resolution' : '1920x1080',
      'browserstack.local' : 'true'
     },

      //{'browserName': 'firefox',
      // 'javascriptEnabled': true,
      // 'os' : 'OS X',
      // 'os_version' : 'Yosemite',
      // 'resolution' : '1024x768'
      //},
      //
      //{'browserName': 'safari',
      //'javascriptEnabled': true,
      // 'os' : 'OS X',
      // 'os_version' : 'Yosemite',
      // 'resolution' : '1024x768'
      //},

    //{'browserName': 'phantomjs'}  //runs 10 times slower
  ],

    reporters: ['html'],
    framework: 'jasmine2',  // jasmine2 => generate junit_report.xml

    // this timeout is actually verifiable in the script when I print it out
    jasmineNodeOpts: {
        defaultTimeoutInterval: 20000,  //DEFAULT is 30 seconds
        isVerbose: true,
        showColors: true,
        includeStackTrace: true,
        print: function () { }
    },

    onPrepare: function() {

        var myBrowser = 'index' + Math.floor(Math.random()*65534);

        browser.ignoreSynchronization = true; // FOR NON-ANGULAR WEBSITE
        browser.driver.get(test_url);
        browser.driver.sleep(3000);

        jasmine.getEnv().addReporter(new HtmlReporter({
            savePath: log_dir
            , screenshotsFolder: 'images'
            , takeScreenshots: true  // screenshot for spec
            , takeScreenshotsOnlyOnFailures: false
            , docTitle: 'CMS'
            , preserveDirectory: true
            , filePrefix: myBrowser // function() { return browser.capabilities.get('browserName'); } // yield chrome.html for example
            , consolidate: true
            , consolidateAll: true
            , displayStacktrace: 'all'  // {none, all, specs, summary}
        }));

        var jasmineReporters = require(jasmine_reporters_dir);
        jasmine.getEnv().addReporter(new jasmineReporters.JUnitXmlReporter({
            consolidateAll: true
            , savePath: log_dir
            , filePrefix: myBrowser  // yield junit style xml
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

    }, //onPrepare

};
