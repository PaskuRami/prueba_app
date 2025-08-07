import streamlit as st
from PIL import Image 
from ui import futbol
from ui import texto

#Imagen logo pestaña navegación 
img = Image.open("logo.png") 

st.set_page_config(page_title='Mi APP', page_icon=img, layout="wide", initial_sidebar_state="collapsed") 


def main():
    st.title("Aplicacion principal")
    menu=["Inicio","Futbol","Texto","Conocenos"]
    choice=st.sidebar.selectbox("Menu", menu)

    if choice == "Inicio":
        st.subheader("Inicio")
    elif choice == "Futbol":
        #pass
        futbol.cargar_partidos()
    elif choice == "Texto":
        texto.app_texto()

if __name__ == '__main__':
    main()