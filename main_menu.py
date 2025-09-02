import streamlit as st
from PIL import Image 
from futbol import cargar_partidos
from texto import app_texto

#Imagen logo pestaña navegación 
img = Image.open("logo.png") 

st.set_page_config(page_title='Mi APP', page_icon=img, layout="wide", initial_sidebar_state="collapsed") 


def main_menu():
    st.title("Aplicacion principal")
    menu=["Inicio","Futbol","Texto","Conocenos"]
    choice=st.sidebar.selectbox("Menu", menu)

    if choice == "Inicio":
        st.subheader("Inicio")
    elif choice == "Futbol":
        #pass
        cargar_partidos()
    elif choice == "Texto":
        app_texto()
    elif choice == "GLP":
        glp_map()

if __name__ == '__main__':
    main_menu()


