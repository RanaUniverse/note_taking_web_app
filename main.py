from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return render_template("about_page.html")


@app.route("/help")
def help_page():
    return render_template("help_page.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
