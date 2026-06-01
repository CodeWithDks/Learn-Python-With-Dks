from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

history = []

def addition(num1, num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):

    if num2 !=0:
        return num1 / num2 # return division value
    else:
        return None
    
def power(num1,num2):
    return num1**num2

def modulus(num1,num2):
    if num2 != 0:
        return num1%num2
    else:
        return None

def floor_division(num1,num2):
    if num2 != 0:
        return num1//num2
    else:
        return None
    
def format_number(n):
    return int(n) if n == int(n) else n

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    operation = data["operation"]
    result = None

    operations = {
    "+": addition,
    "-": subtraction,
    "**": power,
    "*": multiplication,
    "/": division,
    "%": modulus,
    "//": floor_division
    }

    if operation in ["/", "//", "%"] and num2 == 0:
      return jsonify({"error": "Cannot perfom this operation."})
    
    result = operations[operation](num1, num2)

    result = round(result, 2)
    result = format_number(result)   # format AFTER rounding
    history.append(f"{format_number(num1)} {operation} {format_number(num2)} = {result}")
    return jsonify({"result": result, "history": history})

if __name__ == "__main__":
    app.run(debug=True)