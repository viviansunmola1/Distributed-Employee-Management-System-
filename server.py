from flask import Flask, jsonify, request

app = Flask(__name__)
employee_data = {}

@app.route('/')
def index():
    return "Go to localhost:5000/data"

@app.route('/data', methods=['POST', 'GET'])
def process_data():
    if request.method == 'POST':
        employee = request.get_json()
        # Process the received employee data as required
        employee_data.update(employee)
        response = {'status': 'Success'}
        return jsonify(response)
    elif request.method == 'GET':
        return jsonify(employee_data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
