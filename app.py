from flask import Flask, redirect, render_template, request, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "P39E7YVPYPDCS6ZRG9R6DDWN"


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/signup', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT email FROM main WHERE email = '{email}'")
        ting = cursor.fetchone()
        if ting == [] or ting == None:
            cursor.execute(
                f"INSERT INTO main (email, password) VALUES ('{email}','{password}')")
            db.commit()
            cursor.close()
            return redirect(url_for("login"))
        else:
            return render_template("accountalreadyexists.html")
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email1']
        password = request.form['password1']
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(
            f"SELECT email, password FROM main WHERE email = '{email}'")
        info = cursor.fetchall()
        db.commit()
        cursor.close()
        print(info)
        if info == [] or info == None:
            return redirect(url_for("signup"))
        else:
            if info[0][1] == password:
                session["user"] = email
                return redirect(url_for("main"))
            else:
                return render_template("loginerror.html")
    else:
        return render_template("login.html")


@app.route("/main")
def main():
    if 'user' in session:
        email = session["user"]
    return render_template("main.html", email=email)


@app.route("/listInformation")
def information():
    return render_template("eformation.html")


if __name__ == "__main__":
    app.run(debug=True)
