import streamlit as st
import requests
import os
import time

recent_queries = []

def get_data_from_backend(recent_queries):
    # Write out backend url
    backend_url = "http://backend:80/api/recent/"
    response = requests.get(backend_url)
    api_data = response.json()

    for data in api_data:
        if data not in recent_queries:
            st.sidebar.write(data.get("body", "N/A"))
            recent_queries.append(data)


def send_data_to_backend(data, recent_queries):
    # Write the path to our backend api
    backend_url = "http://backend:80/api/post/"
    # Write the payload (in this case it's our data) in json format
    payload = {"body": data}
    # Get the response code from the backend_url api
    response = requests.post(backend_url, json=payload)

    if response.status_code == 201 or response.status_code == 200:
        st.success("Success! Please wait a moment while we fetch your results.")
        time.sleep(2.5)
        get_data_from_backend(recent_queries)


    else:
        st.error("Failed to send. Please retry later.")

st.title("Summarize a Website")
st.write("Powered by ChatGPT")
st.sidebar.header("Recent Queries")

st.divider()
with st.form("get_address"):
    address = st.text_input("Please put in the web address")
    submitted = st.form_submit_button("Submit")

    if submitted and address:
        send_data_to_backend(address, recent_queries)
    elif submitted:
        for element in recent_queries:
            st.sidebar.write(element.get("body", "N/A"))
        st.warning("Please fill out the address field")
    else:
        for element in recent_queries:
            st.sidebar.write(element.get("body", "N/A"))
        st.info("Please fill out the web address provided above.")
