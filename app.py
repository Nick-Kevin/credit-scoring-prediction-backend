from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enable the react front app to access this API

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/endpoint', methods=['POST'])
def handle_json():
    data = request.get_json()
    persoItems = data.get('persoItems')
    return jsonify({"received": persoItems})


# ensures the development server only starts if you run the script directly,
# preventing it from launching accidentally if the file is imported elsewhere
if __name__ == "__main__":
    app.run(debug=True, port=5000)
