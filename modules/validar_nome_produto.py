def validar_nome_produto(nome):
    try: 
        if len(nome)< 3:
            print("Nome invalido.")
        else:
            return nome
    except:
        print("Erro: digite um nome válido.")
        return None