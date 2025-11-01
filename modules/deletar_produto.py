from modules.conectar_bd import conectar_bd

def deletar_produto(id_produto):
    conexao, cursor = conectar_bd()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")
    else:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conexao.commit()
        print("Produto deletado com sucesso!")

    conexao.close()