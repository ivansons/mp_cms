Matterport CMS
==============

Dev server setup
----------------
Vagrant will create a Ubuntu VM with a complete development environment
and run the dev server inside it.

1. Install `VirtualBox` (as a VM provider for Vagrant):
<https://www.virtualbox.org/wiki/Downloads>

2. Install `Vagrant`:
<https://www.vagrantup.com/downloads.html>

3. Set up Vagrant VM:
```
$ vagrant up
```

4. After setup is done, ssh to Vagrant VM:
```
$ vagrant ssh
```

5. [Production only] Compress CSS and JavaScript files offline (this needs to be run on every node of web server)
```
$ python manage.py compress
```

6. In Vagrant VM, run:
```
$ python manage.py runserver 0.0.0.0:8000
```
Or use the following shortcut:
```
$ pm runserver 0.0.0.0:8000
```

Now open your browser and point to <http://192.168.140.140:8000>
to see the Django app running.

Database sync
-------------
The following Fabric commands need to be run on host (not Vagrant VM):

1. Dump database:
```
$ fab dump_database -R <role>
```
This will dump current database and save to `./db` directory.

```
$ fab vagrant dump_database
```
This will dump current dev env database and save to `./db` directory.

2. Upload database:
```
$ fab upload_database:<database-file> -R <role>
```
This will upload specified database dump.

```
$ dropdb mp_cms
$ createdb mp_cms
$ fab vagrant upload_database:<database-file>
```
This will recreate database and upload specified database dump to dev env.

3. Available roles:
`qa2`: <https://qa2-www-0.matterport.com>
`dev-www-1`: <https://dev-www-1.matterport.com>
`dev-www-2`: <https://dev-www-2.matterport.com>
`dev-www-3`: <https://dev-www-3.matterport.com>
`dev-www-4`: <https://dev-www-4.matterport.com>

4. Miscellaneous:
To create / drop database manually in Vagrant VM, simply run:
```
$ createdb mp_cms
```
or
```
$ dropdb mp_cms
```

S3 cloud storage and CloudFront
-------------
Further steps have to be taken good care of before moving to S3 storage.

1. CORS configuration of S3 bucket to allow cross domain access.
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

2. `python manage.py compress` needs to be run in all of the web servers.

3. *AWS_QUERYSTRING_AUTH* feature has to be turned off for static storage backend to make sure Django-compressor works properly.

4. CouldFront distribution allows GET, HEAD and OPTION.

Prod build
----------
Build tarball for prod:
```
$ make build
```
This will create a tarball under `builds` directory for prod deployment.

Release to QA2
-------------
1. Create / update `qa` branch.
2. Go to GHE `mp_cms` repository, and click on `releases` tab.
3. Click on `Draft a new release`, and create a new tag targeting `qa` branch.  The convention is to use format `<major>.<sprint>.<fix>`.  For example, major version 1 Sprint 6 release 7 should be `1.6.7`.
4. Manually trigger a new build on CircleCI for `qa` branch, in order to build and deploy new static files.  (**this needs to be automated in the future**)
5. Pull to update local repository for the new tag.
6. Run `git describe --tags --long` in local repository to get the version hash.
7. Clone / pull `app-versions` from GHE.
8. Open `mp_env/prodBETA.yaml` file in `app-versions`, and update `mp_cms` value to the version hash from step #6.
9. Commit to `master` branch and push `app-versions`.
10. Wait for 1 or 2 minutes for Salt to pick up latest versions.
11. Run the following Fabric commands on host (not Vagrant VM):
```
$ fab deploy -R qa2
```
12. ~~If miracle happens,~~ Everything should be working!

More information
----------------
[Mezzanine Workflow](https://matterport-confluence.atlassian.net/wiki/display/DCS/Mezzanine+Workflow)

Style guides
------------
1. Python:
PEP 8
```
$ flake8 --exclude=migrations,venv .
```

2. HTML, CSS and JavaScript:
Indent: 2 spaces

Automation Test Setup
---------------------

1. Download 'Selenium' server and start it up in a terminal :
<https://selenium-release.storage.googleapis.com/index.html?path=2.53/>
```
$ java -jar selenium-server-standalone-2.53.0.jar
```

2. Install `NodeJS` :
<https://nodejs.org/en/>

3. In a another terminal, install dependencies from directory where package.json resides:
```
$ cd ~/mp_cms/tests
$ sudo npm install -g
```

4. Run test with Protractor :
```
$ protractor conf.js
```

5. Reports in HTML & XML  are available at directory : 
```
$ cd $HOME/tmp/date_time_of_test_execution
```
# mp_cms
