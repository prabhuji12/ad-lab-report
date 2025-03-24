from flask import Flask, render_template, jsonify, request
import json
import os
import pickle
import numpy as np

app = Flask(__name__)

model_files = {
    "Logistic Regression": "logistic_regression.pkl",
    "K-Nearest Neighbors": "k_nearest_neighbors.pkl",
    "Decision Tree": "decision_tree.pkl",
    "Random Forest": "random_forest.pkl",
    "Gradient Boosting": "gradient_boosting.pkl",
    "Support Vector Machine": "support_vector_machine.pkl",
    "Naive Bayes": "naive_bayes.pkl"
}

models = {}

for name, file in model_files.items():
    if os.path.exists(file):
        with open(file, "rb") as f:
            models[name] = pickle.load(f)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template("index.html", model_names=list(models.keys()))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        selected_model = request.form["model"]

        if selected_model not in models:
            return "Error: Selected model not found"

        model = models[selected_model]
        age = int(request.form["age"])
        gender = int(request.form["gender"])
        speed = float(request.form["speed"])
        helmet = int(request.form["helmet"])
        seatbelt = int(request.form["seatbelt"])

        input_data = np.array([[age, gender, speed, helmet, seatbelt]])
        
        prediction = model.predict(input_data)[0]

        return render_template("index.html", prediction=prediction, model_names=list(models.keys()))

    except Exception as e:
        return f"Error in prediction: {str(e)}"

@app.route('/results')
def results():
    results_no_tuning = load_json('./json/results_no_tuning.json')
    results_tuned = load_json('./json/results_tuned.json')
    best_models = load_json('./json/best_hyperparameters.json')
    results_preprocessing = load_json('./json/results_preprocessing.json')
    results_pca = load_json('./json/results_pca.json')

    return render_template(
        'results.html', 
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
