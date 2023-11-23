def pedirNIF():
    NIF = input("Dame tu NIF : ")
    return NIF

def pedirDatos():
    conjunto = {}
    conjunto ["nombre"] = pedirNombre()
    conjunto ["email"] = pedirEmail()
    conjunto["teléfono"] = pedirTelefono()
    conjunto["correo"] = pedirCorreo()
    conjunto["preferente"] = pedirPreferencia()
    return conjunto
    
    
def pedirNombre():
    nombre = input("Dime tú nombre : ")
    return nombre

def pedirEmail():
    email = input("Dime tú email : ")
    return email

def pedirTelefono():
    telefono = int(input("Dime tú teléfono : "))
    return telefono
    
def pedirCorreo():
    correo = input("Dime tu correo")
    return correo

def pedirPreferencia():
    preferencia = input("Eres preferente ? s/n : ")
    preferencia.lower()
    if preferencia == "s" :
        preferencia = True
    preferencia = False    
    

def main():
    NIF = pedirNIF()
    Datos = {}
    Datos [NIF] = pedirDatos()
    print (Datos)
if __name__ == "__main__":
    main()