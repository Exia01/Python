from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    strawberry = request.form['strawberry']
    Raspberry = request.form['raspberry']
    Apple = request.form['apple']
    Kiwi = request.form['kiwis']
    Watermelon = request.form['Watermelon']
    firstName = request.form['fname']
    lastName = request.form['lname']
    idn = request.form['test']
    return render_template("checkout.html", straw=strawberry, ras=Raspberry, appl=Apple, kiw=Kiwi, watr=Watermelon, fname=firstName, lname=lastName, num1=int(idn))


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/checkout', methods=['POST'])
# def checkout():
#     print(request.form)
#     sum = 0
#     straw = request.form['strawberry']
#     rsp = request.form['raspberry']
#     apl = request.form['apple']
#     blk = request.form['blackberry']

#     firstname = request.form['first_name']
#     lastname = request.form['last_name']
#     id = request.form['student_id']

#     fruit = [int(straw), int(rsp), int(apl), int(blk)]
#     info = [firstname, lastname, id]
#     for i in fruit:
#         sum += fruit[i]
#     fruit.append(sum)
#     return render_template("checkout.html", arr=fruit, inf=info)
