from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index/<x>')
def index(x):
    return render_template("index.html", times=int(x))


@app.route('/play/<x>/<color>')
def play(x, color):
    return render_template("index.html", times=int(x), color=color)


app.run(debug=True)


# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def welcome():
#     return "Welcome!"
# @app.route('/play/')
# def index():
#     return render_template("index.html", times = 3)
# @app.route('/play/<x>')
# def play(x):
#     return render_template("index.html", times = int(x))
# @app.route('/play/<x>/<color>')
# def play2(x, color):
#     return render_template("index.html", times = int(x), color = str(color))
# if __name__=="__main__":
#     app.run(debug=True)
