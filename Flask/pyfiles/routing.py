
from flask import Flask
app = Flask(__name__)

print(__name__)


@app.route('/
index')
def index():
    return "Main page bruh"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/flask')
def Hiflask():
    return "Hi Flask"


@app.route('/say/michael')
def michael():
    return "Hi Jimmy!"


@app.route('/repeat/35/hello')
def ellow():
    return('Hello' * 35)


@app.route('/repeat/99/problems')
def whatvs():
    return('hi' * 99)


app.run(debug=True)
# if __name__ == "__main__":
