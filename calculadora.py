import math
import os
os.system("cls")

cal = input("Digite o cálculo: ")  
partes = cal.split()
resultado = 0

if len(partes) == 2 and partes[1] == "v":
    n1 = float(partes[0])
    resultado = math.sqrt(n1)

elif len(partes) == 3:
    n1, op, n2, i = partes
    n1 = float(n1)
    n2 = float(n2)
    op = ""
    i = ""

    if op == "+":
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "x":
        resultado = n1 * n2
    elif op == "/":
        if len(partes) == 3 and partes[3] == 0:
            resultado = int(n1 / n2)
        elif n2 != 0:
            resultado = n1 / n2
        else:
            print("Erro: divisão por zero")
            resultado = None
    else:
        print("Operador inválido")
        resultado = None

else:
    print("Formato inválido de cálculo")
    resultado = None


if resultado is not None:
   if len(partes) == 3:
    print(int(f"{resultado}"))
    print(f"o resto é{resultado : %}")
   elif isinstance(resultado, float) and resultado.is_integer():
        print(int(resultado))
   else:
        print(f"{resultado:.2f}")
