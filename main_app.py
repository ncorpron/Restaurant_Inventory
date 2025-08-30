import streamlit as st
from inventory import inventory_page
from charts import charts_page
from reports import reports_page
from alerts import alerts_page

st.set_page_config(page_title="Restaurant Inventory Dashboard", layout="wide")









if "page" not in st.session_state:
    st.session_state.page = "Inventory"

pages = ["Inventory","Charts","Reports","Alerts"]
for p in pages:
    if st.sidebar.button(p,key=f"page_{p}"):
        st.session_state.page = p

# Only 2 thresholds
st.sidebar.slider("Low Threshold", 0, 100, 10)
st.sidebar.slider("High Threshold", 0, 200, 50)

if st.session_state.page=="Inventory":
    inventory_page()
elif st.session_state.page=="Charts":
    charts_page()
elif st.session_state.page=="Reports":
    reports_page()
elif st.session_state.page=="Alerts":
    alerts_page()
