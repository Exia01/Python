@app.route('/createUser', methods=['POST'])
def create():
    # include some logic to validate user input before adding them to the database!
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    print(pw_hash)  
    # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'
    # be sure you set up your database so it can store password hashes this long (60 characters)
    query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password_hash)s);"
    # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "username" : request.form['username'],
             "password_hash" : pw_hash }
    mysql.query_db(query, data)
    # never render on a post, always redirect!
    return redirect("/")


    @app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    query = "SELECT * FROM users WHERE username = %(username)s;"
    data = { "username" : request.form["username"] }
    result = mysql.query_db(query, data)
    if result:
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, for this approach, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            # if we get True after checking the password, we may put the user id in session
            session['userid'] = result[0]['id']
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by username or if the passwords don't match,
    # flash an error message and redirect back to a safe route
    flash("You could not be logged in")
    return redirect("/")