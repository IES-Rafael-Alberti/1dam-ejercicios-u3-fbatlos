def mostrar(info):
    print(info["nombre"],"tiene",info["edad"],"años, vive en",info["dirección"],"y su número de teléfono es",info["telefono"],".")



def main():
    try:
        nombre = input("Nombre : ")
        edad = int(input("Edad :"))
        dirección = input("Dirección : ")
        telefono = int(input("Telefono :")) 
        info = {"nombre":nombre , "edad":edad , "dirección":dirección , "telefono":telefono}
        mostrar(info)
    except ValueError as e :
        print(e," Introduce un valor correcto.")
    
if __name__ == "__main__":
    main()