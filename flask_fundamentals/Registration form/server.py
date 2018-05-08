from flask import Flask, render_template, request, redirect, request, session, flash
import re

app = Flask(__name__)
print(__name__)
app.secret_key = "Whatkey?"


@app.route("/")
def main():
    # if "comment" not in session:
    #     session["comment"] = ""
    # if "thename" not in session:
    #     session["thename"] = ""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
