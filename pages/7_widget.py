import streamlit as st
import os

st.title("This is a widget page")

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""


def toggle_checkbox():
    st.session_state.checkbox = not st.session_state.checkbox


st.checkbox("Check me", value=st.session_state.checkbox, on_change=toggle_checkbox)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something:",value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"You entered: {user_input}")
