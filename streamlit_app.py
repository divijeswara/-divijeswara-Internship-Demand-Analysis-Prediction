import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("safe_salary_predictor.pkl")

# App title
st.title("Starting Salary Predictor")

# Collect user input
age = st.slider("Age", 18, 40, 22)
gpa = st.slider("University GPA", 0.0, 4.0, 3.0)
sat_score = st.number_input("SAT Score", 400, 1600, 1200)
ranking = st.number_input("University Ranking", 1, 500, 100)
internships = st.slider("Internships Completed", 0, 10, 2)
projects = st.slider("Projects Completed", 0, 20, 5)
certifications = st.slider("Certifications", 0, 10, 2)
soft_skills = st.slider("Soft Skills Score (1–10)", 1, 10, 6)
networking = st.slider("Networking Score (1–10)", 1, 10, 5)

# Prepare input for prediction (order must match model training)
input_data = np.array([[
    age,
    gpa,
    sat_score,
    ranking,
    internships,
    projects,
    certifications,
    soft_skills,
    networking
]])

# Predict and display result
if st.button("Predict Starting Salary"):
    predicted_salary = model.predict(input_data)[0]
    st.success(f"Estimated Starting Salary: ₹{int(predicted_salary):,}")
