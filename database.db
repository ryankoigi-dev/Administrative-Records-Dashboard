import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE incoming_mail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    subject TEXT,
    reference TEXT,
    date_received TEXT
)
""")

cursor.execute("""
CREATE TABLE file_movement (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_title TEXT,
    issued_to TEXT,
    issue_date TEXT,
    return_date TEXT,
    status TEXT
)
""")

db.commit()
db.close()
