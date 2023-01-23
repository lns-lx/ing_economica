def tir(cf, low=0, high=1, epsilon=0.01):
   
    while abs(high - low) > epsilon:
        mid = (low + high) / 2.0
        npv_low = sum([cf[i] / ((1 + low) ** (i+1)) for i in range(len(cf))])
        npv_mid = sum([cf[i] / ((1 + mid) ** (i+1)) for i in range(len(cf))])
        if npv_low * npv_mid < 0:
            high = mid
        else:
            low = mid
    return mid

def Menu_TIR():
    while True:
        print("\n1. Calcular TIR")
        print("2. Regresar al menu principal\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            cash_flow = []
            print("Ingrese los flujos de caja descontados: ")
            while True:
                val = input()
                if val == "":
                    break
                cash_flow.append(float(val))
            r = tir(cash_flow)
            print(f"La Tasa Interna de Retorno es: {r:.2f}")
        elif opcion == 2:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Menu_TIR()