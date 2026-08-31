REAL ESTATE PROPERTY MANAGEMENT SYSTEM

Python console application using OOP, normal text-file handling, and exception handling.

IMPORTANT: This version does NOT use JSON, databases, Flask, or SQL.

Run:
    python main.py

Demo accounts:
Admin: admin@gmail.com / admin123
Agent: agent@gmail.com / agent123
Customer: customer@gmail.com / customer123

Storage files:
    data/users.txt
    data/properties.txt
    data/enquiries.txt
    data/bookings.txt

Concepts used:
- OOP: classes, objects, inheritance, constructors, methods, encapsulation
- File handling: open(), read, write, append-style persistence through text files
- Exception handling: try/except, ValueError, FileNotFoundError, OSError and general Exception
- Regular expression validation for email
- Lists, dictionaries, loops, conditions and functions

Complete flow:
1. Agent or Admin adds a property.
2. Admin approves the property.
3. Customer searches approved properties.
4. Customer sends an enquiry or booking request.
5. Agent sees enquiries and booking requests for their properties.
6. Admin sees all enquiries and booking requests.
