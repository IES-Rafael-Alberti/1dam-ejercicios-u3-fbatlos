def pedirnum(numeros: list):
    cont = 1
    while cont <= 6:
        num=input(f"{cont} =>")
        if num <= 0 or num  >= 50 : 
            print("Valor Invalido")
    



def orden(numeros : list):
    numeros = numeros.sort()
    numeros = numeros.reverse()
    return numeros

def main():
    print("Ingrese los numeros : ")
    numeros = list()
    pedirnum(numeros)
    print(orden(numeros))

if __name__ == "__main__":
    main()