import streamlit as st
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente

def formatar_cpf(cpf: str) -> str:
    """Formata o CPF para o padrão XXX.XXX.XXX-XX."""
    # Remove todos os caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Aplica a formatação se o CPF tiver 11 dígitos
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


def EditarProponentePage():
    st.title('Editar Proponente')

    
    # Obtendo a lista de proponentes
    proponentes = ProponenteController.SelecionarTodos()
    
    # Se não houver proponentes, exibe uma mensagem
    if not proponentes:
        st.warning("Nenhum proponente encontrado.")
        return
    
    # Seleção do proponente a ser editado
    opcoes_proponentes = [f"{p.nome} (ID: {p.id})" for p in proponentes]
    proponente_selecionado = st.selectbox("Selecione um proponente para editar", options=opcoes_proponentes)
    
    # Obtendo o ID do proponente selecionado
    id_proponente = int(proponente_selecionado.split(" (ID: ")[-1][:-1])
    
    # Carregando os dados do proponente selecionado
    proponente = next((p for p in proponentes if p.id == id_proponente), None)
    
    if proponente:
        # Formulário de edição
        with st.form(key="edit_proponente"):
            input_nome = st.text_input(label="Nome", value=proponente.nome)
            input_idade = st.number_input(label="Idade", value=proponente.idade, format="%d", step=1)
            input_cpf = st.text_input(label="CPF", value=proponente.cpf)
            input_orgao = st.selectbox("Órgão Público", 
                                        options=["PMERJ", "Marinha do Brasil", "Aeronáutica", "UERJ", "Ministério Público"],
                                        index=["PMERJ", "Marinha do Brasil", "Aeronáutica", "UERJ", "Ministério Público"].index(proponente.orgao))
            
            # Verifica se valor_contrato é numérico e não é None, caso contrário define 0.0
            valor_contrato = proponente.valor_contrato if isinstance(proponente.valor_contrato, (int, float)) else 0.0
            input_valor_contrato = st.number_input(label="Valor do Contrato", value=valor_contrato, format="%.2f")
            
            input_button_submit = st.form_submit_button("Salvar Alterações")  # Botão de envio
            
        # Ao pressionar o botão, verifica as validações
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
                
                # Atualiza a instância do proponente
                proponente.nome = input_nome
                proponente.idade = input_idade
                proponente.cpf = cpf_formatado
                proponente.orgao = input_orgao
                proponente.valor_contrato = input_valor_contrato
                
                # Passando a instância atualizada para o método Editar do ProponenteController
                ProponenteController.Editar(proponente)
                
                st.success("Proponente editado com sucesso!")
    else:
        st.error("Proponente não encontrado.")
