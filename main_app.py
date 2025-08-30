import streamlit as st
from banner import show_banner  # your banner function

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
# Page routing with lazy loading
# -----------------------------
if st.session_state.page == "Inventory":
    from Inventory import inventory_page   # import only when needed
    inventory_page()
elif st.session_state.page == "Charts":
    from Charts import charts_page
    charts_page()
elif st.session_state.page == "Reports":
    from Reports import reports_page
    reports_page()
elif st.session_state.page == "Alerts":
    from Alerts import alerts_page
    alerts_page()
