import streamlit as st
import os 
import pandas as pd
import numpy as np

st.title("Layouts")

t1,t2,t3 = st.tabs(['Tab 1','Tab 2','Tab 3'])

with t1:
    st.write("This is Tab 1")
with t2:
    st.write("This is Tab 2")
with t3:
    st.write("This is Tab 3")

c1,c2 = st.columns(2)
with c1:
    st.header("This is column 1")
with c2:
    st.header("This is column 2")

with st.container(border=True):
    st.header("This is container")

placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content")
if st.button("Update Placeholder"):
    placeholder.write("This is updated placeholder")

with st.expander("Expand for more"):
    st.write("additional info 1")
    st.write("additional info 2")
    st.write("additional info 3")

st.button("Hover here",help="This is Help attribute")

    
