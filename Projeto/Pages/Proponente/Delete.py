import streamlit as st
import pandas as pd
import Controllers.ProponenteController as ProponenteController
from models.proponente import Proponente  # Importando a classe Proponente corretamente

def DeletarProponentePage():
    st.title('Deletar Proponente')
    
    # Selecionar todos os proponentes existentes
    proponentes = ProponenteController.SelecionarTodos()  # Obtém todos os proponentes
    
    if proponentes:  # Verifica se há proponentes cadastrados
        # Cria uma lista de nomes para o seletor
        nomes_proponentes = [f"{p.nome} (ID: {p.id})" for p in proponentes]
        proponente_selecionado = st.selectbox("Selecione o proponente para excluir", nomes_proponentes)

        if st.button("Excluir Proponente"):
            # Extrai o ID do proponente selecionado
            id_selecionado = int(proponente_selecionado.split("(ID: ")[1][:-1])
            
            # Chama a função de exclusão
            ProponenteController.Deletar(id_selecionado)
            st.success(f"Proponente ID {id_selecionado} excluído com sucesso!")

            # Atualiza a lista de proponentes após a exclusão
            proponentes = ProponenteController.SelecionarTodos()  # Obtém a nova lista de proponentes

        # Cria uma lista de dicionários para usar no DataFrame
        data = [{'ID': p.id, 'Nome': p.nome, 'Idade': p.idade, 'CPF': p.cpf, 'Órgão': p.orgao, 'Valor do Contrato': p.valor_contrato} for p in proponentes]
        
        # Cria um DataFrame a partir da lista de dicionários
        df_proponentes = pd.DataFrame(data)
        
        # Exibe a tabela com os proponentes
        st.subheader("Lista de Proponentes")
        st.dataframe(df_proponentes)
        
    else:
        st.warning("Não há proponentes cadastrados para excluir.")
