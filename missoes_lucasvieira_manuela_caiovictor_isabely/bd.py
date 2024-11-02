from tkinter import *
from tkinter import ttk
import sqlite3

class Database:
    def __init__(self, db_name="missao.db"):
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS missao (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data_lancamento TEXT NOT NULL,
                    destino TEXT NOT NULL,
                    tripulacao TEXT NOT NULL,
                    carga_util TEXT NOT NULL,
                    duracao TEXT NOT NULL,
                    custo REAL NOT NULL,
                    descricao TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as error:
            print("Erro ao conectar ao banco:", error)

    def insert_missao(self, nome, data_lancamento, destino, tripulacao, carga_util, duracao, custo, descricao, status):
        query = '''INSERT INTO missao (nome, data_lancamento, destino, tripulacao, carga_util, duracao, custo, descricao, status)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        self.cursor.execute(query, (nome, data_lancamento, destino, tripulacao, carga_util, duracao,  custo, descricao, status))
        self.connection.commit()

    def fetch_missoes(self):
        self.cursor.execute("SELECT * FROM missao")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
