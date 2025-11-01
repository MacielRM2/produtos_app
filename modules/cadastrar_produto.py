from modules.conectar_bd import conectar_bd

def cadastrar_produto(nome, preco, estoque):
    conexao, cursor = conectar_bd()

    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", 
                   (nome, preco, estoque))

    conexao.commit()
    print("Produto cadastrado com sucesso!")
    conexao.close()

