alunos = []
while True:
    nome = input("Nome: ")
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    resp = input("Quer continuar? [S/N] ").strip().upper()[0]
    if resp in "N":
        break
print("**" * 15)    
print(f"No. Nome         Média")
print("-" * 28) 
for i, a in enumerate(alunos):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(alunos) - 1:
        print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]} ")    
print("Finalizando o programa")