sexo = "g"
nome = input("Qual é o seu nome? ")
while sexo not in "MmFf":
    sexo = input("Qual o seu sexo? ").strip().upper()[0]
print(f"{nome} é do sexo {sexo}.")        
print("Fim do programa. ")

