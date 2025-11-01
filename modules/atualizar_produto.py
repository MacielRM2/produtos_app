from modules.conectar_bd import conectar_bd

def atualizar_produto(id_produto, nome, preco, estoque):
    conexao, cursor = conectar_bd()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")

    else:
        cursor.execute("""
    UPDATE produtos
    SET nome = ?, preco = ?, estoque = ?
    WHERE id = ?
""", (nome, preco, estoque, id_produto,))

        conexao.commit()
        print("Produto atualizado com sucesso!")

    conexao.close()