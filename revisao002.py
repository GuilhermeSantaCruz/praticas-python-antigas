n1 = int(input("Digite um número: "))  
n2 = int(input("Digite outro número: "))
opção = 0
while opção != 5:
    print('''opções...
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa    ''')
    opção = int(input("Qual a sua opção? "))
    if opção == 1:
        soma = n1 + n2
        print(f"A soma de {n1} e {n2} é igual a {soma} ")
    elif opção == 2:
        multi = n1 * n2
        print(f"O produto de {n1} e {n2} é {multi} ")
    elif opção == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2} ")
        elif n2 > n1:
            print(f"{n2} é maior que {n1} ")
        else:
            print(f"{n1} é igual a {n2} ")
    elif opção == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
    elif opção == 5:
        print("Sair do programa! ")
    else:
        print("Opção errada! ")
    print("-" * 20)    
print("FIM")
                                         
