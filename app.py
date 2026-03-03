#imports
import sqlite3
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template
from analysis import spending_by_category, basic_stats

# flask setup
app = Flask(__name__)
#CREATE DATABASE
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
#########################################
#opens database, access columns by name "(expense["amount"])"
#########################################

#CREATE EXPENSES TABLE

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()
#########################################
#create the columns in accordance to the project plan

@app.route("/")
def home():
#SHOW EXPENSES ON HOMEPAGE
    conn = get_db_connection()
    expenses = conn.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return render_template("index.html",expenses=expenses)

#########################################
# CREATE "ADD EXPENSE" PAGE
@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]
        note = request.form["note"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
            (amount, category, date, note)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")
#########################################
####################################################
#CREATE DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():
    category_data = spending_by_category()
    stats = basic_stats()

    return render_template(
        "dashboard.html",
        category_data=category_data,
        stats=stats
    )
####################################################
#########################################
if __name__ == "__main__":
    init_db()
    app.run(debug=True)

###