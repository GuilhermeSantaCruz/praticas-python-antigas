sexo = "g"
nome = input("Qual é o seu nome? ")
nascimento = int(input("Em que ano você nasceu? "))
while sexo not in "MmFf":
    sexo = input("Qual o seu sexo? ").strip().upper()[0]
print(f"{nome} nasceu no ano de {nascimento} e o seu sexo é {sexo}.")
print("Fim do programa. ")

