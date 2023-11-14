

def polindro(palabra):
    palabra_alreves = palabra.copy()
    palabra_alreves.reverse()
    if palabra == palabra_alreves :
        print("Es un palinddromo")
    else:
        print("no es un palindromo")

def main():
    palabra = list(input("Dame palabbra : "))
    polindro(palabra)

if __name__ == "__main__":
    main()