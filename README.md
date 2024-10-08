# Employee Performance & Satisfaction Prediction API

This is a FastAPI-based web application that predicts employee performance, satisfaction, promotion likelihood, and attrition risk based on several employee data points.

The API accepts employee details as input and returns predictions for the following:

- **Predicted Satisfaction**: Employee satisfaction score.
- **Predicted Performance**: Performance score in recent evaluations.
- **Predicted Promotion Likelihood**: Likelihood of the employee being promoted.
- **Predicted Attrition Risk**: Likelihood of the employee leaving the company.

## Features

- 🌐 **API** built with **FastAPI** framework.
- 🔮 **Multi-output Prediction**: Predicts multiple outcomes related to employee performance and well-being.
- 🚀 Deployed on **Heroku** for public access.
- 📄 Automatically generated **Swagger** UI for API documentation and testing.

## Tech Stack

- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Joblib**: Library used to load the pre-trained model.
- **Pandas**: For handling input data.
- **Scikit-learn**: For the pre-trained machine learning model.
- **Heroku**: For deployment.

## API Endpoints

### 1. Root Endpoint

**GET** `/`

This is a basic endpoint to verify that the API is running.

- **Response**:

```json 
{
  "message": "Employee Prediction API is running."
}
```
### 2. Predict Employee Outcomes
**POST** `/predict/`
This endpoint accepts employee data and returns predictions for satisfaction, performance, promotion likelihood, and attrition risk.

- **Request Body:**
{
  "last_evaluation": 0.8,
  "number_project": 5,
  "average_montly_hours": 150,
  "time_spend_company": 3,
  "salary": "medium"
}

- **Response:**
{
  "Predicted Satisfaction": 0.75,
  "Explanation Satisfaction": "A higher value means the employee is more satisfied with their work environment.",
  "Predicted Performance": 0.85,
  "Explanation Performance": "A higher score indicates stronger performance in recent evaluations.",
  "Predicted Promotion Likelihood": 0.50,
  "Explanation Promotion Likelihood": "A higher value suggests the employee has a better chance of being promoted.",
  "Predicted Attrition Risk": 0.40,
  "Explanation Attrition Risk": "A higher score indicates the employee is more likely to leave the company."
}

**Input Parameters**
- last_evaluation: Employee's last evaluation score (0.0 - 1.0).
- number_project: Number of projects assigned to the employee (1 - 10).
- average_montly_hours: The employee's average monthly work hours (80 - 320).
- time_spend_company: Number of years the employee has spent at the company.
- salary: The employee's salary level: low, medium, or high.


## Medium Documentation
**Medium Link** 
https://medium.com/@deshanasanka.info/how-to-deploy-a-fastapi-machine-learning-application-in-heroku-9e04424cd3fc
