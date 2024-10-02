import streamlit as st
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente
import pandas as pd

st.title("Sistema Prospecção")

st.sidebar.title("Menu")
Page_Proponente = st.sidebar.selectbox('Proponente', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if Page_Proponente == 'Consultar':
    st.title('Proponentes')
    costumerList = []

    for item in ProponenteController.SelecionarTodos():
        costumerList.append([item.nome, item.idade, item.cpf, item.orgao, item.valor_contrato])

    df = pd.DataFrame(
    costumerList,
    columns=['Nome', 'Idade', 'CPF', 'Órgão Público', 'Valor do Contrato']
    )

    st.table(df)

if Page_Proponente == 'Incluir':
    st.title('Incluir Proponente')
    # Formulário do Streamlit
    with st.form(key="include_proponente"):
        input_nome = st.text_input(label="Insira o nome do proponente")
        input_idade = st.number_input(label="Insira a idade do proponente", format="%d", step=1)
        input_cpf = st.text_input(label="Insira o CPF do proponente")  # Usando text_input para CPF
        input_orgao = st.selectbox("Selecione o órgão público que o proponente faz parte", options=["PMERJ", "Marinha do Brasil", "Aeronáutica", "UERJ", "Ministério Público"])
        input_valor_contrato = st.number_input(label="Insira o valor do contrato", format="%.2f")  # Campo para valor do contrato
        input_button_submit = st.form_submit_button("Enviar")

    # Após o botão ser pressionado, crie uma instância de Proponente
    if input_button_submit:
        # Criando uma instância de Proponente com os valores fornecidos no formulário
        novo_proponente = Proponente(0, nome=input_nome, idade=input_idade, cpf=input_cpf, orgao=input_orgao, valor_contrato=input_valor_contrato)
    
        # Passando a instância para o método Incluir do ProponenteController
        ProponenteController.Incluir(novo_proponente)
    
        st.success("Proponente incluído com sucesso!")


