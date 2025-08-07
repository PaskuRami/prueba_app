import streamlit as st
import pandas as pd
import plotly.express as px
#import plotly.express as px 


def cargar_viaje():
    st.subheader("Lista Viaje")
    df = pd.read_csv("./data/lista_viaje.csv")
    st.dataframe(df)

    #Contar por pais grafico redondo 

    df_count = df.groupby('proveedor').count().reset_index() 
    fig = px.pie(df_count, values="producto", names="proveedor", title="Proveedor") 
    st.plotly_chart(fig)

if __name__ == '__main__':
    cargar_viaje()