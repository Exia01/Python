from flask import Flask, render_template, request, session, redirect, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'whatsecret?'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = connectToMySQL('users-info')

# now, we may invoke the query_db method
#print("users", mysql.query_db("SELECT * FROM users;"))


@app.route('/')
def index():
    if 'urs' not in session:
        session['urs'] = ""
    if 'mail' not in session:
        session['mail'] = ""
    totalusers = mysql.query_db("SELECT * FROM users")
    print("Fetched all users", totalusers)
    return render_template('index.html', name=session['urs'], mail=session['mail'])


@app.route('/addinfo', methods=['POST'])
def create():

    if len(request.form['usname']) < 1:
        flash("Usrname cannot be blank!")
        return redirect("/")
    if len(request.form['mail']) < 1:
        flash("Email cannot be blank!")
        return redirect("/")
    elif not EMAIL_REGEX.match(request.form['mail']):
        flash("Invalid Email Address!")
        return redirect("/")
    else:
        flash("Success!")

    query = "INSERT INTO users (username, email, created_at, updated_at) VALUES (%(username)s, %(email)s, NOW(), NOW());"
    data = {
        'username': request.form['usname'],
        'email':  request.form['mail'],
    }
    mysql.query_db(query,data)
    return redirect("/result")


@app.route('/result')
def show():
    totalusers = mysql.query_db("SELECT * FROM users")
    return render_template('results.html', users=totalusers)


@app.route("/clear", methods=["POST"])
def finishsess():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
