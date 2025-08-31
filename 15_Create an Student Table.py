import sqlite3

# Connect to database (or create it if it doesn’t exist)
conn = sqlite3.connect("student_record.db")

# Create a cursor object
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()

# Close the connection (good practice)
conn.close()
