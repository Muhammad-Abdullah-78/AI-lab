from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
data = pd.read_csv("student_marks_prediction_dataset.csv")

# Features & target
X = data[['StudyHours', 'Attendance', 'PreviousMarks', 'AssignmentsCompleted']]
y = data['FinalMarks']

# Train model
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['study_hours'])
    attendance = float(request.form['attendance'])
    previous_marks = float(request.form['previous_marks'])
    assignments = float(request.form['assignments'])

    prediction = model.predict([[study_hours, attendance, previous_marks, assignments]])
    result = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f"Predicted Marks: {result}")

if __name__ == "__main__":
    app.run(debug=True, port=5009)