from flask import (
    Flask,
    request,
)

from calculator import Calculator

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add():
    return operation('add', 2)

@app.route('/api/subtract', methods=['POST'])
def subtract():
    return operation('subtract', 3)

@app.route('/api/multiply', methods=['POST'])
def multiply():
    return operation('multiply', 4)

@app.route('/api/divide', methods=['POST'])
def divide():
    return operation('divide', 6)
    
@app.route('/api/square', methods=['POST'])
def square():
    return operation('square', 6)

def operation(method, num_factors):
    factors = []
    if num_factors == 2:
        factors.append(float(request.json.get('x')))
        factors.append(float(request.json.get('y')))

    return str(getattr(Calculator, method)(*factors))


app.run(host='0.0.0.0', port=8080)
