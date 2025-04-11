import streamlit as st
import time

st.title("Caching")
st.write("Caching is used to store the result of a function so that it can be reused without recomputing it on refresh during specific time.")
st.write("Caching is useful for expensive computations, API calls, or loading large datasets.")
st.write("Caching is specific for user, web-browser and tab.")
st.write("On refresh tab, cache will not change.")


st.subheader("here only for first time it will take time to load data, after that it will not taking time on refresh till 30sec.")

# @st.cache_data # Cache time = infinite
@st.cache_data(ttl=30) # Cache time = 60 seconds
def fetch_data():
    time.sleep(3)
    return {"data": "this is a cached data"}


st.write("fetching data...")
data = fetch_data()
st.write(data)