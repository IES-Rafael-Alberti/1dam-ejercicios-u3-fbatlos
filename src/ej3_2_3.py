def pedir_fruta(frutas):
    fruta = input("Dime una de nuestras frutas : ")
    fruta = fruta.lower()
    while fruta not in frutas:
        print("No tenemos esa fruta , intentalo otra vez")
        fruta = input("=> ")
    fruta = fruta.lower()
    return (pedir_kilos(frutas , fruta))
    
def pedir_kilos(frutas , fruta):
    kilos = float(input("Dime los kilos de fruta :"))
    while kilos < 0 :
        print("Kilos no permitidos , pon uno válido")
        kilos = float(input("=> "))
    return (calculo(kilos , fruta , frutas))

def calculo(kilos , fruta , frutas):
    resultado = frutas[fruta]*kilos
    return(f"El coste de {fruta} con {kilos} es de {resultado}€")


def main():
    try:
        frutas = {"platano" : 1.35 , "manzana" : 0.80 , "pera" : 0.85 , "naranja" : 0.70}
        print(pedir_fruta(frutas))
    except ValueError as e :
        print(e,"Algo a salido mal ")
    
if __name__ == "__main__":
    main()