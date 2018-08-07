from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form


@app.route("/index")
def index():
    return render_template("index.html")


# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
    name = request.form['name']
    print(name)
    email = request.form['email']
    print(email)
    # redirects back to the '/' route
    return redirect('/index')

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    # Here's the line that changed. We're rendering a template from a post route now.
    return render_template('success.html')


# if __name__ == "__main__":

app.run(debug=True)
