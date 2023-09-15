from flask import Flask, render_template, request
from calculator_function import basic_calc

app = Flask(__name__)

@app.route("/")
def myCalc():
    return render_template('calculator.html')

@app.route("/", methods=['POST'])
def compute():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    output = basic_calc(a,b,operation)

    return render_template('calculator.html', output_display=str(output))

if __name__ == '__main__':
    app.run(debug=True)