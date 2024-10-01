import sqlite3

# Função para conectar ao banco de dados
def conectar():
    con = sqlite3.connect('crud_python.db', check_same_thread=False)
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Proponente
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proNome TEXT NOT NULL,
            proIdade INTEGER NOT NULL,
            proOrgao TEXT
        )
        """
    )
    return con, cursor
