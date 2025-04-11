import streamlit as st
import os 
import pandas as pd
import numpy as np

st.title("Session State: ")
st.write("when we click button at that every time app is re-running. To stop it we have use it.")
st.write("sessoin_state is specific for user,web-browser and tab.")
st.write("On refresh tab,  sessoin_state will change.")

st.subheader("Without Session State")
counter = 0
st.write(f"counter value: {counter}")
if st.button("Increment"):
    counter += 1
    st.write(f"counter value: {counter}")


st.subheader("With Session State")
if "counter1" not in st.session_state:
    st.session_state.counter1 = 0

if st.button("Increment counter"):
    st.session_state.counter1 += 1

if st.button("Reset"):
    st.session_state.counter1 =0
    
st.write(f"counter value: {st.session_state.counter1}")