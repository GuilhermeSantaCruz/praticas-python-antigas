resp = "S"
c = 0
soma = 0
media = 0
while resp != "N":
    n = int(input("Digite um número: "))
    c += 1
    soma += n
    media = soma / c
    resp = input("Quer continuar? [S/N] ").strip().upper() [0]
print(f"Você digitou {c} números ")
print(f"A soma de todos os números é {soma}")  
print(f"E a média é {media} ")
  