from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect("buspass.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buspass (
        pass_id TEXT PRIMARY KEY,
        name TEXT,
        student_id TEXT,
        college TEXT,
        source TEXT,
        destination TEXT,
        mobile TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/apply", methods=["GET", "POST"])
def apply():

    if request.method == "POST":

        pass_id = "BP" + str(random.randint(1000,9999))

        name = request.form["name"]
        student_id = request.form["student_id"]
        college = request.form["college"]
        source = request.form["source"]
        destination = request.form["destination"]
        mobile = request.form["mobile"]

        conn = sqlite3.connect("buspass.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO buspass
        VALUES (?,?,?,?,?,?,?)
        """,(
            pass_id,
            name,
            student_id,
            college,
            source,
            destination,
            mobile
        ))

        conn.commit()
        conn.close()

        return render_template("success.html", pass_id=pass_id)

    return render_template("apply.html")


@app.route("/view", methods=["GET","POST"])
def view():

    if request.method == "POST":

        pass_id=request.form["pass_id"]

        conn=sqlite3.connect("buspass.db")
        cursor=conn.cursor()

        cursor.execute(
            "SELECT * FROM buspass WHERE pass_id=?",
            (pass_id,)
        )

        data=cursor.fetchone()

        conn.close()

        return render_template("view.html", data=data)

    return render_template("search.html")


if __name__=="__main__":
    app.run(debug=True)
