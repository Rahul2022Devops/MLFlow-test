from flask import Flask, render_template, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

    try:
        if operation == 'add':
            result = add(num1, num2)

        elif operation == 'subtract':
            result = subtract(num1, num2)

        elif operation == 'multiply':
            result = multiply(num1, num2)

        elif operation == 'divide':
            result = divide(num1, num2)

        else:
            return jsonify({'error': 'Invalid operation'})

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
