import streamlit as st
from banner import show_banner  # your banner function
from Inventory import inventory_page   # import modules at the top
from Charts import charts_page
from Reports import reports_page
from Alerts import alerts_page

st.set_page_config(page_title="Restaurant Inventory Dashboard", layout="wide")

# -----------------------------
# Show banner at the top
# -----------------------------
show_banner()

# -----------------------------
# Initialize session state
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Inventory"

# -----------------------------
# Sidebar: Page Navigation
# -----------------------------
pages = ["Inventory","Charts","Reports","Alerts"]
for p in pages:
    if st.sidebar.button(p, key=f"page_{p}"):
        st.session_state.page = p

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
