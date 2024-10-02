import sqlite3
import os

# Obtenha o caminho absoluto para o banco de dados
caminho_db = os.path.join(os.path.dirname(__file__), 'crud_python.db')

# Função para conectar ao banco de dados
def conectar():
    con = sqlite3.connect(caminho_db, check_same_thread=False)
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Proponente
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proNome TEXT NOT NULL,
            proIdade INTEGER NOT NULL,
            proCPF TEXT NOT NULL,
            proOrgao TEXT,
            proValorContrato REAL
        )
        """
    )
    return con, cursor


# Chama a função de conectar diretamente quando rodar o arquivo
if __name__ == "__main__":
    con, cursor = conectar()
    print("Banco de dados e tabela criados com sucesso!")
    con.close()
