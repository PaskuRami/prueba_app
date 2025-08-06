from ui import dashboard
from ui import login
import streamlit as st
import base64
#Initial configuration
st.set_page_config(page_title="User auth", layout="wide")

#Function to encode image as base64 to set as background
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#Encode the background image
img_base64 = get_base64_of_bin_file('fondo.jpg')

#Set the background image using the encoded base64 string
st.markdown(
    f"""
    <style>
    .stApp{{
        background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True    
)

if __name__ == "__main__":
    login.login_page()   #If no token, show the login page





