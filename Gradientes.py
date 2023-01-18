
def gradiente_aritmetico():
    def valor_presente():
        A = float(input("Ingrese el valor de la anualidad: "))
        i = float(input("Ingrese el valor de la tasa de interes: "))
        n = float(input("Ingrese el numero de periodos: "))
        G = float(input("Ingrese el valor del gradiente: "))
        sub_i = (i/100)
        #vp = A*(((1+i)**(n))/())+(G/sub_i)*((()/())-(()/()))
        vp=A*((((1+sub_i)**n)-1)/(sub_i*(1+sub_i)**n))+(G/sub_i)*(((((1+sub_i)**n)-1)/(sub_i*((1+sub_i)**n)))-(n/(1+sub_i)**n))
        resultado = round(vp, 2)
        print("\n\033[1;31m El valor presente es: ", resultado, "\033[0m")
        valor_presente()
    def valor_futuro():
        A = float(input("Ingrese el valor de la anualidad: "))
        i = float(input("Ingrese el valor de la tasa de interes: "))
        n = float(input("Ingrese el numero de periodos: "))
        G = float(input("Ingrese el valor del gradiente: "))
        sub_i = (i/100)/12
        vf=A*((((1+sub_i)*n)-1)/(sub_i(1+sub_i)*n))+G/sub_i(((((1+sub_i)*n)-1)/(sub_i(1+sub_i)**n))-(n/(1+sub_i)**n))
        resultado = round(vf, 2)
        print("\n\033[1;31m El valor futuro es: ", resultado, "\033[0m")
        valor_futuro()
    while True:
        print("\n--- Gradiente aritmetico ---")
        print("1. Hallar el valor valor presente teniendo la anualidad")
        print("2. Hallar la anualidad teniendo el valor presente")
        print("3. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            valor_presente()
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")
def gradiente_geometrico():
    def valor_presente():
        A = float(input("Ingrese el valor de la anualidad: "))
        i = float(input("Ingrese el valor de la tasa de interes: "))
        n = float(input("Ingrese el numero de periodos: "))
        G = float(input("Ingrese el valor del gradiente: "))
        sub_i = (i/100)/12
        vp=A*((((1+sub_i)*n)-1)/(sub_i(1+sub_i)*n))+G/sub_i(((((1+sub_i)*n)-1)/(sub_i(1+sub_i)**n))-(n/(1+sub_i)**n))
        resultado = round(vp, 2)
        print("\n\033[1;31m El valor presente es: ", resultado, "\033[0m")
        valor_presente()
    def valor_futuro():
        A = float(input("Ingrese el valor de la anualidad: "))
        i = float(input("Ingrese el valor de la tasa de interes: "))
        n = float(input("Ingrese el numero de periodos: "))
        G = float(input("Ingrese el valor del gradiente: "))
        sub_i = (i/100)/12
        vf=A*((((1+sub_i)*n)-1)/(sub_i(1+sub_i)*n))+G/sub_i(((((1+sub_i)*n)-1)/(sub_i(1+sub_i)**n))-(n/(1+sub_i)**n))
        resultado = round(vf, 2)
        print("\n\033[1;31m El valor futuro es: ", resultado, "\033[0m")
        valor_futuro()
    while True:
        print("\n--- Gradiente geometrico ---")
        print("1. Hallar el valor valor presente teniendo la anualidad")
        print("2. Hallar la anualidad teniendo el valor presente")
        print("3. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            valor_presente()
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            print("Regresando al menu anterior")
            break
        else:
            print("Opcion no valida")
def Menu_gradientes():
    print("")
    print("Programa en construccion xd")
    print("Regresando al menu anterior")
    print("")
    while True:
        print("\n--- Gradientes ---")
        print("1. Gradiente aritmetico")
        print("2. Gradiente geometrico")
        print("3. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            gradiente_aritmetico()
        elif opcion == 2:
            gradiente_geometrico()
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Menu_gradientes()
