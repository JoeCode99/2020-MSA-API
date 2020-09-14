# 2020-MSA-API

Access the live webpage: https://msa-api.azurewebsites.net/

## Project Description
***
CoderFinder is a website where software developers can search, favourite, and write notes about available jobs. The site is relatively simple, consisting of three main pages.

#### Home Page

The home page is the simplest of all three pages, showing a title as well as a random quote from https://programming-quotes-api.herokuapp.com/.
Reload the page to see new random quotes for inspiration!

#### Jobs Page

The jobs page consists of two main sections: 
1. Search criteria 
1. Job List

The search criteria allows users to filter jobs by both their location (i.e. Zurich) and job title (i.e. node). Clicking on submit will return a filtered list of jobs.

The job table displays all available jobs (according to the user's search criteria). The API it calls (https://cors-anywhere.herokuapp.com/https://jobs.github.com/positions.json) returns jobs in JSON format, and all that information is formatted to build the table.

Clicking on the `View` button on any list item will display a modal with more information about that particular job. Within the modal, there is a `Favourite` button. Pressing this button adds the job to the database as a favourite job.

This job will now be visible in the favourites page.

#### Favourites Page

The favourites page will display all of your favourited jobs. The table appears to be exactly like the job table, however the `View` button links to a more complex modal.

The modal not only displays more information about the selected job, but it also provides a notes section where users can write any information they like about that particular job. The written notes can be saved by clicking the `Save` button, and if the user no longer wishes to have that job favourited, they can select the `Delete` button (which will open another modal confirming the user's action).

## Running the Project
***
In windows, simply run the following in terminal: 
1. `py -m venv venv` 
1. `venv/Scripts/activate` 
1. `flask run`

If any isues arise, `pip install` the following packages: 
1. os 
1. urllib 
1. flask 
1. flask_sqlalchemy 
1. sqlalchemy

## Tech Stack
***
The tech stack consists of the following:
* Backend: Python (with Flask and SQLAlchemy - handles routing and database CRUD operations)
* Frontend: HTML, Bootstrap, and JavaScript
