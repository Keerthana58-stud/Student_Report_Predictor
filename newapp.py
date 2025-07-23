import streamlit as st
import requests
import joblib
import os

st.set_page_config(page_title="Student Pass/Fail Predictor")

st.title("Student Pass/Fail Predictor")

st.write("Enter marks for 3 Subjects to predict whether the student will Pass or Fail")

marks1 = st.number_input("Marks in Maths", min_value=0, max_value=100,value=50)
marks2 = st.number_input("Marks in Science", min_value=0, max_value=100,value=50)
marks3 = st.number_input("Marks in English", min_value=0, max_value=100,value=50)


features=[marks1,marks2,marks3]

model = joblib.load(open("api\\model.pkl", "rb"))


if st.button("Predict Result"):

    response=requests.post("http://127.0.0.1:8000/predict", json={'features': features})
    if response.status_code == 200:
        result = response.json()["prediction"]
        if result == 1:
            st.success("✅ Student Passed")
        else:
            st.error("❌ Student Failed")
    else:
        st.error(f"⚠️ API Error: {response.status_code}")
    # prediction = model.predict(features)[0]

    # if prediction==1:
    #     st.success("Passed")
    # else:
    #     st.error("Failed")

