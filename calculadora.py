import math
import os

os.system("cls")
entrada = input("Digite a conta: ")
os.system("cls")

partes = entrada.split()
x = float(partes[0]) if "." in partes[0] else int(partes[0])
op = partes[1]
y = float(partes[2]) if len(partes) == 3 else None

if op == "+":
    resultado = x + y
elif op == "-":
    resultado = x - y
elif op in ["*", "x"]:
    resultado = x * y
elif op == "/":
    resultado = x / y
elif op == "//":
    resultado = x // y
    resto = x % y
elif op == "v":
    resultado = math.sqrt(x)
elif op == "^":
    resultado = math.pow(x, y)
elif op == "%":
    resultado = (y / 100) * x
else:
    print("Erro")
    resultado = None

if resultado is not None:
    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado) 
    if op == "v":
        print(f"√ {x} = {resultado}")
    elif op == "//":
        print(f"{x} // {y} = {resultado} com resto {resto}")
    else:
        print(f"{x} {op} {y:.0f} = {resultado}")
