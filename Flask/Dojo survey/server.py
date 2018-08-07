from flask import Flask, render_template, request, redirect
app = Flask(__name__)
print(__name__)


@app.route("/")
def main():
    return render_template('index4.html')


@app.route("/process", methods=["POST"])
def send():
    name = request.form['thename']
    location = request.form['location']
    cmmt = request.form['comment']
    lang = request.form['lang']
    print(name)
    return render_template("index.html", name=name, loc=location, comment=cmmt, lang=lang)


@app.route('/danger')
def alert():
    print("Some dude visited  a page, we directed her/him/it/insert/here/")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
