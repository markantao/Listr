from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/signup', methods=['POST', 'GET'])
def register():


@app.route("/main")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
