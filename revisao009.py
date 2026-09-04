numpar = 0
num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))
print(num, end=" ")
print(f"\nO número 9 apareceu {num.count(9)} vezes ")
print(f'A soma dos valores é {sum(num)}')
print(f'O maior número da tupla num é {max(num)}')
print(f'O menor número da tupla num é {min(num)}')
if 3 in num:
       print(f"O número 3 apareceu na {num.index(3)+1}ª posição. ")
else:
       print("O número 3 não apareceu em nenhuma posição. ")       
print("Os números pares digitados foram: ", end="")
for n in num:
       if n % 2 == 0:
              numpar += 1
              print(n, end=" ")
print()              
print(f'E na tupla num tem {numpar} números pares.')