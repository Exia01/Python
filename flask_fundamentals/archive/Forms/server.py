from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form


@app.route('/')
def main():
    users = (
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    )
    # print(type(users))
    # print(users[0]['first_name'])

    for i in users:
        print(i['first_name'])

    return render_template('index.html', users=users)


app.run(debug=True)
