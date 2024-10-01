import services.database as db

def Incluir(proponente):
    try:
        # Obtém a conexão e o cursor
        con, cursor = db.conectar()
        
        # Insere o novo proponente no banco de dados
        cursor.execute("""
            INSERT INTO Proponente(proNome, proIdade, proOrgao) 
            VALUES (?, ?, ?)""", (proponente.nome, proponente.idade, proponente.orgao))
        
        # Confirma a transação
        con.commit()
        
    except Exception as e:
        print(f"Erro ao inserir proponente: {e}")
        
    finally:
        # Fecha a conexão após inserir os dados
        con.close()
