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
