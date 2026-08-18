maisvelho = 0
tothomens = 0
totmulheres = 0
nomemaisvelho = ""
for c in range(1, 8):
    nome = input("Digite seu nome: ")
    idade = int(input(f"Qual a idade de {nome}? "))
    if idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    sexo = input("Qual o sexo? [M/F] ").strip().upper()[0]
    while sexo not in "MF":
        sexo = input("Qual o sexo? [M/F] ").strip().upper()[0] 
    if sexo == "M":
        tothomens += 1
    if sexo == "F":
        totmulheres += 1               
print(f'E a pessoa mais velha entrevistada foi {nomemaisvelho} com {maisvelho} anos.')
print(f'Tivemos um total de {tothomens} homens entrevistados.')
print(f'Tivemos um total de {totmulheres} mulheres entrevistadas.')
