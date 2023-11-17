def asignaturas(asignatura):
    for asignatur in asignatura:
        nota=int(input(f"Dime tu nota en {asignatur} : "))
        print (f"En la asignatura {asignatur} has sacado un {nota}")

def main():
    asignatura = (['Mates'] , ['Lengua'] , ['Física'] , ['Química'] , ['Filosofía'])
    asignaturas(asignatura)

if __name__ == "__main__":
    main()