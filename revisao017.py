from datetime import datetime
trabalhador = {}
trabalhador["nome"] = input("Nome: ")
nasc = int(input("ano de nascimento: "))
trabalhador["idade"] = datetime.now(). year - nasc
trabalhador["Carteira"] = int(input("Carteira de trabalho: (digite 0 caso não tenha) "))
if trabalhador["Carteira"] != 0:
    trabalhador["contratação"] = int(input("Amo de contratação: "))
    trabalhador["salário"] = float(input("Salário: R$ "))
    trabalhador["aposentadoria"] = trabalhador["idade"] + ((trabalhador["contratação"] + 35) - datetime.now().year)
print("**" * 20)  
for k, v in trabalhador.items():
    print(f"  - {k} tem o valor {v} ")