import streamlit as st
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente
import pandas as pd
import Pages.Proponente.Create as PageCreateProponente

def Read():
    st.title('Proponentes')
    costumerList = []

    for item in ProponenteController.SelecionarTodos():
        costumerList.append([item.nome, item.idade, item.cpf, item.orgao, item.valor_contrato])

    df = pd.DataFrame(costumerList,
     columns=['Nome', 'Idade', 'CPF', 'Órgão Público', 'Valor do Contrato'])
    
    st.dataframe(df)  # Usar dataframe para uma tabela interativa
