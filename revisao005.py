maisvelho = 0
for c in range(1, 5):
    nome = input("Digite seu nome: ")
    idade = int(input(f"Qual a idade de {nome}? "))
    if idade > maisvelho:
        maisvelho = idade
    sexo = input("Qual o sexo? [M/F] ").strip().upper() [0]    
print(f'A pessoa mais velha entrevistada tem {maisvelho} anos.')
