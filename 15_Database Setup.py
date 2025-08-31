import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()
