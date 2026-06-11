from flask import Flask, render_template
import psycopg2


app = Flask(__name__)

# 🔗 Use Render INTERNAL URL or ENV variable
DATABASE_URL = "postgresql://employees_db_tyd6_user:CJX6BjNcjG475aacv5WEosdXxKB5qXB3@dpg-d8l7hmf7f7vs73fnpprg-a/employees_db_tyd6"

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()

    # Fetch latest record
    cur.execute("SELECT name, email FROM users ORDER BY id DESC LIMIT 1;")
    row = cur.fetchone()

    cur.close()
    conn.close()

    # If no data exists
    if row:
        name, email = row
    else:
        name, email = "No Data", "N/A"

    return render_template("index.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)