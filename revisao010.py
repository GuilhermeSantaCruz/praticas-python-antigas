num = []
contmaiorX = 0
for n in range(1, 6):
    numero = int(input(f"Digite o {n}º valor: "))
    num.append(numero)
    
print(f"Os números digitados foram {num}")
for v in num:
    if v > 10:
        contmaiorX += 1
print(f"E na lista num tem {contmaiorX} números maiores que 10.")        