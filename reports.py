import streamlit as st
from utils import load_data
import io

def reports_page():
    st.title("Reports Page")
    inventory = load_data()
    csv = inventory.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="inventory.csv")
