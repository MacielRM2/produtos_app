
def validar_estoque(estoque):
    try:
        estoque = int(estoque)
        if estoque <0:
            print("Estoque invalido")
            return None
        else:
            return estoque
        
    except:
        print("Estoque invalido, somente numeros inteiros")
        return None