def bisiesto (aa):
    if aa % 4 == 0 and aa % 100 == 0 and aa % 400 == 0:
        return True 
    elif aa % 4 == 0 and aa % 100 == 0:
        return False
    elif aa % 4 == 0:
        return True  

def verificar (dd, mm, aa):
    if dd > 0 and dd < 32:
        if mm > 0 and mm < 13:
            if bisiesto (aa) == True:
                feb = dias_x_mes[1] + 1
                return True
            elif bisiesto (aa) == False:
                return True
            else:
                return False
        else:
            return False
            
    else:
        return False

dias_x_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))

    if verificar(dia, mes , anio) == True:
        print("fecha valida")

    else:
        print("fecha invalida")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()