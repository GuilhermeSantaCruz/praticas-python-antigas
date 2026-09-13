contimpar = 0
numpar = []
contpar = 0
totpar = 0
num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))
print(num, end=" ")
print(f"\nO número 9 apareceu {num.count(9)} vezes ")
print(f'A soma dos valores é {sum(num)}')
print(f'Os números da tupla num em ordem crescente são: {sorted(num)}')
print(f'O maior número da tupla num é {max(num)} e apareceu {num.count(max(num))} vezes.')
print(f'Ele apareceu pela primeira vez na {num.index(max(num))+1}ª posição.')
print(f'O menor número da tupla num é {min(num)} e ele apareceu na {num.index(min(num))+1}ª posição')
if 3 in num:
       print(f"O número 3 apareceu na {num.index(3)+1}ª posição. ")
else:
       print("O número 3 não apareceu em nenhuma posição. ")       
for n in num:
       if n % 2 == 0:
              numpar.append(n)              
       else:
              contimpar += 1 
for p in numpar:
       contpar += 1
       totpar += p
       if contpar == 1:
              maiorpar = p
       if p > maiorpar:
              maiorpar = p
if contpar > 0:
       print(f'Os números pares digitados foram: {numpar}')
       print(f'Foram digitados {contpar} números pares')
       print(f'O maior par da tupla num é: {maiorpar}')
       print(f'A soma dos números pares é {totpar}')
else:
       print('Não foi digitado nenhum número PAR.')                                         
print(f'E na tupla num tem {contimpar} números ímpares.')