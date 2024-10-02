import services.database as db
import streamlit as st  # Adicionando import do Streamlit para exibir erros
from models.proponente import Proponente

def Incluir(proponente):
    try:
        # Obtém a conexão e o cursor
        con, cursor = db.conectar()
        
        # Insere o novo proponente no banco de dados
        cursor.execute("""
            INSERT INTO Proponente(proNome, proIdade, proCPF, proOrgao, proValorContrato) 
            VALUES (?, ?, ?, ?, ?)""", (proponente.nome, proponente.idade, proponente.cpf, proponente.orgao, proponente.valor_contrato))
        
        # Confirma a transação
        con.commit()
        
    except Exception as e:
        st.error(f"Erro ao inserir proponente: {e}")  # Exibe o erro no Streamlit
        
    finally:
        # Fecha a conexão após inserir os dados
        con.close()

def SelecionarTodos():
    try:
        # Obtém a conexão e o cursor
        con, cursor = db.conectar()
        
        # Executa o comando SELECT
        cursor.execute("SELECT * FROM Proponente")
        costumerList = []
        
        # Itera sobre as linhas do banco de dados e cria as instâncias de Proponente
        for row in cursor.fetchall():
            costumerList.append(Proponente(row[0], row[1], row[2], row[3], row[4], row[5]))  # Proponente instanciado corretamente
        
        return costumerList
    
    except Exception as e:
        st.error(f"Erro ao selecionar proponentes: {e}")
        return []
    
    finally:
        # Fecha a conexão após a consulta
        con.close()