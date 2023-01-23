def VAN():
    n_periodos=int(input("Ingrese el numero de periodos: "))
    Beneficios=[]
    for i in range(n_periodos):
        Beneficios.append(float(input("Ingrese el beneficio del periodo "+str(i+1)+": ")))
    Interes=float(input("Ingrese el interes: "))
    VAN = 0
    for i in range(len(Beneficios)):
        VAN += Beneficios[i]/(1+Interes)**i
    
    a=print("El Valor Actual Neto es VAN: ",VAN)
    return a

def Menu_VAN():
    while True:
        print("\n1. Calcular VAN")
        print("2. Regresar al menu principal\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            VAN()
        elif opcion == 2:
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    Menu_VAN()