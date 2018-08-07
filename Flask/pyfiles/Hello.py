from flask import Flask  # Import Flask to allow us to create our app.
# Global variable __name__ tells Flask whether or not we are running the file
app = Flask(__name__)
# directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is


# The "@" symbol designates a "decorator" which attaches the following
@app.route('/')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.


if __name__ == "__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
