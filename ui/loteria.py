import streamlit as st
import pandas as pd
import plotly.express as px

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

def cargar_loteria():
    st.subheader("Loteria 15676")
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

    count_precio = df['precio' ].sum()
    st.info('Papeletas Navidad = 50, Papeletas Nino = 25', icon="ℹ️")
    st.write(f"Loteria Navidad: 150€, Loteria Nino: 75€, Total dinero papeletas: 225€, Total dinero recolectado: {count_precio}€")

       
    #Contar por unidades_navidad, unidades_nino, precio grafico redondo 
    df_sum_lotnav = df['unidades_navidad'].sum()
    df_sum_lotnino = df['unidades_nino'].sum()

    col3, col4 = st.columns(2)
    with col3:
        fig2 = px.pie(df, values="unidades_navidad", names="cliente", title="Papeletas Navidad")
        st.plotly_chart(fig2)
    with col4:
        fig3 = px.pie(df, values="unidades_nino", names="cliente", title="Papeletas Nino")
        st.plotly_chart(fig3)
    
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(df,x='unidades_navidad',y='unidades_navidad')
        # Añade el valor de la suma como anotación en la esquina del gráfico
        fig.update_layout(
            title=f"Total loteria Navidad: {df_sum_lotnav} papeletas",
            annotations=[
                dict(
                    x=0.5,
                    y=1.0,
                    xref='paper',
                    yref='paper',
                    text=f"Suma total: {df_sum_lotnav}",
                    showarrow=False,
                    font=dict(size=14)
                )
            ]
        )
        st.plotly_chart(fig)
    with col2:
        fig2 = px.bar(df,x='unidades_nino',y='unidades_nino')
        # Añade el valor de la suma como anotación en la esquina del gráfico
        fig2.update_layout(
            title=f"Total loteria Niño: {df_sum_lotnino} papeletas",
            annotations=[
                dict(
                    x=0.5,
                    y=1.0,
                    xref='paper',
                    yref='paper',
                    text=f"Suma total: {df_sum_lotnino}",
                    showarrow=False,
                    font=dict(size=14)
                )
            ]
        )
        st.plotly_chart(fig2)

if __name__ == '__main__':
    cargar_loteria()
