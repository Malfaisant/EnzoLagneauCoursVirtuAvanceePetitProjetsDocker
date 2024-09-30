from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bonjour d\'App 2!'

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    name = data.get('name')
    response_message = f"Bonjour, {name}!"
    return jsonify(response_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

