def polindro(palabra):
    palabra_alreves = palabra.copy()
    palabra_alreves.reverse()
    if palabra == palabra_alreves :
        print("Es un palíndromo")
    else:
        print("no es un palíndromo")

def main():
    palabra = list(input("Dame palabra : "))
    polindro(palabra)

if __name__ == "__main__":
    main()