import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Sample projects to insert
projects = [
    ("Hall Ticket Generator", "A web app to generate hall tickets with QR codes for exams.", "https://github.com/samay/hall-ticket-generator"),
    ("Doodle Board", "An interactive drawing board built with React and Canvas.", "https://github.com/samay/doodle-board"),
    ("Invoice Generator", "A website to generate invoices for companies using React and MySQL.", "https://github.com/samay/invoice-generator"),
    ("My Portfolio", "A website which shows my skill and experience","https://github.com/samay/my_portfolio")
]

# Insert projects into the table
cursor.executemany('INSERT INTO projects (title, description, link) VALUES (?, ?, ?)', projects)

# Commit and close the connection
conn.commit()
conn.close()
