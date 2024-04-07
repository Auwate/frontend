import streamlit as st
import requests
import os

def send_data_to_backend(data):
    # Write the path to our backend api
    backend_url = "http://" + os.environ.get("BACKEND_HOST") + ":80/api/post"
    # Write the payload (in this case it's our data) in json format
    payload = {"data": data}
    # Get the response code from the backend_url api
    response = requests.post(backend_url, json=payload)

    if response == 200:
        st.success("Request sent, please wait...")
    else:
        st.error("Failed to send. Please retry later.")

st.title("Summarize a Website")
st.write("Powered by ChatGPT")

st.divider()
with st.form("get_address"):
    address = st.text_input("Please put in the web address")
    submitted = st.form_submit_button("Submit")

    if submitted and address:
        send_data_to_backend(address)
    elif submitted:
        st.warning("Please fill out the address field")
    else:
        st.info("Please fill out the web address provided above.")
