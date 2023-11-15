def pedir_palabra() -> tuple:
    palabra = tuple(input("Dame una palabra : ").lower())
    palabra = palabra.replace()
    return palabra

def contador_vocales(palabra : tuple ) -> tuple :
    vocales = (["a",0] , ["e",0] , ["i",0] , ["o",0] , ["u",0])
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales
#hace lo mismo que lo de arriba solo que optimizado , cuenta las vocales de la palabra
#el for es para ir cambiando y comprobando cada vocal en cada palabra y la guarda en una tupla.
#return tuple ((vocal , palabra.count(vocal)) for vocal in ('a' , 'e' , 'i' , 'o' , 'u'))

def mostrar(vocales):
    print("Números de vocales : ")
    for vocal in vocales :
        print(f"{vocal[0]} = {vocal[1]}")
        

def main():
    palabra = pedir_palabra() 
    vocales = contador_vocales(palabra)
    mostrar(vocales)


if __name__ == "__main__":
    main()



