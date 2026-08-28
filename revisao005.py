tothomens = 0
totmulheres = 0
nomemaisvelho = ""
nomemaisnovo = ""
somaidade = 0
somasal = 0
contpess = 0
nomemaiorsal = ""
resp = "S"
while resp != "N":
    nome = input("Digite seu nome: ")
    contpess += 1
    idade = int(input(f"Qual a idade de {nome}? "))
    somaidade += idade
    if contpess == 1:
        maisvelho = maisnovo = idade
        nomemaisnovo = nomemaisvelho = nome
    else:
        if idade < maisnovo:
            maisnovo = idade    
            nomemaisnovo = nome
        if idade > maisvelho:
            maisvelho = idade
            nomemaisvelho = nome 
    salario = float(input(f'Qual o seu salário {nome}? R$')) 
    if contpess == 1:
        menorsal = maiorsal = salario 
        nomemaiorsal = nome
    else:
        if salario < menorsal:
            menorsal = salario
        if salario > maiorsal:
            maiorsal = salario
            nomemaiorsal = nome        
    somasal += salario        
    sexo = input("Qual o sexo? [M/F] ").strip().upper()[0]
    while sexo not in "MF":
        sexo = input("Qual o sexo? [M/F] ").strip().upper()[0] 
    if sexo == "M":
        tothomens += 1
    if sexo == "F":
        totmulheres += 1   
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in "SN":
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
mediaidade = somaidade / contpess  
mediasal = somasal / contpess 
print(f'Tivemos um total de {contpess} pessoas entrevistadas.')    
print(f'E a pessoa mais nova entrevistada foi {nomemaisnovo} com {maisnovo} anos.')                    
print(f'E a pessoa mais velha entrevistada foi {nomemaisvelho} com {maisvelho} anos.')
print(f'Tivemos um total de {tothomens} homens entrevistados.')
print(f'Tivemos um total de {totmulheres} mulheres entrevistadas.')
print(f'A idade média das pessoas entrevistadas é de {mediaidade:.1f} anos.')
print(f'A média salarial dos entrevistados é R${mediasal:.2f}')
print(f'O menor salário entre os entrevistados foi R${menorsal:.2f}')
print(f'E o maior salário entre os entrevistados foi de {nomemaiorsal} que é R${maiorsal:.2f}')
