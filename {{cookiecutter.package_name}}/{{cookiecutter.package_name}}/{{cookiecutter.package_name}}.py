from flask import flash, Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.secret_key = 'abc'


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
