from flask import Flask, render_template, request, redirect, request, session, flash

app = Flask(__name__)
print(__name__)
app.secret_key = "Whatkey?"


@app.route("/")
def main():
    if "comment" not in session:
        session["comment"] = ""
    if "thename" not in session:
        session["thename"] = ""
    return render_template("index.html", comment=session["comment"], left=session["thename"])


@app.route("/process", methods=["POST"])
def send():
    if len(request.form['thename']) < 1:
        flash("Please provide a proper name, no V for vendetta here!")
        session["comment"] = request.form["comment"]
        session["thename"] = request.form["thename"]
    if len(request.form['comment']) < 1:
        flash("We need commentaries, please provide us one, no longer than a tweet.")
        session["thename"] = request.form["thename"]
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("No longer than a tweet...'120 characters.'")
        session["thename"] = request.form["thename"]
        return redirect("/")
    name = request.form['thename']
    location = request.form["location"]
    cmmt = request.form['comment']
    lang = request.form['lang']

    return render_template("index2.html", name=name, loc=location, comment=cmmt, lang=lang)


@app.route('/danger')
def alert():
    print("Some dude visited  a page, we directed her/him/it/insert/here/")
    return redirect('/')


@app.route("/clear", methods=["POST"])
def finishsess():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
