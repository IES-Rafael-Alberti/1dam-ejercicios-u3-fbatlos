def asignaturas(asignatura ):
    for asignatur in asignatura:
        print (f"Yo estudio : {asignatur}")

def main():
    asignatura = (['Mates'] , ['Lengua'] , ['Física'] , ['Química'] , ['Filosofía'])
    asignaturas(asignatura)

if __name__ == "__main__":
    main()