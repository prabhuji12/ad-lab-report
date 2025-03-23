from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    results_no_tuning = load_json('./json/results_no_tuning.json')
    results_tuned = load_json('./json/results_tuned.json')
    best_models = load_json('./json/best_hyperparameters.json')
    results_preprocessing = load_json('./json/results_preprocessing.json')
    results_pca = load_json('./json/results_pca.json')

    return render_template(
        'index.html', 
        results_no_tuning=results_no_tuning, 
        results_tuned=results_tuned, 
        best_models=best_models,
        results_preprocessing=results_preprocessing,
        results_pca=results_pca
    )

@app.route('/notebook')
def notebook():
    return render_template('notebook.html')

if __name__ == '__main__':
    app.run(debug=True)
