import streamlit as st


st.set_page_config(
    page_title="Multipage App",
    layout="wide"
)
st.title("Main Page")
st.sidebar.success("select page from above")


if "input" not in st.session_state:
    st.session_state['input'] = ''

input = st.text_input("give input text that accessible on every pages: ",st.session_state['input'])
if st.button("Submit"):
    st.session_state['input'] = input
    st.write("you have entered: ",input)


# Add custom CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1563832528262-15e2bca87584?q=80&w=2019&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
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
    
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        # MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        # footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# sidebar_bg = ""  # Web URL
sidebar_bg = "https://images.unsplash.com/photo-1736942145358-ff047387450b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"  # Web URL

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("{sidebar_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color:white; 
        text-shadow: 0.3px 0.3px 0.3px white,0.6px 0.6px 1px black;

        
    }}
    </style>
    """,
    unsafe_allow_html=True
)