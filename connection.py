import mysql.connector as SQLC
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

db_config = None

try:
    temp_conn = SQLC.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        use_pure=True
    )

    temp_cursor = temp_conn.cursor()
    temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    temp_cursor.close()
    temp_conn.close()

    db_config = SQLC.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        use_pure=True
    )

    print("Database connected successfully!")

    cursor = db_config.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            role ENUM('admin', 'agent', 'customer') NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS properties(
            property_id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(150) NOT NULL,
            property_type VARCHAR(50) NOT NULL,
            location VARCHAR(100) NOT NULL,
            price DECIMAL(15,2) NOT NULL,
            bedrooms INT NOT NULL,
            agent_id INT NULL,
            description VARCHAR(500),
            status ENUM('Pending','Approved','Rejected','Available','Sold','Rented') DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(agent_id) REFERENCES users(user_id) ON DELETE SET NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enquiries(
            enquiry_id INT PRIMARY KEY AUTO_INCREMENT,
            customer_id INT NOT NULL,
            property_id INT NOT NULL,
            message VARCHAR(500) NOT NULL,
            status ENUM('New','Read','Closed') DEFAULT 'New',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(customer_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY(property_id) REFERENCES properties(property_id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            booking_id INT PRIMARY KEY AUTO_INCREMENT,
            customer_id INT NOT NULL,
            property_id INT NOT NULL,
            status ENUM('Requested','Approved','Rejected') DEFAULT 'Requested',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(customer_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY(property_id) REFERENCES properties(property_id) ON DELETE CASCADE
        )
    """)

    db_config.commit()

    user_query = """
        INSERT INTO users(user_id, name, email, password, role)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE user_id = user_id
    """

    users = [
        (1, "System Admin", "admin@gmail.com", "admin123", "admin"),
        (2, "Demo Agent", "agent@gmail.com", "agent123", "agent"),
        (3, "Demo Customer", "customer@gmail.com", "customer123", "customer"),
        (4, "ravi", "ravi@gmail.com", "ravi123", "agent")
    ]

    for user in users:
        cursor.execute(user_query, user)

    property_query = """
        INSERT INTO properties
        (property_id, title, property_type, location, price, bedrooms, agent_id, description, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE property_id = property_id
    """

    properties = [
        (101, "Green Valley Apartment", "Apartment", "Hyderabad", 6500000.0, 3, 2,
         "Spacious 3 BHK apartment", "Approved"),
        (102, "Dream Apartment", "Apartment", "Hyderabad", 55000000.0, 5, 4,
         "Spacious Apartment with 5 BHK", "Approved")
    ]

    for property_data in properties:
        cursor.execute(property_query, property_data)

    cursor.execute("SELECT COUNT(*) FROM enquiries WHERE enquiry_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            """INSERT INTO enquiries(enquiry_id, customer_id, property_id, message, status)
               VALUES (%s, %s, %s, %s, %s)""",
            (1, 3, 102, ": I am interested in this property.", "New")
        )

    cursor.execute("SELECT COUNT(*) FROM bookings WHERE booking_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            """INSERT INTO bookings(booking_id, customer_id, property_id, status)
               VALUES (%s, %s, %s, %s)""",
            (1, 3, 102, "Approved")
        )

    cursor.execute("SELECT COUNT(*) FROM bookings WHERE booking_id = 2")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            """INSERT INTO bookings(booking_id, customer_id, property_id, status)
               VALUES (%s, %s, %s, %s)""",
            (2, 3, 102, "Requested")
        )

    db_config.commit()
    print("Tables and demo records are ready.")

    cursor.close()

except SQLC.Error as err:
    print("Database Connection Failed:", err)
    db_config = None
