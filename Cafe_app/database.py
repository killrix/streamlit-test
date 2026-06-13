
import sqlite3

conn = sqlite3.connect(
    "cafe_database.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    mobile TEXT,
    table_no INTEGER,
    amount REAL,
    status TEXT DEFAULT 'Preparing',
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS tables(
    table_no INTEGER PRIMARY KEY,
    status TEXT
)
""")

# Feedback
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    customer_name TEXT,
    rating INTEGER,
    comments TEXT
)
""")

# Loyalty
cursor.execute("""
CREATE TABLE IF NOT EXISTS loyalty(
    customer_name TEXT PRIMARY KEY,
    points INTEGER
)
""")

# Initialize tables

for i in range(1,11):

    cursor.execute(
        """
        INSERT OR IGNORE INTO tables
        VALUES (?,?)
        """,
        (
            i,
            "Available"
        )
    )

conn.commit()

print("Database initialized.")

