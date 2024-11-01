import streamlit as st
from services.database import Database
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente
import pandas as pd
import Pages.Proponente.Create as PageCreateProponente
import Pages.Proponente.Read as PageReadProponente
import Pages.Proponente.Delete as PageDeleteProponente
import Pages.Proponente.Update as PageUpdateProponente

# Inicializa o banco de dados
db = Database()
db.conectar()

st.title("Sistema Prospecção")

st.sidebar.title("Menu")
Page_Proponente = st.sidebar.selectbox('Proponente', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if Page_Proponente == 'Consultar':
    PageReadProponente.Read()

if Page_Proponente == 'Incluir':
    PageCreateProponente.IncluirProponentePage()

if Page_Proponente == 'Excluir':
    PageDeleteProponente.DeletarProponentePage()

if Page_Proponente == 'Alterar':
    PageUpdateProponente.EditarProponentePage()

# Fechar a conexão ao final
db.close()