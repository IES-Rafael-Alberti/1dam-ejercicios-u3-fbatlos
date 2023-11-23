def pedirnombres():
    alumnos = set()
    cont = str()
    while cont != "x" :
        cont = input("=> ")
        if cont == "x":
            return alumnos
        alumnos.add(cont)
    return alumnos

def repetir(primaria , segundaria):
    return (primaria & segundaria)

def comparativa(primaria , segundaria):
    return (primaria - segundaria , segundaria - primaria)

def compararTodo(primaria , segundaria):
    if primaria == segundaria :
        return "Todos los nombres se repiten !!"
    return "No todos los nombres se repiten "

def main():
    print("Te voy a pedir los nombres de los alumnos de primaria")
    primaria = pedirnombres()
    print("Te voy a pedir los nombres de los alumnos de segundaria")
    segundaria = pedirnombres()
    repeticion = repetir(primaria , segundaria)
    comparacion1 , comparacion2 =comparativa(primaria , segundaria)
    comparacion = comparacion1|comparacion2
    comparartodo = compararTodo(primaria , segundaria)
    print("Los alumnos de primaria son:",primaria)
    print("Los alumnos de segundaria son:",segundaria)
    print("Los nombres repetidos son:",repeticion)
    print("Los nombres no repetidos son:",comparacion)
    print(comparartodo)
        
    
    
    
if __name__ == "__main__":
    main()