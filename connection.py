import mysql.connector as SQLC

# Step 1: Database connection
db_config = SQLC.connect(
    host="localhost",
    user="root",
    password="Manusha@21"
)

# Step 2: Create cursor
cursor = db_config.cursor()

print(db_config)
print(cursor)

# Step 3: Create database
create_database_query = "CREATE DATABASE IF NOT EXISTS real_estate"
cursor.execute(create_database_query)

print("Database created successfully!")

# Step 4: Select database
cursor.execute("USE real_estate")

# Step 5: Create users table
users_table = """
CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL
);
"""

cursor.execute(users_table)
print("Users table created successfully!")

# Step 6: Create properties table
properties_table = """
CREATE TABLE IF NOT EXISTS properties(
    property_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    price DECIMAL(12,2),
    property_type VARCHAR(50),
    agent_id INT,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY(agent_id) REFERENCES users(user_id)
);
"""

cursor.execute(properties_table)
print("Properties table created successfully!")

# Step 7: Create enquiries table
enquiries_table = """
CREATE TABLE IF NOT EXISTS enquiries(
    enquiry_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    property_id INT,
    message VARCHAR(255),
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY(customer_id) REFERENCES users(user_id),
    FOREIGN KEY(property_id) REFERENCES properties(property_id)
);
"""

cursor.execute(enquiries_table)
print("Enquiries table created successfully!")

# Step 8: Create bookings table
bookings_table = """
CREATE TABLE IF NOT EXISTS bookings(
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    property_id INT,
    booking_date DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY(customer_id) REFERENCES users(user_id),
    FOREIGN KEY(property_id) REFERENCES properties(property_id)
);
"""

cursor.execute(bookings_table)
print("Bookings table created successfully!")

# Step 9: Insert users
user_query = """
INSERT IGNORE INTO users(name, email, password, role)
VALUES (%s, %s, %s, %s)
"""

users = [
    ("Admin", "admin@gmail.com", "admin123", "Admin"),
    ("Manusha", "manusha@gmail.com", "manusha123", "Agent"),
    ("Rithika", "rithika@gmail.com", "rithika123", "Customer"),
    ("Rahul", "rahul@gmail.com", "rahul123", "Agent"),
    ("Priya", "priya@gmail.com", "priya123", "Agent"),
    ("Sneha", "sneha@gmail.com", "sneha123", "Customer"),
    ("Arjun", "arjun@gmail.com", "arjun123", "Customer")
]

cursor.executemany(user_query, users)

# Step 10: Insert properties
property_query = """
INSERT INTO properties(title, location, price, property_type, agent_id, status)
SELECT %s, %s, %s, %s, %s, %s
WHERE NOT EXISTS (
    SELECT 1 FROM properties
    WHERE title = %s
)
"""

properties = [
    ("2BHK Apartment", "Hyderabad", 4500000, "Apartment", 2, "Approved", "2BHK Apartment"),
    ("3BHK Villa", "Bangalore", 7500000, "Villa", 2, "Approved", "3BHK Villa"),
    ("Luxury Apartment", "Hyderabad", 5500000, "Apartment", 4, "Approved", "Luxury Apartment"),
    ("Modern Villa", "Bangalore", 8500000, "Villa", 5, "Approved", "Modern Villa"),
    ("3BHK Flat", "Chennai", 6200000, "Apartment", 5, "Approved", "3BHK Flat"),
    ("Independent House", "Hyderabad", 7200000, "House", 2, "Pending", "Independent House"),
    ("Farm House", "Pune", 9500000, "Farm House", 4, "Approved", "Farm House")
]

cursor.executemany(property_query, properties)

# Step 11: Insert enquiry
enquiry_query = """
INSERT INTO enquiries(customer_id, property_id, message, status)
SELECT %s, %s, %s, %s
WHERE NOT EXISTS (
    SELECT 1 FROM enquiries
    WHERE customer_id = %s AND property_id = %s
)
"""

cursor.execute(
    enquiry_query,
    (3, 1, "I am interested in this property", "Pending", 3, 1)
)

# Step 12: Insert booking
booking_query = """
INSERT INTO bookings(customer_id, property_id, booking_date, status)
SELECT %s, %s, %s, %s
WHERE NOT EXISTS (
    SELECT 1 FROM bookings
    WHERE customer_id = %s AND property_id = %s
)
"""

cursor.execute(
    booking_query,
    (3, 1, "2026-09-30", "Pending", 3, 1)
)

# Step 13: Save changes
db_config.commit()

print("Records inserted successfully!")

# Step 14: Display users
cursor.execute("SELECT * FROM users")

data = cursor.fetchall()

for row in data:
    print(row)

# Step 15: Close connection
cursor.close()
db_config.close()

print("Database connection closed.")
