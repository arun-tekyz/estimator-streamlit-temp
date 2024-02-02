import streamlit as st
import requests
import json

if 'resp' not in st.session_state:
 st.session_state.resp = ''

# Streamlit app layout
st.title('App Requirement Submission')

# Create an input area
requirement = st.text_area("Write your app requirement", placeholder="Write you app requirement")

# Function to send requirement to the backend and listen for response
def post_requirement(requirement):
    url = "http://localhost:3000/estimation/generate-srs"
    headers = {"Content-Type": "application/json"}
    # Modify the data to include the user's requirement instead of fixed text
    data = json.dumps({"requirement": requirement})
    
    # Make a POST request and stream the response
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# When the submit button is clicked
if st.button('Submit'):
    if requirement:
        with st.spinner('Generating SRS'):
            response_data = post_requirement(requirement)
            st.title("Refined Requirement")
            st.write(response_data['data']['refined_requirement'])
            st.title("SRS Document")
            st.markdown(response_data['data']['srs'])
    else:
        st.warning('Please write your app requirement before submitting.')
