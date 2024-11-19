from flask import Flask, request, jsonify
from nltk import word_tokenize

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.json
    sentence = data.get('sentence', '')

    if not sentence:
        return jsonify ({'error': 'No sentence prodvided'}), 400
    
    tokens = word_tokenize(sentence)
    return jsonify({'tokens':tokens})


@app.route('/hello')
def hello():
    return 'hello world, I use python!', 200

if __name__ == "__main__":
    app.run(debug=True)