import streamlit as st
from utils import load_data

def inventory_page():
    st.title("Inventory Page")
    inventory = load_data()
    st.dataframe(inventory)
