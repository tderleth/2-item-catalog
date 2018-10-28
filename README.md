# Project: Logs Analyses

This repo is part of a series of projects belonging to my [Full Stack Web Developer Nanodegree](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004). Purpose of this lesson is to dig deeper into the [flask framework](http://flask.pocoo.org/), oAuth flows as well as API design and implementation.  

## Installation

The project uses [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [vagrant](https://www.vagrantup.com/) as development environment. For more info on setup look into the [VM configuration](/Vagrantfile). To get the VM up and running you need to have both tools (vortualbox and vagrant) installed on your computer. 

1.  `git clone git@github.com:tderleth/1-logs-analysis.git`
2.  `cd 2-item-catalog`
3.  `vagrant up && vagrant ssh`

## Development

In order to start/view the application you need to run the following steps:

1.  `cd /vagrant && python run.py`
2.  Go to your browser and view [localhost:5000](http://localhost:5000)

## References

[VM configuration](/Vagrantfile) duplicate of [udacity/fullstack-nanodegree-vm/](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)

## Requirements

-   [Rubic](https://review.udacity.com/#!/rubrics/5/view) 

### API Endpoints

-   [ ] _Does the project implement a JSON endpoint with all required content?_ The project implements a JSON endpoint that serves the same information as displayed in the HTML endpoints for an arbitrary item in the catalog.

### CRUD

-   [x] _Does the website read category and item information from a database?_ Website reads category and item information from a database.
-   [ ] _Does the website include a form allowing users to add new items and correctly processes these forms?_ Website includes a form allowing users to add new items and correctly processes submitted forms.
-   [ ] _Does the website include a form to update a record in the database and correctly processes this form?_ Website does include a form to edit/update a current record in the database table and correctly processes submitted forms.
-   [ ] _Does the website include a way to delete an item from the catalog?_ Website does include a function to delete a current record.
-   [ ] Make sure that users are not able to submit a form to the database until they have added a value. This means you should validate your forms.
-   [ ] Make sure also that when a category is deleted, the item should be deleted along side it. Items should not still be contained in the database when its Parent is deleted.

### Authentication & Authorization

-   [x] _Do create, delete, and update operations consider authorization status prior to execution?_ Create, delete and update operations do consider authorization status prior to execution.
-   [x] _Does the website implement a third party authentication and authorization service?_ Page implements a third-party authentication & authorization service (like Google Accounts or Mozilla Persona) instead of implementing its own authentication & authorization spec.
-   [x] _Is there a “login” and “logout” button/link in the website?_ Make sure there is a 'Login' and 'Logout' button/link in the project. The aesthetics of this button/link is up to the discretion of the student.

### Code Quality

-   [ ] _Is the code ready for personal review and is neatly formatted?_ Code is ready for personal review and neatly formatted and compliant with the Python [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

### Comments

-   [ ] _Are comments present and effectively explain longer code procedures?_ Comments are present and effectively explain longer code procedures.

### Documentation

-   [ ] _Is there a README file included detailing all steps required to successfully run the application?_ README file includes details of all the steps required to successfully run the application.

## Maintainer

-   [Thomas Derleth](mailto:thomas.derleth@moovel.com)
