from flask import Flask, render_template, request, redirect, session
from random import randint
import datetime
app = Flask(__name__)
app.secret_key = "uncle"

from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('friendsdb')
# now, we may invoke the query_db method
# print("all the First Names", mysql.query_db("SELECT * FROM friends;"))


@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends=all_friends)

@app.route('/create_friend', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
