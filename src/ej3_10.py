def ordenar(numeros : list):
    numeros.sort()
    print (f"El mayor es {numeros[-1]} y el menor es {numeros[0]}")

def main():
    numeros = list([50, 75, 46, 22, 80, 65, 8])
    ordenar(numeros)

if __name__ == "__main__":
    main()