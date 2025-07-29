import streamlit as st
import pandas as pd

def cargar_partidos():
    st.subheader("Aplicacion")
    df = pd.read_csv("datosTiendaTecnologiaLatam.csv")
    st.dataframe(df)

if __name__ == '__main__':
    cargar_partidos()