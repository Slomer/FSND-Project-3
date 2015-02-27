# Udacity Full Stack Nanodegree project 3.  Item catalog.
## Description
This is a project submission for the Udacity full stack web dev nanodegree.  Project 3: Item Catalog using python's flask and sqlalchemy apis (with sqlite as the database platform).

A simple secure temporary token or nonce is used during any edit functions and they are passed via POST requests via ajax modals.

This uses a modified version of the the Udacity support repo found [here](http://github.com/udacity/fullstack-nanodegree-vm) as well as [vagrant](https://www.vagrantup.com/) and virtualization software such as [virtualbox](https://www.virtualbox.org/).


##Steps to run
optional step: put your own github application key information into the config.py file and ensure http://localhost:8080 is your github application callback.  A temporary one is included already for testing purposes and at least at the time this is submitted it is an active key.

1. Clone or Download the rep.
2. run vagrant up from the vagrant subdirectory in the rep.  This assumes you have vagrant installed already.
3. SSH into the virtual machine using Vagrant SSH
4. From the vagrant/item-catalog subfolder, run "python flask_app.py".  The databases should be built for you if this is the first time it has been run but they will be empty.
5. After you see "Running on http://0.0.0.0:8080/" in the shell, open a browser to http://localhost:8080
6. The page should be fairly boring to start with and will show just a login button.  Click login with github and authorize to see the rest of the application.
7. Once logged in, 2 additional buttons should show.  Press the little database icon in the top right to load in the sample data.
8. The UI should be fairly straightforward.  Each company has an expandable menu item and once expanded it's items will show.  In a desktop environment you can hover over elements to get popup tips on edit functions but they should all work in a mobile or touch environment as well.
9. If you log out, the edit elements will not show or function but the content should.

##API endpoints
JSON: http://localhost:8080/company/(company-id)/JSON
XML: http://localhost:8080/company/(company-id)/XML

example: http://localhost:8080/company/1/JSON

note: this is easily accessed in a manual way by filtering to a single company from the main app page and then adding XML or JSON to the end of the url.

##Possible enhancements:

1. Add front end form validation.  Right now the app handles blank inputs gracefully and will simply show a blank company name/item name/image without an actual error but it would be best to require at least some information during input.
2. Add an admin level user and restrict edits from standard users to only content they add or are granted access to by an admin.
3. Add a javascript spinner when logging in or waiting on ajax modals to signal that something is happening.
4. Move the username pull to an ajax call instead of as part of the initial login to speed up the initial login time and remove any chance of the api preventing a successful load.  For now it is assumed that if github responds to an oauth it will respond to a request for the username but that is not a safe assumption.
5. Add inline editing for company name.
6. Add bulk data uploads either by parsing pasted input or through jquery post so that entire companies or multiple items can be added at once by a user.
7. Add some basic search logic into the API endpoints so that companies can be queried more than one at a time based on partial name match, etc.