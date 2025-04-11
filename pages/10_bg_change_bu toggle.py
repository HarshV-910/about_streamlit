import streamlit as st

st.set_page_config(layout="wide")

b1 = "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
b2 = "https://images.unsplash.com/photo-1563832528262-15e2bca87584?q=80&w=2019&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# ----------------------------------------------------------------------------------

st.title("Background Image Switcher")
st.write("Use the toggle in the sidebar to change backgrounds!")

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This text stays readable with the dark overlay")
    
with col2:
    st.header("Column 2")
    st.metric("Temperature", "72°F", "+2°F")

# ---------------------------------------------------------------------------------

with st.sidebar:
    if st.toggle("Switch Background"):
        current_bg = b1
    else:
        current_bg = b2

# ---------------------------------------------------------------------------------

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{current_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: -1;
    }}

    header {{visibility: hidden;}}
    </style>
    """,
    unsafe_allow_html=True
)