


def pedir_fecha(meses):
    fecha = (input("Dame tu fecha dd/mm/aaaa "))
    fecha = fecha.split("/")
    print(f"{fecha[0]} de {meses[fecha[1]]} {fecha[2]}")



def main():
    meses = {"1" :"Enero" , "2" :"Febrero", "3" :"Marzo"}
    pedir_fecha (meses)
    
    
if __name__ == "__main__":
    main()