import pandas as pd
import numpy as np
import streamlit as st

# Cache the load_data() function to avoid recalculating every time
@st.cache_data
def load_data():
    data = {
        "Item": ["Chicken Breast", "Beef", "Rice", "Milk", "Lettuce", "Eggs", "Cheese", "Tomatoes", "Fish", "Yogurt"],
        "Category": ["Meat", "Meat", "Grain", "Dairy", "Vegetable", "Dairy", "Dairy", "Vegetable", "Meat", "Dairy"],
        "Location": ["Downtown", "Downtown", "Uptown", "Uptown", "Downtown", "Downtown", "Uptown", "Uptown", "Downtown", "Uptown"],
        "Beginning Inventory": [50, 40, 10, 30, 20, 60, 25, 15, 20, 35],
        "Price_per_Unit": [5.0, 7.0, 1.0, 2.5, 1.5, 0.3, 3.0, 2.0, 6.0, 1.0],
        "Stock Value": [250, 280, 10, 75, 30, 18, 75, 30, 120, 35],
        "Usage": [10, 5, 20, 12, 8, 18, 10, 6, 9, 15],
        "End Inventory": [40, 35, 0, 18, 12, 42, 15, 9, 11, 20],
        "Avg_Usage": [8, 6, 18, 10, 7, 15, 12, 8, 10, 12],
        "Days_Left": [4, 7, 0, 2, 3, 2, 1, 1, 3, 5],
        "Suggested_Order": [20, 15, 30, 15, 10, 20, 15, 10, 20, 15],
        "Reorder Amount": [20, 15, 30, 15, 10, 20, 15, 10, 20, 15],
        "Predicted Reorder": [25, 15, 35, 15, 10, 25, 15, 10, 20, 15]
    }
    df = pd.DataFrame(data)
    months = ["January", "February", "March"]  # example
    usage_df = pd.DataFrame()  # placeholder if needed
    return df, usage_df, months


# Cache the recalc() function as well if it's performing heavy calculations
@st.cache_data
def recalc(df, months):
    # Placeholder: you can add any recalculation logic if needed
    return df
