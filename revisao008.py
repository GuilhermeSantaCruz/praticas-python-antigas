from random import randint
num = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))
print(f"Os números sorteados foram: {num} ",end=" ")
print(f"\nO maior número sorteado foi {max(num)} ")
print(f"O menor número sorteado foi {min(num)} ")
