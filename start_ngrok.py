import os
from pyngrok import ngrok

# Read token from environment variable
NGROK_TOKEN = os.getenv("NGROK_AUTHTOKEN")

if NGROK_TOKEN:
    ngrok.set_auth_token(NGROK_TOKEN)
    public_url = ngrok.connect(8501)
    print("Your Streamlit app is live at:", public_url)
else:
    print("No NGROK_AUTHTOKEN found. Ngrok will not run.")
