tothomens = 0
totmulheres = 0
nomemaisvelho = ""
nomemaisnovo = ""
somaidade = 0
for c in range(1, 8):
    nome = input("Digite seu nome: ")
    idade = int(input(f"Qual a idade de {nome}? "))
    somaidade += idade
    if c == 1:
        maisvelho = maisnovo = idade
        nomemaisnovo = nomemaisvelho = nome
    else:
        if idade < maisnovo:
            maisnovo = idade    
            nomemaisnovo = nome
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
mediaidade = somaidade / 7        
print(f'E a pessoa mais nova entrevistada foi {nomemaisnovo} com {maisnovo} anos.')                    
print(f'E a pessoa mais velha entrevistada foi {nomemaisvelho} com {maisvelho} anos.')
print(f'Tivemos um total de {tothomens} homens entrevistados.')
print(f'Tivemos um total de {totmulheres} mulheres entrevistadas.')
print(f'A idade média das pessoas entrevistadas é de {mediaidade:.1f} anos.')

