# mini_RDBMS


This is a mini webpage based Relational Database Management System (RDBMS) using Flask-Restful. For my Summer 2019 internship at San Ramon startup <a href="https://www.apporchid.com/">AppOrchid</a>, I was first tasked with learning about SQL and REST API's. So, I was given an assignment: recreate the actor table of the commonly used <a href= "http://www.postgresqltutorial.com/postgresql-sample-database/">DVDrental database (hosted using Postgres)</a> onto an HTML webpage format. The webpage was to include operations for inserting, updating, and deleting items to and from the HTML table. These operations would have had to subsequently insert, update, and delete items from the Postgres Database using a RESTful API.
<br>
<hr>

![Image of Website](https://i.ibb.co/vmXxKsT/Screenshot.png)

<h2>Technologies Used</h2>

  - *Flask-Restful* (Python) - created a server where the website was hosted, accessed the postgres database, and allowed for HTTP requests to be made to the server through the REST philosophy. This was done in the crud.py file.
  - *Javascript* - creating the table and allowing for CRUD operations on the front end
  - *Javascript AJAX* - sending HTTP requests to and from the server created using Flask-Restful
  - *HTML and CSS* - The HTML table was generated using JS and was styled using CSS.
  - *PostGreSQL (SQL)* - This is where the DVDrental database was hosted. I allowed access to this database in my crud.py file and used simple SQL queries to select, insert, update, and delete data in the actor table of this database.

<h2>What I learned</h2>

  - How to use Flask to create a REST API.
  - How the front end and the back end of a website are connected.
  - How to work with Databases and use basic SQL.
  - What a server is and how they are hosted on a local machine.
  - How to use Javascript to generate HTML and AJAX to send http requests to a server.
  - What a <a href="https://virtualenv.pypa.io/en/latest/">Virtual Environment</a> is and how to use one.
