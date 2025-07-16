import streamlit as st
import numpy as np
import joblib

model = joblib.load('salary_predictor.pkl')

st.title("Starting Salary Predictor")

age = st.slider("Age", 18, 40, 25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
gpa = st.slider("University GPA", 0.0, 4.0, 3.0)
sat = st.slider("SAT Score", 400, 1600, 1100)
ranking = st.number_input("University Ranking", min_value=1, max_value=1000, value=250)
internships = st.slider("Internships Completed", 0, 10, 2)
projects = st.slider("Projects Completed", 0, 20, 5)
certs = st.slider("Certifications", 0, 10, 2)
soft_skills = st.slider("Soft Skills Score (1–10)", 1, 10, 7)
networking = st.slider("Networking Score (1–10)", 1, 10, 5)
field = st.selectbox("Field of Study", ['Arts', 'Law', 'Medicine', 'Computer Science', 'Engineering', 'Business', 'Mathematics'])

gender_map = {"Male": 1, "Female": 0, "Other": 2}
field_map = {'Arts': 0, 'Law': 1, 'Medicine': 2, 'Computer Science': 3, 'Engineering': 4, 'Business': 5, 'Mathematics': 6}

input_data = np.array([[
    age,
    gender_map[gender],
    gpa,
    sat,
    ranking,
    field_map[field],
    internships,
    projects,
    certs,
    soft_skills,
    networking
]])

prediction = model.predict(input_data)[0]
st.success(f"Estimated Starting Salary: ₹{int(prediction):,}")
