def buscarpares(numeros) -> set :
    cont=set()
    for num in (numeros):
        if num%2 == 0:
            cont.add(num)
    return cont

def buscarmultiplos(numeros):
    cont=set()
    for num in (numeros):
        if num%3 == 0:
            cont.add(num)
    return cont
    
    

def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = buscarpares(numeros)
    multiplosde3 = buscarmultiplos(numeros)
    pares_y_multiplos_de_tres = pares & multiplosde3
    print(f"Los numeros pares son : {pares}.\nThe multipls of three are : {multiplosde3}\nThe intersection is : {pares_y_multiplos_de_tres}")
    
    
         
if __name__ == "__main__":
    main()