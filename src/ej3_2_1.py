def pedirdivisa(divisa):
    dentro = input("Dime tu divisa entre : Euro , Dollar y Yen : ")
    while dentro not in divisa : 
        print("**ERROR** Divisa no encontrada , prueba otra vez ")
        dentro = input("=> ")
    print("Su divisa es :",divisa[dentro]) 
    
def main():
    divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    pedirdivisa(divisa)
if __name__ == "__main__":
    main()