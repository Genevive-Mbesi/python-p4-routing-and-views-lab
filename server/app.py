#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_parameter>')
def print_string(string_parameter):
    print(string_parameter)
    return string_parameter

@app.route('/count/<int:int_parameter>')
def count(int_parameter):
    if int_parameter >= 1:
        numbers = list(range(1, int_parameter + 1))
        return "<br>".join(map(str, numbers))
    else:
        return "Invalid input. Please provide a positive integer."

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f"Result: {num1} {operation} {num2} = {result}"
    else:
        return "Invalid operation or division by zero."


if __name__ == '__main__':
    app.run(port=5555, debug=True)

