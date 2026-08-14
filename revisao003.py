cont = 0
soma = 0
c = 0
while cont != 999:
    cont = int(input("Digite qualquer valor: [999] para encerrar o programa. "))
    c += 1
    soma += cont
    
print(f"Ao todo você digitou {c - 1} números e a soma deles é {soma - 999} ")
