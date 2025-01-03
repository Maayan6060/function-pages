import streamlit as st
import os

# Function to load and render pages dynamically
def load_page(page_name):
    page_module = __import__(f"pages.{page_name}", fromlist=[''])
    page_module.app()

# Sidebar navigation
st.sidebar.title("Navigation")
page_choices = ["differential", "integral"]
selected_page = st.sidebar.radio("Go to", page_choices)

# Load the selected page
page_mapping = {
    "differential": "differential", 
    "integral": "integral"
}
load_page(page_mapping[selected_page])
