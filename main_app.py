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
    show_banner("https://raw.githubusercontent.com/ncorpron/Restaurant_Inventory/main/assets/images/casey-lee-awj7sRviVXo-unsplash.jpg")  # Fresh Food
elif st.session_state.page == "Charts":
    show_banner("https://raw.githubusercontent.com/ncorpron/Restaurant_Inventory/main/assets/images/victoria-shes-UC0HZdUitWY-unsplash.jpg")  # Entrees
elif st.session_state.page == "Reports":
    show_banner("https://raw.githubusercontent.com/ncorpron/Restaurant_Inventory/main/assets/images/joseph-gonzalez-zcUgjyqEwe8-unsplash.jpg")  # Wine
else:
    show_banner("https://raw.githubusercontent.com/ncorpron/Restaurant_Inventory/main/assets/images/lily-banse--YHSwy6uqvk-unsplash.jpg")  # Default Food

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
