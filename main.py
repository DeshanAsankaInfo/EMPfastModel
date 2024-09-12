from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load the trained multi-output model
model = joblib.load('employee_multioutput_model.pkl')


# Define the request body using Pydantic BaseModel
class EmployeeInput(BaseModel):
    last_evaluation: float  # Last evaluation score (0.0 - 1.0)
    number_project: int  # Number of projects (1 - 10)
    average_montly_hours: int  # Average monthly hours (80 - 320)
    time_spend_company: int  # Time spent in company (in years)
    salary: str  # Salary level: low, medium, high


# Map salary levels to numeric values
salary_map = {'low': 0, 'medium': 1, 'high': 2}


# Define the FastAPI POST method to handle predictions
@app.post("/predict/")
async def predict(employee: EmployeeInput):
    try:
        # Convert salary level to numeric value
        salary_numeric = salary_map[employee.salary.lower()]

        # Create a dataframe for the input data
        input_data = pd.DataFrame([[employee.last_evaluation, employee.number_project, employee.average_montly_hours,
                                    employee.time_spend_company, salary_numeric]],
                                  columns=['last_evaluation', 'number_project', 'average_montly_hours',
                                           'time_spend_company', 'salary'])

        # Make predictions using the trained model
        predictions = model.predict(input_data)
        predicted_satisfaction, predicted_performance, predicted_promotion, predicted_attrition_risk = predictions[0]

        # Return predictions as a JSON response
        return {
            "Predicted Satisfaction": round(predicted_satisfaction, 2),
            "Explanation Satisfaction": "A higher value means the employee is more satisfied with their work environment.",
            "Predicted Performance": round(predicted_performance, 2),
            "Explanation Performance": "A higher score indicates stronger performance in recent evaluations.",
            "Predicted Promotion Likelihood": round(predicted_promotion, 2),
            "Explanation Promotion Likelihood": "A higher value suggests the employee has a better chance of being promoted.",
            "Predicted Attrition Risk": round(predicted_attrition_risk, 2),
            "Explanation Attrition Risk": "A higher score indicates the employee is more likely to leave the company."
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Example route to test if the API is running
@app.get("/")
def read_root():
    return {"message": "Employee Prediction API is running."}
