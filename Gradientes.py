def gradiente_aritmetico():
    def valor_presente():
        while True:
            print('\n--- Gradiente aritmetico - Valor presente ---')
            print('1. Creciente (Si la gradiente aumenta)')
            print('2. Decreciente (Si la gradiente disminuye)')
            print('3. Regresar al menu anterior\n')
            opcion = int(input('Ingrese opcion: '))
            if opcion == 1:
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                vp=A*((((1+sub_i)**n)-1)/(sub_i*(1+sub_i)**n))+(G/sub_i)*(((((1+sub_i)**n)-1)/(sub_i*((1+sub_i)**n)))-(n/(1+sub_i)**n))
                resultado = round(vp, 2)
                print("\n\033[1;32m El valor presente creciente es: ", resultado, "\033[0m")
                gradiente_aritmetico()
            elif opcion == 2:
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                vp=A*((((1+sub_i)**n)-1)/(sub_i*(1+sub_i)**n))-(G/sub_i)*(((((1+sub_i)**n)-1)/(sub_i*((1+sub_i)**n)))-(n/(1+sub_i)**n))
                resultado = round(vp, 2)
                print("\n\033[1;32m El valor presente decreciente es: ", resultado, "\033[0m")
                gradiente_aritmetico()
            elif opcion == 3:
                break
            else:
                print('Opcion invalida')
    def valor_futuro():
        while True:
            print('\n--- Gradiente aricmetico - valor futuro ---')
            print('1. Creciente (Si la gradiente aumenta)')
            print('2. Decreciente (Si la gradiente disminuye)')
            print('3. Regresar al menu anterior\n')
            opcion = int(input('Ingrese opcion: '))
            if opcion == 1:
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                vf=A*((((1+sub_i)*n)-1)/(sub_i(1+sub_i)*n))+G/sub_i(((((1+sub_i)*n)-1)/(sub_i(1+sub_i)**n))-(n/(1+sub_i)**n))
                resultado = round(vf, 2)
                print("\n\033[1;32m El valor futuro creciente es: ", resultado, "\033[0m")
                gradiente_aritmetico()
            elif opcion == 2:
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                vf=A*((((1+sub_i)*n)-1)/(sub_i(1+sub_i)*n))-G/sub_i(((((1+sub_i)*n)-1)/(sub_i(1+sub_i)**n))-(n/(1+sub_i)**n))
                resultado = round(vf, 2)
                print("\n\033[1;32m El valor futuro decreciente es: ", resultado, "\033[0m")
                gradiente_aritmetico()
            elif opcion == 3:
                break
            else:
                print('Opcion incorrecta')
    
    def cuota_n():
        def creciente():
            print("\n--- Gradiente aritmetico - cuota n creciente ---")
            A = float(input("Ingrese el valor de la anualidad: "))
            n = float(input("Ingrese el numero de periodos: "))
            G = float(input("Ingrese el valor del gradiente: "))
            c_n = A + (n - 1) * G # cuota n
            print('\n\033[1;32m Cuota n creciente es: ', c_n, '\033[0m')
        def decreciente():
            print("\n--- Gradiente aritmetico - cuota n decreciente ---")
            A = float(input("Ingrese el valor de la anualidad: "))
            n = float(input("Ingrese el numero de periodos: "))
            G = float(input("Ingrese el valor del gradiente: "))
            c_n = A - (n - 1) * G # cuota n
            print('\n\033[1;32m Cuota n decreciente es: ', c_n, '\033[0m')
        while True:
            print('\n--- Gradiente aritmetico - cuota n ---')
            print('1. Creciente (Si la gradiente aumenta)')
            print('2. Decreciente (Si la gradiente disminuye)')
            print('3. Regresar al menu anterior\n')
            opcion = int(input('Ingrese una opcion: '))
            if opcion == 1:
                creciente()
            elif opcion == 2:
                decreciente()
            elif opcion == 3:
                break
            else:
                print('Opcion no valida')
    while True:
        print("\n--- Gradiente aritmetico ---")
        print('1. Valor presente')
        print('2. Valor futuro')
        print('3. Cuota n')
        print("4. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            valor_presente()
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            cuota_n()
        elif opcion == 4:
            break
        else:
            print("Opcion no valida")
def gradiente_geometrico():
    def valor_presente():
        while True:
            print('\n--- Gradiente geometrico - Valor presente ---')
            print('1. Creciente (Si la gradiente aumenta)')
            print('2. Decreciente (Si la gradiente disminuye)')
            print('3. Regresar al menu anterior\n')
            opcion = int(input('Ingrese opcion: '))
            if opcion == 1:
                print('\n--- Gradiente geometrico - Valor presente creciente---')
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                sub_G = G/100
                vp=(A*(((1+sub_G)**n)*((1+sub_i)**(-n))-1))/(sub_G-sub_i)
                resultado = round(vp, 2)
                print("\n\033[1;32m El valor presente creciente es: ", resultado, "\033[0m")
                gradiente_geometrico()
            elif opcion == 2:
                print('\n--- Gradiente geometrico - Valor presente decreciente---')
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                sub_G = G/100
                vp=vp=(A*(1-((1-sub_G)**n)*((1+sub_i)**(-n))))/(sub_G+sub_i)
                resultado = round(vp, 2)
                print("\n\033[1;32m El valor presente decreciente es: ", resultado, "\033[0m")
                gradiente_geometrico()
            elif opcion == 3:
                break
            else:
                print('Opcion invalida')
    def valor_futuro():
        while True:
            print('\n--- Gradiente geometrica - valor futuro ---')
            print('1. Creciente (Si la gradiente aumenta)')
            print('2. Decreciente (Si la gradiente disminuye)')
            print('3. Regresar al menu anterior\n')
            opcion = int(input('Ingrese opcion: '))
            if opcion == 1:
                print('\n--- Gradiente geometrica - valor futuro creciente ---')
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                vf=A*((((1+G)**n)-((1+sub_i)**n))/(G-sub_i))
                resultado = round(vf, 2)
                print("\n\033[1;32m El valor futuro creciente es: ", resultado, "\033[0m")
                gradiente_geometrico()
            elif opcion == 2:
                print('\n--- Gradiente geometrica - valor futuro decreciente ---')
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                G = float(input("Ingrese el valor del gradiente: "))
                sub_i = (i/100)
                vf=A*((((1+sub_i)**n)-((1-G)**n))/(G+sub_i))
                resultado = round(vf, 2)
                print("\n\033[1;32m El valor futuro decreciente es: ", resultado, "\033[0m")
                gradiente_geometrico()
            elif opcion == 3:
                break
            else:
                print('Opcion incorrecta')
    def cuota_n():
        def creciente():
            print("\n--- Gradiente geometrico - cuota n creciente ---")
            A = float(input("Ingrese el valor de la anualidad: "))
            n = float(input("Ingrese el numero de periodos: "))
            G = float(input("Ingrese el valor del gradiente: "))
            c_n = A * ((1 + G)**(n-1)) # cuota n
            resultado = round(c_n, 2)
            print('\n\033[1;32m Cuota n creciente es: ', resultado, '\033[0m')
        def decreciente():
            print("\n--- Gradiente geometrico - cuota n decreciente ---")
            A = float(input("Ingrese el valor de la anualidad: "))
            n = float(input("Ingrese el numero de periodos: "))
            G = float(input("Ingrese el valor del gradiente: "))
            c_n = A * ((1 - G)**(n-1)) # cuota n
            print('\n\033[1;32m Cuota n decreciente es: ', c_n, '\033[0m')
        
        while True:
            print('\n--- Gradiente aritmetico - cuota n ---')
            print('1. Creciente (Si la gradiente aumenta)')
            print('2. Decreciente (Si la gradiente disminuye)')
            print('3. Regresar al menu anterior\n')
            opcion = int(input('Ingrese una opcion: '))
            if opcion == 1:
                creciente()
            elif opcion == 2:
                decreciente()
            elif opcion == 3:
                break
            else:
                print('Opcion no valida')

    while True:
        print("\n--- Gradiente geometrico ---")
        print('1. Valor presente')
        print('2. Valor futuro')
        print('3. Cuota n')
        print("4. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            valor_presente()
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            cuota_n()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")
def Menu_gradientes():
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