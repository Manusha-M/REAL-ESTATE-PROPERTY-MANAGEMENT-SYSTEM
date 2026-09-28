============================================================
             REAL ESTATE PROPERTY MANAGEMENT SYSTEM
============================================================

A simple console-based Real Estate Property Management System
developed using Python, MySQL, OOP concepts and file handling.

------------------------------------------------------------
PROJECT FEATURES
------------------------------------------------------------

The system supports three main users:

1. ADMIN
   - Manage agents
   - Add and manage properties
   - Approve or reject properties
   - View enquiries
   - View booking requests

2. AGENT
   - Add properties
   - View own properties
   - Update properties
   - View enquiries
   - Manage booking requests

3. CUSTOMER
   - Register and login
   - Search properties
   - View approved properties
   - Send enquiries
   - Request bookings
   - Save favourite properties
   - Request property visits

------------------------------------------------------------
PROJECT FILES
------------------------------------------------------------

main.py
    Starts the application and displays the main menu.

admin.py
    Contains admin related operations.

agent.py
    Contains agent related operations.

customer.py
    Contains customer related operations.

property.py
    Handles property related operations.

enquiry.py
    Handles enquiry related operations.

user.py
    Handles user related operations.

db.py
    Contains database related functions used by the project.

connection.py
    Connects Python with MySQL, creates the database and
    tables, and inserts sample records.

users.txt
    Stores user information used by the file-handling part
    of the project.

properties.txt
    Stores property information.

enquiries.txt
    Stores enquiry information.

bookings.txt
    Stores booking information.

requirements.txt
    Contains the Python packages required for the project.

------------------------------------------------------------
TECHNOLOGIES USED
------------------------------------------------------------

Python
MySQL
MySQL Connector
OOP
File Handling
Exception Handling
SQL

------------------------------------------------------------
MYSQL DATABASE
------------------------------------------------------------

Database name:

    real_estate

Tables:

    users
    properties
    enquiries
    bookings

The connection.py file creates the database and tables
automatically if they do not already exist.

------------------------------------------------------------
SETUP
------------------------------------------------------------

1. Install Python 3.

2. Install MySQL 8.

3. Open Git Bash inside the project folder.

4. Create a virtual environment:

    python -m venv venv

5. Activate the virtual environment:

    source venv/Scripts/activate

6. Install the required packages:

    pip install -r requirements.txt

------------------------------------------------------------
MYSQL PASSWORD
------------------------------------------------------------

Open connection.py and check the MySQL password.

The current connection is:

    host="localhost"
    user="root"
    password="ROOT"

If your MySQL root password is different, change only the
password value in connection.py.

------------------------------------------------------------
CREATE DATABASE AND TABLES
------------------------------------------------------------

Run:

    python connection.py

The script creates:

    real_estate

and these tables:

    users
    properties
    enquiries
    bookings

It also inserts sample users, agents, customers and
properties.

The insert section is written so that running the file
again does not create duplicate sample records.

------------------------------------------------------------
CHECK DATABASE IN MYSQL
------------------------------------------------------------

Open MySQL:

    mysql -u root -p

Then run:

    SHOW DATABASES;

    USE real_estate;

    SHOW TABLES;

To check the data:

    SELECT * FROM users;

    SELECT * FROM properties;

    SELECT * FROM enquiries;

    SELECT * FROM bookings;

------------------------------------------------------------
SQL PRACTICE
------------------------------------------------------------

After creating the database, the tables can be used for
SQL practice in MySQL Workbench.

Examples of topics that can be practiced:

    SELECT
    WHERE
    AND / OR
    LIKE
    BETWEEN
    IN
    ORDER BY
    GROUP BY
    HAVING
    COUNT
    SUM
    AVG
    MIN
    MAX
    INNER JOIN
    LEFT JOIN
    RIGHT JOIN
    Subqueries

Example INNER JOIN:

    SELECT p.title, p.location, u.name AS agent
    FROM properties p
    INNER JOIN users u
    ON p.agent_id = u.user_id;

Example LEFT JOIN:

    SELECT u.name, p.title
    FROM users u
    LEFT JOIN properties p
    ON u.user_id = p.agent_id;

------------------------------------------------------------
RUN THE APPLICATION
------------------------------------------------------------

After the database setup is complete, run:

    python main.py

------------------------------------------------------------
NOTES
------------------------------------------------------------

The TXT files are kept because the original project uses
file handling for storing application data.

The MySQL database setup is provided through connection.py
for database and SQL practice.

Do not commit real passwords to a public GitHub repository.
If the project is uploaded publicly, replace the password
with your own local configuration before sharing it.

============================================================
