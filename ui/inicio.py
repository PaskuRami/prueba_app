import streamlit as st
from PIL import Image 
from ui import viaje
from ui import texto
from ui import maleta
from ui import streamlit_location
from auth.jwt_utils import generate_token, decode_token

#Imagen logo pestaña navegación 
img = Image.open("logo.png") 

st.set_page_config(page_title='Mi APP', page_icon=img, layout="wide", initial_sidebar_state="collapsed") 


def main():
    st.title("Aplicacion principal")
    
    menu=["Inicio","Viaje","Maleta","Conocenos","GLP Map"]
    token_data = decode_token(st.session_state["auth_token"])
    st.sidebar.success(f"Usuario: {token_data['username']} ({token_data['role']})")
    #Allows you to log out
    if st.sidebar.button("Log Out"):
        del st.session_state["auth_token"]
        st.rerun()
    choice=st.sidebar.selectbox("Menu", menu)

    if choice == "Inicio":
        st.subheader("Inicio")
    elif choice == "Viaje":
        #pass
        viaje.cargar_viaje()
    elif choice == "Maleta":
        maleta.maleta_viaje()
    elif choice == "GLP Map":
        streamlit_location.glp_maps()
    

if __name__ == '__main__':
    main()






