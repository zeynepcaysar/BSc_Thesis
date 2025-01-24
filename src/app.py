from flask import Flask, render_template, request
import joblib
import numpy as np

# PAIN INTENSITY PREDICTION FOR THE CURRENT MIGRAINE


# Load the trained model: GB model - pain intensity prediction - short dataset
model = joblib.load('/data/caysar9/notebooks/zeynep-caysar-bachelor-thesis/src/predictive_modeling/short_dataset_models/gb_model_short_dataset_pain_intensity.pkl')

# Initialize the Flask app
app = Flask(__name__)

# Map pain intensity classes
pain_classes = {1: "Low", 2: "Medium", 3: "High"}


# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input and validate 
        input_data = {}
        for field in [
            'trigger_lack_physical_activity', 'trigger_physical_activity',
            'trigger_poor_sleep', 'trigger_stress', 'reported_anxiety', 'reported_depression'
        ]:
            input_data[field] = request.form.get(field)
            if input_data[field] not in ['0', '1']:
                return render_template('index.html', error=f"Error: {field.replace('_', ' ').capitalize()} must be 0 or 1.")
            input_data[field] = int(input_data[field])

        for field in [
            'sleep_duration_hours', 'sleep_duration_past_7_days',
            'migraine_attacks_past7days', 'mean_migraine_duration_past7days', 'total_physical_activity'
        ]:
            try:
                input_data[field] = float(request.form.get(field))
            except ValueError:
                return render_template('index.html', error=f"Error: {field.replace('_', ' ').capitalize()} must be a number.")

        try:
            input_data['age'] = int(request.form.get('age'))
        except ValueError:
            return render_template('index.html', error="Error: Age must be an integer.")

        
        features = [
            input_data['trigger_lack_physical_activity'], input_data['trigger_physical_activity'],
            input_data['trigger_poor_sleep'], input_data['trigger_stress'], input_data['sleep_duration_hours'],
            input_data['sleep_duration_past_7_days'], input_data['age'], input_data['migraine_attacks_past7days'],
            input_data['mean_migraine_duration_past7days'], input_data['total_physical_activity'],
            input_data['reported_anxiety'], input_data['reported_depression']
        ]
        input_array = np.array([features])

        # Make prediction
        print("Model Class Order:", model.classes_)
        model_classes = model.classes_  
        pain_classes = {model_classes[i]: name for i, name in enumerate(["Low", "Medium", "High"])}
        print("Adjusted Pain Classes:", pain_classes)

        # Predict pain intensity class
        pain_class_label = model.predict(input_array)[0]  # --> Predicted class
        pain_class_name = pain_classes[pain_class_label]  
        print(f"Predicted Class Label: {pain_class_label} ({pain_class_name})")

        # Get probabilities for all classes
        probabilities = model.predict_proba(input_array)[0]
        print(f"Probabilities for all classes: {probabilities}")

        # Get probability for the predicted class
        predicted_class_index = list(model_classes).index(pain_class_label)  
        probability = probabilities[predicted_class_index] * 100  # Converting to percentage
        print(f"Selected Probability for Predicted Class: {probability:.2f}%")

        probability = max(probability, 0.01)



        # Recommendations based on pain intensity class
        if pain_class_label == 1:
            recommendation = (
                "Good news! Your predicted pain intensity is Low. "
                "To maintain this, focus on managing stress, getting adequate sleep, staying hydrated, and leading an active lifestyle."
            )
        elif pain_class_label == 2:
            recommendation = (
                "Your predicted pain intensity is Medium. "
                "Consider identifying and managing triggers like stress or poor sleep. "
                "Maintain hydration and a balanced routine, and practice relaxation techniques."
            )
        else:
            recommendation = (
                "Your predicted pain intensity is High. "
                "Focus on reducing stress, resting in a dark and quiet room, and consulting a healthcare provider if needed. "
                "Pain relief methods like cold compresses or prescribed medications may help."
            )

        return render_template('result.html', prediction=pain_class_name, probability=round(probability, 2),recommendation=recommendation
        )

    except Exception as e:
        print("An error occurred:", e)
        return render_template('index.html', error=f"Unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
