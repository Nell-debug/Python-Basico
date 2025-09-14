import datetime
import os 
os.system("cls")
br = None
idade = 0
nome = None
data = None
região = None

while br is None:
    os.system("cls")
    br =input("Você é Brasileiro? ").lower()
    if br in ["s", "sim"]:
            os.system("cls")
            br = "Sim"
            if br == "Sim":
                 regiao = input("Qual região brasileira você mora? ")
                 os.system("cls")
    elif br in ["nao", "não","n"]:
            br = "Não"
            os.system("cls")
            break
    else:
     os.system("cls")
     continue

while nome is None:
     os.system("cls")
     if nome is None:
          nome = input("Como você prefere ser chamado(a)? ")
          os.system("cls")
          break
     else:
         os.system("cls") 
         continue
    
while idade == 0:
     if data is None:
          data = int(input("Qual é o ano em que você nasceu? "))
          os.system("cls")
          aniversario = (input("Você já fez aniversário este ano? ")).lower()
          os.system("cls")
          data1 = datetime.date.today().year
          if data and data1 is not None:
               idade = (data1 - data)
               if aniversario in ["n", "nao", "não"]:
                    idade -= 1
               else: pass
               os.system("cls")

          else:
               continue

print("Olá,", nome,"!")
print("Você tem", idade, "anos de idade.")
if br == "Sim":
     print("E você é brasileiro da região", regiao,".")
elif br == "Não":
     print("E você não é brasileiro.")
