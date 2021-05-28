from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/signup')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
