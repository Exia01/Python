from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/index/')
def index():
    return render_template("index.html", times=8, b=8)


@app.route('/y/<x>/<ab>')
def index1(x, ab):
    return render_template("index.html", times=int(x), b=int(ab))


if __name__ == "__main__":
    app.run(debug=True)
