
def crearDiccionario(palabra):
    diccionario = dict(par.split(":") for par in palabra.split(","))
    return diccionario

def  


def traducirfrase(frase:str , diccionario ):
    palabras = frase.split("")
    traduccion = []
    
    for palabra in palabras:
        traduccion.append(diccionario.get(palabra,palabra))
    frasefinal = " ".join(traduccion)
    return frasefinal

def main():
    palabra = input ("Dame una frase separada por la traducción con : y , ejm(niño:boy , mesa : table) : ")
    diccionario = crearDiccionario(palabra)
    print(traducirfrase(diccionario))
if __name__ == "__main__":
    main()