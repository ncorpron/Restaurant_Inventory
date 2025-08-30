import streamlit as st

def show_banner(image_url):
    st.markdown(
        f"""
        <style>
        .food-banner {{
            background-image: url('{image_url}');
            background-size: cover;
            background-position: center;
            height: 220px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        </style>
        <div class="food-banner"></div>
        """,
        unsafe_allow_html=True
    )
