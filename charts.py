import streamlit as st
import plotly.express as px
from utils import load_data

def charts_page():
    st.title("Charts Page")
    inventory = load_data()
    fig = px.bar(inventory, x="Item", y="Beginning Inventory")
    st.plotly_chart(fig)
