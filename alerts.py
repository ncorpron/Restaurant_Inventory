import streamlit as st
from utils import load_data, recalc

def alerts_page():
    st.title("🚨 Inventory Alerts")
    inventory, usage_df, months = load_data()
    filtered_inventory = recalc(inventory, months)

    low_stock_threshold = st.sidebar.slider("Low Stock Threshold", 1, 50, 10)
    low_stock = filtered_inventory[filtered_inventory["End Inventory"]<low_stock_threshold]
    if not low_stock.empty:
        st.warning("Low Stock Items")
        st.dataframe(low_stock[["Item","End Inventory","Reorder Amount","Category","Location"]])

    alert_days = st.sidebar.slider("Predictive Alert Threshold (days left)", 1, 60, 15)
    predicted_alerts = filtered_inventory[filtered_inventory["Days_Left"] < alert_days]
    if not predicted_alerts.empty:
        st.error("Items Predicted to Run Out Soon")
        st.dataframe(predicted_alerts[["Item","End Inventory","Days_Left","Predicted Reorder"]])
