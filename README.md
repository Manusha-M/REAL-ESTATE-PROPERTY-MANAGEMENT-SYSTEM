# Real Estate Property Management System

A Python-based console application for managing real estate properties, agents, customers, enquiries, and booking requests. The project uses Object-Oriented Programming (OOP), file handling, exception handling, and a MySQL database for database practice and storage.

---

##  Project Overview

The Real Estate Property Management System provides separate access for **Admin, Agent, and Customer** users.

### Admin
- Add and manage agents
- Add properties
- Approve or reject properties
- View enquiries
- View booking requests

### Agent
- Add properties
- View own properties
- Update property details
- View enquiries
- View booking requests

### Customer
- Register and login
- Search properties
- View approved properties
- Send enquiries
- Request property bookings
- Save favourite properties
- Request property visits

---

##  Features

- User registration and login
- Role-based menus
- Property management
- Property approval
- Customer enquiries
- Booking requests
- File handling
- Exception handling
- Object-Oriented Programming
- MySQL database connection and table creation
- SQL practice using real project tables

---

##  Tech Stack

| Category | Technology |
| --- | --- |
| Language | Python 3 |
| Programming | Object-Oriented Programming (OOP) |
| Database | MySQL |
| Python-MySQL Connection | mysql-connector-python |
| Storage | Text files and MySQL |
| Interface | Console-based |

---

##  Project Structure

```text
REAL-ESTATE-PROPERTY-MANAGEMENT-SYSTEM/
│
├── main.py
├── admin.py
├── agent.py
├── customer.py
├── property.py
├── enquiry.py
├── user.py
├── db.py
├── connection.py
│
├── users.txt
├── properties.txt
├── enquiries.txt
├── bookings.txt
│
├── requirements.txt
└── README.txt
```

### File Description

- `main.py` - Main menu and application flow
- `admin.py` - Admin operations
- `agent.py` - Agent operations
- `customer.py` - Customer operations
- `property.py` - Property related operations
- `enquiry.py` - Enquiry related operations
- `user.py` - User related operations
- `db.py` - Database related functions
- `connection.py` - MySQL connection, database creation, table creation, and sample data
- `users.txt` - User data used by the file-handling part
- `properties.txt` - Property data
- `enquiries.txt` - Enquiry data
- `bookings.txt` - Booking data
- `requirements.txt` - Required Python packages

---

##  MySQL Database

The MySQL database created by `connection.py` is:

```text
real_estate
```

The following tables are created:

```text
users
properties
enquiries
bookings
```

### Table Relationships

```text
users
  |
  ├── properties
  |
  ├── enquiries
  |
  └── bookings
```

The `properties`, `enquiries`, and `bookings` tables use foreign keys to connect related records.

---

##  Setup & Run

### Prerequisites

Make sure the following are installed:

- Python 3.x
- MySQL Server
- Git Bash

Check Python:

```bash
python --version
```

Check MySQL:

```bash
mysql --version
```

### 1. Open the project in Git Bash

```bash
cd ~/Downloads/REAL-ESTATE-PROPERTY-MANAGEMENT-SYSTEM-main
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/Scripts/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

Open `connection.py` and update the MySQL password if required:

```python
db_config = SQLC.connect(
    host="localhost",
    user="root",
    password="your_mysql_password"
)
```

### 6. Create the database and tables

Run:

```bash
python connection.py
```

The script automatically:

- Connects to MySQL
- Creates the `real_estate` database
- Creates the required tables
- Adds sample users
- Adds sample agents and customers
- Adds sample properties
- Adds a sample enquiry
- Adds a sample booking

### 7. Run the application

```bash
python main.py
```

---

##  SQL Practice

After running `connection.py`, the database can be opened in MySQL Workbench.

```sql
USE real_estate;
```

You can practice:

- SELECT
- WHERE
- AND / OR
- LIKE
- BETWEEN
- IN
- ORDER BY
- GROUP BY
- HAVING
- COUNT
- SUM
- AVG
- MIN
- MAX
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- Subqueries

### Example INNER JOIN

```sql
SELECT p.title, p.location, u.name AS agent
FROM properties p
INNER JOIN users u
ON p.agent_id = u.user_id;
```

### Example LEFT JOIN

```sql
SELECT u.name, p.title
FROM users u
LEFT JOIN properties p
ON u.user_id = p.agent_id;
```

### Example GROUP BY

```sql
SELECT agent_id, COUNT(*) AS total_properties
FROM properties
GROUP BY agent_id;
```

---

##  OOP Concepts Used

The project demonstrates:

- Classes and objects
- Constructors
- Inheritance
- Encapsulation
- Methods
- Exception handling
- File handling
- Modular programming

---

##  Notes

- The project is console-based.
- The text files are retained because they are part of the original file-handling implementation.
- MySQL is used for database setup and SQL practice through `connection.py`.
- Keep your local MySQL password private when sharing the project.
- Do not upload real database passwords to a public repository.

---

##  Team Members & Contributions

| Name | Role / Contribution |
| --- | --- |
| **Sravani** | Admin module, admin login, agent management, property approval/rejection, enquiry and booking management |
| **Manusha** | Agent module, property management, agent operations, MySQL database connection and table setup |
| **Rithika** | Customer module, customer registration/login, property search, enquiries, bookings, favourites and visit requests |

### Team Project

This project was developed as a **group project**, with each member working on different modules and integrating the modules into the complete Real Estate Property Management System.

---

##  Project Flow

```text
Main Menu
    |
    ├── Admin Login
    │      ├── Manage Agents
    │      ├── Manage Properties
    │      ├── Enquiries
    │      └── Booking Requests
    │
    ├── Agent Login
    │      ├── Add Property
    │      ├── View Properties
    │      ├── Update Property
    │      ├── Enquiries
    │      └── Booking Requests
    │
    └── Customer
           ├── Register / Login
           ├── Search Properties
           ├── View Approved Properties
           ├── Send Enquiry
           ├── Booking Request
           ├── Save Favourite
           └── Request Visit
```

---

##  Team

**Sravani | Manusha | Rithika**

Real Estate Property Management System
