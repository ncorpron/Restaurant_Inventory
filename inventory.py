import streamlit as st
from utils import load_data, recalc

def inventory_page():
    st.title("📦 Inventory Overview")
    inventory, usage_df, months = load_data()
    filtered_inventory = recalc(inventory, months)
    
    st.dataframe(filtered_inventory[["Item","Category","Location","End Inventory","Suggested_Order"]])
