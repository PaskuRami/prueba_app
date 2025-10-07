import streamlit as st
import pandas as pd
import plotly.express as px
#import plotly.express as px 

#Escribir en archivo csv
def writing_on_csv(dataDict):
    with open("./data/loteria.csv", mode="w", newline='\n') as file:
        data = pd.DataFrame(dataDict)
        data.to_csv(file,index=False,escapechar="\r")

def reading_from_csv():
    with open("./data/loteria.csv", mode="r") as file:
        data = pd.read_csv(file)
        return(data)

#Cambios en las tablas
def process_changes():
    editor_state = st.session_state.get("dynamic_editor_travel",{})
    edited = editor_state.get("edited_rows",{})
    added = editor_state.get("added_rows",{})
    deleted = editor_state.get("deleted_rows",{})

def cargar_viaje():
    st.subheader("Loteria")
    #df = reading_from_csv
    df = pd.read_csv("./data/loteria.csv")
    #st.dataframe(df)

    #Editable Dataframe con filas dinamicas
    edited_df = st.data_editor(
        df,
        key="dynamic_editor_travel",
        hide_index= True,
        use_container_width=True,
        num_rows="dynamic",
        on_change=process_changes        
    )
    st.button("Guardar", on_click=writing_on_csv, args=[edited_df])

    #Contar por pais grafico redondo 

    #df_count = df.groupby('proveedor').count().reset_index() 
    #fig = px.pie(df_count, values="producto", names="proveedor", title="Proveedor") 
    #st.plotly_chart(fig)

if __name__ == '__main__':
    cargar_loteria()
