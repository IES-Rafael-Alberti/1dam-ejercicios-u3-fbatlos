def multiplicador(lista1 , lista2):
    return tuple(lista1[i]*lista2[i] for i in range (len(lista1)))
        
def main():
    lista1 = [1,2,3]
    lista2 = [-1,0,2]
    print(multiplicador(lista1 , lista2))
if __name__ == "__main__":
    main()