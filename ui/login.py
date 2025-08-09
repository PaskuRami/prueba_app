#This module handles user registration, authentication, and role management. 
# It ensures that users can log in, be authenticated, and access their designated pages.

import streamlit as st

from auth.auth_manager import AuthManager
from auth.jwt_utils import generate_token, decode_token

from ui import dashboard #Make sure the dashboard module is imported correctly
from ui import viaje
from ui import inicio

auth_manager = AuthManager()

def login_page():
    st.title("Login")
    #Check if ther is already an active session
    if "auth_token" in st.session_state:
        token_data = decode_token(st.session_state["auth_token"])
        if token_data:
            st.success(f"Active session: {token_data['username']} ({token_data['role']})")
            #Allows you to log out
            if st.button("Log Out"):
                del st.session_state["auth_token"]
                st.rerun()
            #Redirects to the dashboard of the corresponding role
            if token_data["role"] == "admin":
                dashboard.admin_dashboard()
            if token_data["role"] == "Gestion":
                #st.info("Rol Gestion")
                #viaje.cargar_viaje()
                inicio.main()
            else:
                st.info("Role not supported yet.")
                return
    
    else:
        #Formulario de inicio de sesion
        username = st.text_input("User", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login", key="login_button"):
            user = auth_manager.authenticate_user(username, password)
            if user:
                token = generate_token(user["username"], user["role"])
                st.session_state["auth_token"] = token
                st.success(f"Welcome, {user['username']} ({user['role']})")
                st.rerun() #Reload to enter the active session
            else:
                st.error("Incorrect username or password")






