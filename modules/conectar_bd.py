# Nome: Rayssa Rebeca da Silva
import sqlite3
def conectar_bd():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    """)
    conexao.commit()

    print("Banco de dados conectado e a tabela verificada com sucesso!!")
    return conexao, cursor 