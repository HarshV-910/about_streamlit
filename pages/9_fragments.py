import streamlit as st

st.title("Fragments")
st.write("Fragments are used to create reusable components in Streamlit.")
st.write("They are useful for creating custom components, layouts, and widgets.")
st.write("Fragments are defined using the `st.fragment` function.")
st.divider()
st.write("By this we can rerun some specific part of the code without reloading the entire app.")
st.write("if we change the value of any widget in the fragment, it will re run only that fragment.")
st.divider()

@st.fragment()
def toggle():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter Text...")
    # st.rerun(scope="fragment") # default scope is "fragment"
    # st.rerun(scope="page")
    # st.rerun(scope="app")
    # st.rerun(scope="all")
    # st.rerun(scope="session")
    # st.rerun(scope="user")
    # st.rerun(scope="browser")
    # st.rerun(scope="tab")

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload Image")
    new_cols[2].selectbox("Select Box", ["Option 1", "Option 2", "Option 3"])
    new_cols[3].slider("Select Value", 0,100,50)
    new_cols[4].text_input("Enter Text")

toggle()

filter_and_file()

st.selectbox("Select", ["1", "2", "3"],None)