from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def dashboard():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM incoming_mail")
    mail_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_movement WHERE status='Issued'")
    issued_files = cursor.fetchone()[0]

    return render_template(
        "dashboard.html",
        mail_count=mail_count,
        issued_files=issued_files
    )

@app.route("/mail")
def mail_register():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM incoming_mail ORDER BY date_received DESC")
    records = cursor.fetchall()
    return render_template("mail_register.html", records=records)

@app.route("/files")
def file_tracking():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM file_movement")
    files = cursor.fetchall()
    return render_template("file_tracking.html", files=files)

if __name__ == "__main__":
    app.run(debug=True)
