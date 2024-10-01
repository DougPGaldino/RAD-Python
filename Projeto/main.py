import streamlit as st
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente

image_path = "C:/Users/Douglas/Documents/RAD-Python/Projeto/imagens/assist.png"
st.image(image_path, width=200)

st.title("Prospecção")


# Formulário do Streamlit
with st.form(key="include_proponente"):
    input_nome = st.text_input(label="Insira o nome do proponente")
    input_idade = st.number_input(label="Insira a idade do proponente", format="%d", step=1)
    input_orgao = st.selectbox("Selecione o órgão em que o proponente faz parte", options=["PMERJ", "Marinha do Brasil", "Aeronáutica", "UERJ", "Ministério Público"])
    input_button_submit = st.form_submit_button("Enviar")

# Após o botão ser pressionado, crie uma instância de Proponente
if input_button_submit:
    # Criando uma instância de Proponente com os valores fornecidos no formulário
    novo_proponente = Proponente(nome=input_nome, idade=input_idade, orgao=input_orgao)
    
    # Passando a instância para o método Incluir do ProponenteController
    ProponenteController.Incluir(novo_proponente)
    
    st.success("Proponente incluido com sucesso!")
