def ingresar_nota(asignaturas):
    notas = []
    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas.append((asignatura, nota))
    return notas

def asignaturas_suspendida(notas):
    reprobadas = [asignatura for asignatura, nota in notas if nota < 5.0]
    return reprobadas

def main():
    asignaturas = ["Mates", "Lengua" , "Física", "Química", "Filosofía"]
    notas = ingresar_nota(asignaturas)
    asignaturas_aprobadas = asignaturas_suspendida(notas)
    
    if not asignaturas_aprobadas:
        print("Has aprobado todas las asignaturas.")
    else:
        print("Debes repetir las siguientes asignaturas:")
        for asignatura in asignaturas_aprobadas:
            print(asignatura)

if __name__ == "__main__":
    main()
