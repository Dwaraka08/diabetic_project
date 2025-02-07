import streamlit as st 
import dill
import numpy as np

st.title("Obestiy Classification")

col1,col2=st.columns(2)

with col1:

    Age=st.text_input("Enter your age:")
    Gender=st.text_input("Enter your gender(Male:1,Female:0):")
    Height=st.text_input("Entet your height:")
    Weight=st.text_input("Enter your weight:")
    BMI=st.text_input("Enter you BMI:")

    with open("diabtes_2.dill","rb") as f:
        model=dill.load(f)
with col2:
    st.image(r"obesity.png")

if st.button("Predict"):
    data=[[Age,Gender,Height,Weight,BMI]]
    data_array=np.array(data,dtype=float).reshape(1,-1)
    prediction=model.predict(data_array)
    if prediction==0:
        st.write("Normal Weight")
    elif prediction==1:
        st.write("Obese")
    elif prediction==2:
        st.write("Over Weight")
    elif prediction==3:
        st.write("Under Weight")
