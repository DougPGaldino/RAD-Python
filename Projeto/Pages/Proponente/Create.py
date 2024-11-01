import streamlit as st
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente
import pandas as pd

def formatar_cpf(cpf: str) -> str:
    """Formata o CPF para o padrão XXX.XXX.XXX-XX."""
    # Remove todos os caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Aplica a formatação se o CPF tiver 11 dígitos
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf

def IncluirProponentePage():
    st.title('Incluir Proponente')
    
    # Formulário do Streamlit
    with st.form(key="include_proponente"):
        input_nome = st.text_input(label="Insira o nome do proponente")
        input_idade = st.number_input(label="Insira a idade do proponente", format="%d", step=1)
        input_cpf = st.text_input(label="Insira o CPF do proponente") 
        input_orgao = st.selectbox("Selecione o órgão público que o proponente faz parte", options=["PMERJ", "Marinha do Brasil", "Aeronáutica", "UERJ", "Ministério Público"])
        input_valor_contrato = st.number_input(label="Insira o valor do contrato", format="%.2f")
        input_button_submit = st.form_submit_button("Enviar")

    # Após o botão ser pressionado, verifique as validações
    if input_button_submit:
        # Remove caracteres não numéricos do CPF
        cpf_sem_formatacao = ''.join(filter(str.isdigit, input_cpf))
        
        # Verificações de validação
        if not input_nome or not input_idade or not input_cpf or not input_orgao or input_valor_contrato <= 0:
            st.error("Todos os campos devem ser preenchidos e o valor do contrato deve ser maior que zero.")
        elif len(cpf_sem_formatacao) != 11:
            st.error("O CPF deve conter exatamente 11 dígitos e não pode estar vazio.")
        else:
            # Formata o CPF
            cpf_formatado = formatar_cpf(input_cpf)
            
            # Criando uma instância de Proponente com os valores fornecidos no formulário
            novo_proponente = Proponente(0, nome=input_nome, idade=input_idade, cpf=cpf_formatado, orgao=input_orgao, valor_contrato=input_valor_contrato)
        
            # Passando a instância para o método Incluir do ProponenteController
            ProponenteController.Incluir(novo_proponente)
        
            st.success("Proponente incluído com sucesso!")
