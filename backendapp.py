from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask running successfully"

@app.route('/api')
def api():
    return jsonify({"message":"Initial API response"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Branch kur started
