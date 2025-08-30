import streamlit as st
import plotly.express as px
from utils import load_data, recalc
from banner import show_banner

def charts_page():
    st.title("📊 Charts & Inventory Insights")
    inventory, usage_df, months = load_data()
    filtered_inventory = recalc(inventory, months)

    # Stock status
    low_stock_threshold = st.sidebar.slider("Low Stock Threshold", 1, 50, 10)
    def stock_status(val):
        if val < low_stock_threshold:
            return "🟥 Low"
        elif val < low_stock_threshold * 2:
            return "🟨 Medium"
        else:
            return "🟩 High"
    filtered_inventory["Stock_Status"] = filtered_inventory["End Inventory"].apply(stock_status)

    selected_status = st.radio("Highlight a stock status:", ["All", "🟥 Low", "🟨 Medium", "🟩 High"], horizontal=True)
    display_df = filtered_inventory if selected_status=="All" else filtered_inventory[filtered_inventory["Stock_Status"]==selected_status]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items", len(display_df))
    col2.metric("Avg End Inventory", round(display_df["End Inventory"].mean(),1))
    col3.metric("Most Critical Item", display_df.loc[display_df['End Inventory'].idxmin(),'Item'])

    st.dataframe(display_df[["Item","Category","Location","End Inventory","Stock_Status","Suggested_Order"]])

    # Charts
    st.subheader("Usage vs End Inventory")
    fig1 = px.bar(filtered_inventory, x="Item", y=["Usage","End Inventory"], barmode="group", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Stock Value Distribution")
    fig2 = px.pie(filtered_inventory, names="Item", values="Stock Value", hole=0.3, color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig2, use_container_width=True)

