import streamlit as st

def app_texto():
    st.subheader("Seccion de texto")
    st.write("VAmos a escribir")
    st.success("Todo salio bien")

if __name__ == '__main__':
    app_texto()