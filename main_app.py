import streamlit as st
from banner import show_banner  # your banner function
from inventory import inventory_page   # import modules at the top
from charts import charts_page
from reports import reports_page
from alerts import alerts_page

st.set_page_config(page_title="Restaurant Inventory Dashboard", layout="wide")

# -----------------------------
# Initialize session state if it doesn't exist
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Inventory"  # Default page to "Inventory"

# -----------------------------
# Show banner with page-specific images
# -----------------------------
if st.session_state.page == "Inventory":
    show_banner("https://images.unsplash.com/photo-1580902145051-e8d17c3bcda9?crop=entropy&cs=tinysrgb&fit=max&ixid=MnwzNjQ4NTd8MHx8c2VhcmNofDExfHxmb29kfHx8fHx8fDE2Nzc2Nzg0NzI&ixlib=rb-1.2.1&q=80&w=1080")  # Fresh Food
elif st.session_state.page == "Charts":
    show_banner("https://images.unsplash.com/photo-1504697847147-4b8e2fa470b3?crop=entropy&cs=tinysrgb&fit=max&ixid=MnwzNjQ4NTd8MHx8c2VhcmNofDN8fHxlbnRyZWVzfGVufDB8fHx8fDE2NzcyMzA3NzA&ixlib=rb-1.2.1&q=80&w=1080")  # Entrees
elif st.session_state.page == "Reports":
    show_banner("https://images.unsplash.com/photo-1566795911-8b9bdf8e2e74?crop=entropy&cs=tinysrgb&fit=max&ixid=MnwzNjQ4NTd8MHx8c2VhcmNofDN8fHxd2luZXxlbnRyZWV8ZW58fDB8fHx8fDE2NzcyMzA4MzA&ixlib=rb-1.2.1&q=80&w=1080")  # Wine
else:
    show_banner("https://images.unsplash.com/photo-1579738207245-77ed742e5704?crop=entropy&cs=tinysrgb&fit=max&ixid=MnwzNjQ8NTd8MHx8c2VhcmNofDExfHxmb29kfHx8fHx8fDE2Nzc2Nzg0NzI&ixlib=rb-1.2.1&q=80&w=1080")  # Default Food

# -----------------------------
# Sidebar: Page Navigation
# -----------------------------
pages = ["Inventory", "Charts", "Reports", "Alerts"]
for p in pages:
    if st.sidebar.button(p, key=f"page_{p}"):
        st.session_state.page = p  # Update page state on button click

# -----------------------------
# Sidebar: Thresholds
# -----------------------------
st.sidebar.slider("Low Threshold", 0, 100, 10)
st.sidebar.slider("High Threshold", 0, 200, 50)

# -----------------------------
# Page routing
# -----------------------------
if st.session_state.page == "Inventory":
    inventory_page()
elif st.session_state.page == "Charts":
    charts_page()
elif st.session_state.page == "Reports":
    reports_page()
elif st.session_state.page == "Alerts":
    alerts_page()
