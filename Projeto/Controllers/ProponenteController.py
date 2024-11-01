# ProponenteController.py
from services.database import db  # Importa a instância de db diretamente
import streamlit as st
from models.proponente import Proponente

def Incluir(proponente):
    try:
        cursor = db.conectar()  # Obtém o cursor da conexão ativa
        query = """
            INSERT INTO Proponente (proNome, proIdade, proCPF, proOrgao, proValorContrato)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (proponente.nome, proponente.idade, proponente.cpf, proponente.orgao, proponente.valor_contrato))
        db.con.commit()  # Confirma a transação
        print("Proponente inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir proponente: {e}")
    finally:
        db.close()

def SelecionarTodos():
    try:
        cursor = db.conectar()
        
        cursor.execute("SELECT * FROM Proponente")
        costumerList = [Proponente(*row) for row in cursor.fetchall()]
        
        return costumerList
    
    except Exception as e:
        st.error(f"Erro ao selecionar proponentes: {e}")
        return []
    
    finally:
        db.close()

def Deletar(id_proponente):
    try:
        db.conectar()  # Conecta ao banco de dados
        query = "DELETE FROM Proponente WHERE id = %s"
        db.cursor.execute(query, (id_proponente,))
        db.con.commit()  # Salva as alterações
        print("Proponente excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir proponente: {e}")
    finally:
        db.close()

def Editar(proponente):
    try:
        db.conectar()
        query = """
            UPDATE Proponente
            SET proNome = %s, proIdade = %s, proCPF = %s, proOrgao = %s, proValorContrato = %s
            WHERE id = %s
        """
        db.cursor.execute(query, (proponente.nome, proponente.idade, proponente.cpf, proponente.orgao, proponente.valor_contrato, proponente.id))
        db.con.commit()
        print("Proponente atualizado com sucesso!")
        return True  # Indica sucesso
    except Exception as e:
        print(f"Erro ao atualizar proponente: {e}")
        return False  # Indica falha
    finally:
        db.close()
