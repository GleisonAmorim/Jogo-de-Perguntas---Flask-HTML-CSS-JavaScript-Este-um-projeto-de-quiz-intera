from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

with open('perguntas.json', encoding='utf-8') as f:
    perguntas = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perguntas')
def todas_perguntas():
    return jsonify(perguntas)

if __name__ == '__main__':
    app.run(debug=True)
