import streamlit as st
import os 
import pandas as pd
import numpy as np

st.title("Form Elements")


st.text("st.text")
text = st.text_input("st.text_input: ")

with st.form(key='sample_form',clear_on_submit=True):
    st.subheader("Text Input")
    text = st.text_input("st.text_input: ")
    text_area = st.text_area("st.text_area: ")

    st.subheader("Date & Time Input")
    dob = st.date_input("st.date_input: ")
    time = st.time_input("st.time_input: ")

    st.subheader("Selectors")
    choice = st.radio("st.radio",['Option 1','Option 2','Option 3','Option 4'])

    c1 = st.checkbox("st.checkbox 1")
    c2 = st.checkbox("st.checkbox 2")
    c3 = st.checkbox("st.checkbox 3")

    st.file_uploader("Upload Image")

    l = ['A','B','C','D']
    st.selectbox("st.selectbox :",l)

    st.select_slider("st.select_slider: ",options=[0,1,2,3,4,5,6,7,8,9,10])
    st.slider("st.slider: ",0,100,5,step=10)

    num1 = st.number_input('st.number_input 1', min_value=0.0, max_value=5.0, step=0.01)
    num2 = st.number_input('st.number_input 2', min_value=0, max_value=5, step=1)
    num3 = st.number_input('st.number_input 3')

    submit = st.form_submit_button(label="st.form_submit_button")
    if submit:
        if not dob or not num2:
            st.warning("fill dob and st.number_input 2")
        else:
            st.success("Form Submitted")
 
st.button("same name with different id buttons",key="btn2")
st.button("same name with different id buttons")






# Add custom CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        # background-image: url("https://images.unsplash.com/photo-1563832528262-15e2bca87584?q=80&w=2019&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-image: url("https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        # opacity: 0.5;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: -1;
    }

    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)