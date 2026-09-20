num = []
contmaiorX = 0
contpar = 0
contimpar = 0
for n in range(1, 6):
    numero = int(input(f"Digite o {n}º valor: "))
    num.append(numero)
    if numero % 2 == 0:
        contpar += 1
    else:
        contimpar += 1    
print(f"Na lista num tem {contpar} valores PARES!") 
print(f'Na lista num tem {contimpar} valores ÍMPARES')   
print(f"Os números digitados foram {num}")
for v in num:
    if v > 10:
        contmaiorX += 1
print(f"E na lista num tem {contmaiorX} números maiores que 10.")        