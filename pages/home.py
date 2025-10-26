import streamlit as st
import page1  # ou chamar uma função de page1
import dieta

page = st.sidebar.selectbox("Escolha a página", ["Geral", "Dieta"])
if page == "Geral":
    page1.show()
elif page == "Dieta":
    dieta.show()

