from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'shh'


@app.route('/')
def index():
    if 'counter' not in session:  # this is creating the dictionary keys
        session['counter'] = 0  # this provides the values / string or number
        print(session['counter'])

    session['counter'] += 1
    print(session)

    # this passes the information onto the html doc
    # html variable goes first
    return render_template("index.html", count=session['counter'])


@app.route('/show', methods=['POST'])
def increment():
    print("Got Post Info")

    session['counter'] += 1  # page is already counting through redirecting

    return redirect('/')


@app.route('/one', methods=['POST'])
def one():
 # page is already counting through redirecting

    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
