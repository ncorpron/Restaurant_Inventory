import streamlit as st
from inventory import inventory_page
from charts import charts_page
from reports import reports_page
from alerts import alerts_page

st.set_page_config(page_title="Restaurant Inventory Dashboard", layout="wide")



import streamlit as st

def show_banner():
    st.markdown(
        """
        <style>
        .food-banner {
            background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836');
            background-size: cover;
            background-position: center;
            height: 220px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        </style>
        <div class="food-banner"></div>
        """,
        unsafe_allow_html=True
    )





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
