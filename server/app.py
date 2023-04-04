#!/usr/bin/env python3
from markupsafe import escape
from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<parameter>")
def print_route(parameter):
    print(f"{parameter}")
    return f"{parameter}"


@app.route("/count/<int:parameter>")
def count(parameter):
    output = ""
    for n in range(parameter):
        output += str(n) + "\n"
    return output
    # numbers = [n for n in range(parameter)]
    # # split_numbers = "\n".join(str(numbers))
    # # return split_numbers
    # for n in numbers:
    #     while n < (len(numbers)-1):
    #         return str(n)
    # return [n for n in range(parameter)]


@app.route("/math/<int:num1><string:operation><int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f"{num1 + num2}"
    elif operation == "-":
        return f"{num1 - num2}"
    elif operation == "*":
        return f"{num1 * num2}"
    elif operation == "div":
        return f"{num1 / num2}"
    elif operation == "%":
        return f"{num1 % num2}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
