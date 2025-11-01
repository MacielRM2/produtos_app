

def validar_preco(preco):
    try:
        preco = float(preco)
        if preco <0:
            print("Preço invalido, Não pode ser negativo.")
            return None
        else:
            return preco
        
    except:
        print("Preço invalido, digite apenas numeros.")
        return None