from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
def index():
    return render_template("Fake_Blog.html", phrase='suhhhh', times=5)


app.run(debug=True)
