from flask import Flask, render_template, request, session, redirect, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'whatsecret?'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = connectToMySQL('sti')


@app.route("/")
def index():
    if 'Fname' not in session:
        session['Fname'] = ""
    if 'lname' not in session:
        session['Lname'] = ""
    if 'Mail' not in session:
        session['Mail'] = ""
    return render_template("index2.html", Fname=session['Fname'], Lname=session['Lname'], Email=session['Mail'])


@app.route('/create', methods=['POST'])
def create():
    # error_flag = 0
    if len(request.form['Fname']) < 2:
        flash("First Name cannot be blank!")
        return redirect("/")  
        # error_flag = 1 could be instead of the flash?
    if len(request.form['pass']) < 1:
        flash("Password  cannot be blank!")
        return redirect("/")
    if len(request.form['Lname']) < 2:
        flash("Last Name cannot be blank!")
        return redirect("/")
    if len(request.form['Email']) < 2:
        flash("Email cannot be blank!")
        return redirect("/")
    elif not EMAIL_REGEX.match(request.form['Email']):
        flash("Invalid Email Address!")
#         return redirect("/")
    else:
        flash("Success!")
    pw_hash = bcrypt.generate_password_hash(request.form['pass'])
    print(pw_hash)
    query = "INSERT INTO users (first_name, last_name, email, pass, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s, %(Email)s,%(password_hash)s, NOW(), NOW());"
    data = {
        'first_name': request.form['Fname'],
        'last_name':  request.form['Lname'],
        'Email':  request.form['Email'],
        'password_hash': pw_hash}
    # print(query, data)
    mysql.query_db(query, data)
    return redirect("/success")


@app.route("/login/", methods=['POST', 'GET'])
def login():
    if 'Mail' not in session:
        session['Mail'] = ""
    if request.method == 'GET':
        return render_template("login.html", Email=session['Mail'])
    if len(request.form['pass']) < 2:
        flash("Fill out the password please")
    query = "SELECT * FROM users WHERE email = %(Email)s;"
    data = {"Email": request.form["Email"]}
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['pass'], request.form['pass']):
            session['userid'] = result[0]['id']
            return redirect('/success')


    flash("You could not be logged in")
    return render_template("login.html",)


@app.route("/success")
def all():
    return render_template("thankyou.html")


@app.route("/welcome")
def welcome():
    return render_template("WelcomePage.html")


@app.route("/clear", methods=["POST"])
def finish():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
