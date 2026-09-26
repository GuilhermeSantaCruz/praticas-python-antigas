from random import randint
computador = randint(0, 10)
print("Sou seu computador... E já pensei em um número de 0 a 10 ")
print("Tente adivinhar....")
acertou = False
tentativas = 0
while acertou == False:
    jogador = int(input("Escolha um valor de 0 a 10: "))
    tentativas += 1
    if computador == jogador:
        acertou = True
        print(f"Parabens! Você acertou com {tentativas} tentativas ")
    elif computador > jogador:
        print("ERROU! Tente com um número maior no qual você digitou ") 
    elif computador < jogador:
        print("ERROU! Tente com um número menor no qual você digitou ") 
print("FIM DO PROGRAMA!")