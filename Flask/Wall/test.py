from flask import Flask, render_template, request, session, redirect, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'whatsecret?'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = connectToMySQL('wall')


@app.route("/")
def index():
    if 'login' not in session:
        session['login'] = 0
    if 'Fname' not in session:
        session['Fname'] = ""
    if 'lname' not in session:
        session['Lname'] = ""
    if 'Email' not in session:
        session['Email'] = ""
        # creates sessions to save them in
    # login = session['login']
    return render_template("index.html", Fname=session['Fname'], Lname=session['Lname'], Email=session['Email'])


@app.route('/create', methods=['POST'])
def create():
    flag = 0
    Email = request.form['Email']
    Fname = request.form['Fname']
    Lname = request.form['Lname']
    Pass = request.form['pass']
    Rpass = request.form['Rpass']
    if Email or Fname or Lname:
        session['Email'] = Email
        session['Fname'] = Fname
        session['Lname'] = Lname

    if len(Email) < 1 or len(Fname) < 1 or len(Fname) < 1 or len(Pass) or len(Rpass) < 1:
        flash('Please fill out all inputs.')
        flag = 1
    if not EMAIL_REGEX.match(Email):
        flash("Invalid Email Address!")
        session['Email'] = ""
        flag = 1
    # this pulls data from the and ensure no repetition --> query = "SELECT * FROM users WHERE email = %(Email)s;"
    # data = {
        # 'Email' : Email
    #result = mysql.query_db(query,data)
    # if result:
        #flash('Email taken!')
        #flag = 1
    if Pass != Rpass:
        flash('Passwords are not a match!')
        flag = 1
    if not Fname.isalpha() and Fname:
        session['Fname'] = ''
        flash("Name Cannot contain numbers.")
        flag = 1
    if not Lname.isalpha() and Lname:
        session['Lname'] = ''
        flash("Last Name Cannot contain numbers.")
        flag = 1
    if flag == 1:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pass'])
    print(pw_hash)
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s, %(Email)s,%(password_hash)s, NOW(), NOW());"
    data = {
        'first_name': request.form['Fname'],
        'last_name':  request.form['Lname'],
        'Email':  request.form['Email'],
        'password_hash': pw_hash}
    # print(query, data)
    mysql.query_db(query, data)
    query = "SELECT id FROM users WHERE email = %(Email)s;"
    data = {
        'Email': request.form['Email']
    }
    result = mysql.query_db(query, data)
    session.clear()
    session['id'] = result[0]['id']
    return redirect("/login/")  # Don't rememeber what this does


@app.route("/login/", methods=['POST', 'GET'])
def login():
    session['login'] = 1
    if 'Email' not in session:
        session['Email'] = ""
    if request.method == 'GET':
        session['Email'] = ""
        return render_template("login.html")
    
    Email = request.form['Email']
    Pass = request.form['Pass']
    if len(Email) < 1 or len(Pass) < 1:
        flash('Please fill out info to log in..')

    query = "SELECT * FROM users WHERE email = %(Email)s;"
    data = {"Email": request.form["Email"]}
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['Pass']):
            session['id'] = result[0]['id']
            return redirect('/welcome')

    flash("You could not be logged in")
    return render_template("login.html", Email=session['Email'])


@app.route("/welcome", methods=['GET'])
def welcome():
    if 'id' not in session:
        return redirect('/')
    query = "SELECT first_name FROM users WHERE id = %(id)s;"
    data = {
        'id': session['id']
    }
    result = mysql.query_db(query, data)
    Fname = result[0]['first_name']

    query = "SELECT CONCAT_WS(' ', users.first_name, users.last_name) as name, messages.id as message, DATE_FORMAT(messages.created_at, '%M %D %Y %l:%i %p') as created, messages.text as text, users.id as user FROM users join messages on users.id = messages.user_id;"
    Foobar = mysql.query_db(query)

    query = "SELECT CONCAT_WS(' ', users.first_name, users.last_name) as name, posts.id as comment, DATE_FORMAT(posts.created_at, '%M %D %Y %l:%i %p') as created, posts.text as text, posts.message_id as message  FROM users join posts on users.id = posts.user_id;"
    Chin = mysql.query_db(query)

    print("Fetched all", Foobar)
    print(Chin)
    return render_template('WelcomePage.html')


@app.route("/clear", methods=["POST"])
def finish():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
