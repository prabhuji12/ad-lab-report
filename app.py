from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    results_no_tuning = load_json('results_no_tuning.json')
    results_tuned = load_json('results_tuned.json')
    best_models = load_json('best_hyperparameters.json')

    return render_template(
        'index.html', 
        results_no_tuning=results_no_tuning, 
        results_tuned=results_tuned, 
        best_models=best_models
    )

@app.route('/notebook')
def notebook():
    return render_template('notebook.html')

if __name__ == '__main__':
    app.run(debug=True)
