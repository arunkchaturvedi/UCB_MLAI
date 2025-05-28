import joblib # For saving and loading the model
from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# Global variable to hold the loaded model
model = None

def load_model():
    """Load the trained model from disk."""
    global model
    global N_FEATURES_EXPECTED
    model_path = '/models/xgboost_classifier.joblib'
    try:
        model = joblib.load(model_path)
        if hasattr(model, 'n_features_in_'):
            N_FEATURES_EXPECTED = model.n_features_in_
        print(f"Model loaded successfully from {model_path}. Expecting {N_FEATURES_EXPECTED} features.")
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}.")
        model = None 
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

@app.route('/')
def home():
    """Renders the home page with a form for input."""
    # Pass the number of features to the template
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles prediction requests."""
    if model is None:
        return jsonify({'error': 'Model not loaded.'}), 500

    try:
        # Get data from the POST request (form)
        # The form should send feature0, feature1, ..., featureN-1
        input_features = []
        for i in range(N_FEATURES_EXPECTED):
            feature_value = request.form.get(f'feature{i}')
            if feature_value is None:
                return jsonify({'error': f'Missing feature{i}'}), 400
            try:
                input_features.append(float(feature_value))
            except ValueError:
                return jsonify({'error': f'Invalid value for feature{i}. Must be a number.'}), 400

        # Convert features to a numpy array, reshape for a single sample
        final_features = np.array(input_features).reshape(1, -1)

        # Make prediction
        prediction_proba = model.predict_proba(final_features) # Probabilities for each class
        prediction = model.predict(final_features) # Class label

        # Prepare response
        # prediction_proba[0][1] is the probability of the positive class (class 1)
        # prediction[0] is the predicted class label (0 or 1)
        response = {
            'predicted_class': int(prediction[0]),
            'probability_class_0': float(prediction_proba[0][0]),
            'probability_class_1': float(prediction_proba[0][1])
        }
        return jsonify(response)

    except Exception as e:
        print(f"Error during prediction: {e}") # Log the error
        return jsonify({'error': f'Error during prediction: {str(e)}'}), 500

if __name__ == '__main__':
    # Load the model for the Flask app
    load_model() # Load the model when the app starts

    # Run the Flask app
    # Ensure the 'templates' folder exists in the same directory as this script
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("Created 'templates' directory. Please put your index.html file there.")

    print(f"Starting Flask app. Open your browser to http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0') # host='0.0.0.0' makes it accessible on your network

