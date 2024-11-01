# services/database.py
import psycopg2

class Database:
    def __init__(self):
        self.con = None
        self.cursor = None

    def conectar(self):
        if not self.con:  # Conecta apenas se não houver conexão ativa
            try:
                self.con = psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="postgres",
                    host="localhost",
                    port="5432"
                )
                self.cursor = self.con.cursor()
                self.criar_tabela()
            except Exception as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                raise
        return self.cursor

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Proponente (
                id SERIAL PRIMARY KEY,
                proNome VARCHAR(100) NOT NULL,
                proIdade INTEGER NOT NULL,
                proCPF VARCHAR(14) NOT NULL,
                proOrgao VARCHAR(100),
                proValorContrato NUMERIC
            )
        """)
        self.con.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.con:
            self.con.close()
            self.con = None

# Instância global
db = Database()
