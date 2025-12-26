from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

fun_facts = [
    "Did you know? Zero is the only number that can't be divided!",
    "A 'jiffy' is an actual unit of time.",
    "The number 4 is the only number with the same amount of letters as its value.",
    "Multiplying any number by 9 and adding the digits eventually gives 9.",
    "A googol is 1 followed by 100 zeros!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    # Validate inputs
    if num1 is None or num2 is None or operation is None:
        return jsonify({"error": "Missing inputs"}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        return jsonify({"error": "Invalid number format"}), 400

    if not (1 <= num2 <= 10):
        return jsonify({"error": "Second number must be between 1 and 10"}), 400

    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Power":
            if abs(num2) > 100:
                return jsonify({"error": "Exponent too large"}), 400
            result = num1 ** num2
        elif operation == "Modulo":
            if num2 == 0:
                return jsonify({"error": "Modulo by zero"}), 400
            result = num1 % num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    fact = random.choice(fun_facts)
    return jsonify({"result": result, "fun_fact": fact})

if __name__ == '__main__':
    app.run(debug=True)