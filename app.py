from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    results = load_json('results.json')
    best_models = load_json('best_models.json')
    return render_template('index.html', results=results, best_models=best_models)

@app.route('/notebook')
def notebook():
    return render_template('notebook.html')

@app.route('/api/results')
def api_results():
    return jsonify(load_json('results.json'))

@app.route('/api/best_models')
def api_best_models():
    return jsonify(load_json('best_models.json'))

if __name__ == '__main__':
    app.run(debug=True)
