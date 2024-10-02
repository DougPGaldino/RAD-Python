import streamlit as st
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente
import pandas as pd
import Pages.Proponente.Create as PageCreateProponente
import Pages.Proponente.Read as PageReadProponente

st.title("Sistema Prospecção")

st.sidebar.title("Menu")
Page_Proponente = st.sidebar.selectbox('Proponente', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if Page_Proponente == 'Consultar':
    PageReadProponente.Read()

if Page_Proponente == 'Incluir':
    PageCreateProponente.IncluirProponentePage()


