import streamlit as st
from futbol import cargar_partidos
from texto import app_texto

def main():
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

if __name__ == '__main__':
    main()