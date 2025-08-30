import streamlit as st
from utils import load_data

def alerts_page():
    st.title("Alerts Page")
    inventory = load_data()
    st.warning("This is a simulated alert for low stock items")
