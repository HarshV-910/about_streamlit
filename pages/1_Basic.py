import streamlit as st
import os 
import pandas as pd
import time


st.title("Basic")

st.write("you have entered input at main page: ",st.session_state['input'])


st.title("hello st.title")
st.write("this is st.write")
st.header("this is st.header")
st.subheader("this is st.subheader")
st.markdown("this is st.markdown")
st.caption("this is st.caption")
st.write("`this is st.write under backtick`")

code_example = '''
def greet(name):
    print("Hello again, ",name )
'''
"this is st.code"
st.code(code_example,language='python')
"this is st.divider"
st.divider( )

if st.button("this is st.button1"):
    st.write("button is pressed")

if st.button("this is st.balloons"):
    st.balloons()

if st.button("this is st.snow"):
    st.snow()

if st.button("this is st.progress"):
    st.progress(75)    

if st.button("this is st.loading"):
    with st.spinner("Loading..."):   # Animated spinner
        time.sleep(2)
    st.success("Done! ✅")

if st.button("this is st.audio"):
    st.audio("audio1.mp3")

if st.button("this is st.help"):
    st.help("this is st.help")

st.success("this is st.success")
st.info("this is st.info")
st.warning("this is st.warning")
st.error("this is st.error")
st.exception("this is st.exception")



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