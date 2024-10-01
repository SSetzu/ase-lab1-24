from typing import List

from flask import Flask, request, make_response, jsonify
import random as random_utils

app = Flask(__name__, instance_relative_config=True)


class TypedArgument:
    def __init__(self, name: str, type_: type):
        self.name = name
        self.type_ = type_


def retrieve_parameters(query_arguments: List[TypedArgument]):
    values = []
    for arg in query_arguments:
        value = request.args.get(arg.name, type=arg.type_)
        if not value:
            return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST
        values.append(value)
    if len(values) == 1:
        return values[0]
    return tuple(values)


@app.route("/add")
def add():
    a, b = retrieve_parameters(
        [TypedArgument("a", float), TypedArgument("b", float)]
    )
    return make_response(jsonify(s=a + b), 200)  # HTTP 200 OK


# Endpoint /sub for subtraction which takes a and b as query parameters.
@app.route("/sub")
def sub():
    a, b = retrieve_parameters(
        [TypedArgument("a", float), TypedArgument("b", float)]
    )
    return make_response(jsonify(s=a - b), 200)  # HTTP 200 OK


# Endpoint /mul for multiplication which takes a and b as query parameters.
@app.route("/mul")
def mul():
    a, b = retrieve_parameters(
        [TypedArgument("a", float), TypedArgument("b", float)]
    )
    return make_response(jsonify(s=a * b), 200)  # HTTP 200 OK


# Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route("/div")
def div():
    a, b = retrieve_parameters(
        [TypedArgument("a", float), TypedArgument("b", float)]
    )
    return make_response(jsonify(s=a * b), 200)  # HTTP 200 OK


# Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route("/mod")
def mod():
    a, b = retrieve_parameters(
        [TypedArgument("a", float), TypedArgument("b", float)]
    )
    return make_response(jsonify(s=a % b), 200)  # HTTP 200 OK


# Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.
@app.route("/random")
def random():
    a, b = retrieve_parameters(
        [TypedArgument("a", float), TypedArgument("b", float)]
    )
    if a > b:
        return make_response("Invalid input\n", 400)
    return make_response(jsonify(s=random_utils.uniform(a, b)), 200)  # HTTP 200 OK


# upper which given the string a it returns it in a JSON all in uppercase.
@app.route("/upper")
def upper():
    try:
        a = retrieve_parameters(
            [TypedArgument("a", str)]
        )
    except ValueError:
        return make_response("Invalid input\n", 400)
    return make_response(jsonify(s=a.upper()), 200)


# lower which given the string a it returns it in a JSON all in lowercase.
@app.route("/lower")
def lower():
    try:
        a = retrieve_parameters(
            [TypedArgument("a", str)]
        )
    except ValueError:
        return make_response("Invalid input\n", 400)
    return make_response(jsonify(s=a.lower()), 200)

# concat which given the strings a and b it returns in a JSON the concatenation of them.
@app.route("/concat")
def concat():
    a, b = retrieve_parameters(
        [TypedArgument("a", str), TypedArgument("b", str)]
    )
    return make_response(jsonify(s=a + b), 200)  # HTTP 200 OK


if __name__ == "__main__":
    app.run(debug=True)
