import streamlit as st
import os 
import pandas as pd

st.title("DataFrame")

df = pd.DataFrame({
    'name':['bob','alice','raj','rinku'],
    'age':[23,43,22,32],
    'occupation':['engineer','doctor','artist','thef']
})
st.subheader("dataframe")
st.dataframe(df)

st.subheader("editable dataframe")
st.data_editor(df)

st.subheader("static dataframe")
st.table(df)

st.subheader("metrics")
st.metric(label="total row",value=len(df))
st.metric(label="average age",value=round(df['age'].mean(),1))



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