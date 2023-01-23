
def Payback_contable():
    n_periodos=int(input("Ingrese el numero de periodos: "))
    Beneficios=[]
    for i in range(n_periodos):
        Beneficios.append(float(input("Ingrese el flujo de caja "+str(i+1)+": ")))

    Inversion_inicial=float(input("Ingrese la inversion inicial: "))
    Payback = 0
    for i in range(len(Beneficios)):
        Payback += Beneficios[i]
        if Payback >= Inversion_inicial:
            break
    print("El Payback Contable es: ",i+1)

def Payback_descontado():
    n_periodos=int(input("Ingrese el numero de periodos: "))
    Beneficios=[]
    for i in range(n_periodos):
        Beneficios.append(float(input("Ingrese el flujo de caja "+str(i+1)+": ")))
    Inversion_inicial=float(input("Ingrese la inversion inicial: "))
    Interes=float(input("Ingrese el interes: "))
    Payback = 0
    for i in range(len(Beneficios)):
        Payback += Beneficios[i]/(1+Interes)**i
        if Payback >= Inversion_inicial:
            break
    print("El Payback Descontado es: ",i+1)
    return i+1
    

def Menu_payback():
    while True:
        print("\n1. Calcular Payback Contable")
        print("2. Calcular Payback Descontado")
        print("3. Regresar al menu principal\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            Payback_contable()
        elif opcion == 2:
            Payback_descontado()
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")
  
if __name__ == "__main__":
    Menu_payback()
