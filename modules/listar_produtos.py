from modules.conectar_bd import conectar_bd

def listar_produtos():
    conexao, cursor = conectar_bd()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for p in produtos:
            print(f"ID {p[0]} | Nome: {p[1]} | Preço: {p[2]} | Estoque: {p[3]} ")

    conexao.close()