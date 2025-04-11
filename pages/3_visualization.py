import streamlit as st
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualization")

data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

st.dataframe(data)

st.subheader("st.area_chart")
st.area_chart(data)

st.subheader("st.bar_chart")
st.bar_chart(data)

st.subheader("st.line_chart")
st.line_chart(data)

st.subheader("st.pyplot")
fig, ax = plt.subplots()
ax.plot(data['A'],label='A')
ax.plot(data['B'],label='B')
ax.plot(data['C'],label='C')
ax.set_title("subplot")
ax.legend()
st.pyplot(fig)

st.subheader("st.scatter_chart")
scatter_data = pd.DataFrame({
    'x':np.random.randn(100),
    'y':np.random.randn(100),
    'z':np.random.randn(100),
    'a':np.random.randn(100),
})
st.scatter_chart(scatter_data)

st.subheader("st.map")
map_data = pd.DataFrame(
    np.random.randn(100,2) / [50,50] + [37.76,-122.4],
    columns=['lat','lon']
)
st.map(map_data)




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