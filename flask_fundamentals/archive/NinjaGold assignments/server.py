from flask import Flask, render_template, request, redirect, session
from random import randint
import datetime
app = Flask(__name__)
app.secret_key = "uncle"

# our index route will handle rendering our form


@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
        session["activity"] = []
        print(session["activity"])

    return render_template("index.html", money=session["gold"])


@app.route("/process-money", methods=["POST"])
def processmoney():
    now = datetime.datetime.now()
    if request.form["info"] == "farm":
        a = randint(10, 20)
        session["gold"] += a
        session["activity"].insert(0, ["Boooiii Earned "+str(a)+" gold from the farm! "+now.strftime("(%Y-%m-%d %H:%M)")])
    elif request.form["info"] == "cave":
        a = randint(5, 10)
        session["gold"] += a
        session["activity"].insert(0, ["Boooiii Earned "+str(a)+" gold from the cave! "+now.strftime("(%Y-%m-%d %H:%M)")])
    elif request.form["info"] == "house":
        a = randint(2, 5)
        session["gold"] += a
        session["activity"].insert(0, ["Boooiii Earned "+str(a)+" gold from the house !"+now.strftime("(%Y-%m-%d %H:%M)")])
    elif request.form["info"] == "casino":
        a = randint(0, 50)
        b = randint(0, 1)
        if b >= 1:
            session["gold"] += a
            session["activity"].insert(0, ["<p class='green'>You wonnnnn "+str(a)+" gold at the casino!"+now.strftime("(%Y-%m-%d %H:%M)</p>")])
        else:
            session["gold"] -= a
            session["activity"].insert(0, ["<p class='red'>Womp, lost "+str(a)+" gold at the casino!"+now.strftime("(%Y-%m-%d %H:%M)</p>")])
    return redirect("/")


@app.route("/clear", methods=["POST"])
def finishsess():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
