import streamlit as st
from utils import load_data, recalc
import io

def reports_page():
    st.title("📄 Reports")
    inventory, usage_df, months = load_data()
    filtered_inventory = recalc(inventory, months)

    csv = filtered_inventory.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download CSV", data=csv, file_name="inventory.csv")

    output = io.BytesIO()
    filtered_inventory.to_excel(output, index=False, engine='openpyxl')
    st.download_button("⬇️ Download Excel", data=output.getvalue(), file_name="inventory.xlsx")
