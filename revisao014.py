produtos = ("Computador", 1580.00, "Monitor", 840.00, "Mouse", 89.00, "Teclado", 100.00, "Caderno", 38.00, "Lápis", 3.00, "apostilas", 36.00)
print("=-" *20)
print(" LISTAGEM DOS PREÇOS DOS ITENS ")
print("=-" *20)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end="")
    else:
        print(f"R${produtos[pos]:>8.2f}")