from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({"msg": "Flask backend running"})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
