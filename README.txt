REAL ESTATE PROPERTY MANAGEMENT SYSTEM - MYSQL VERSION

Files:
    connection.py  -> creates database, tables and demo data
    db.py          -> reusable MySQL connection
    user.py        -> registration and login
    property.py    -> property operations
    enquiry.py     -> enquiry operations
    admin.py       -> admin operations
    agent.py       -> agent operations
    customer.py    -> customer operations
    main.py        -> menus and application flow
    .env           -> MySQL connection details

Database:
    real_estate

Tables:
    users
    properties
    enquiries
    bookings

Install:
    pip install -r requirements.txt

Before running, check the MySQL password in .env.

Run:
    python connection.py
    python main.py

Demo accounts:
    Admin:    admin@gmail.com / admin123
    Agent:    agent@gmail.com / agent123
    Customer: customer@gmail.com / customer123
    Agent:    ravi@gmail.com / ravi123
