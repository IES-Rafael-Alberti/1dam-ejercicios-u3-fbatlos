def domicilios_clientes(lista_compras):
    domicilio = set()
    for compra in lista_compras:
        domicilio.add(compra[3])
    return domicilio




def main():
    lista_compras = [()]
    dimicilios = domicilios_clientes(lista_compras)
    
    
if __name__ == "__main__":
    main()