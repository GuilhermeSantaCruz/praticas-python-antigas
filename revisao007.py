classificação = ("Flamengo", "Cruzeiro", "Palmeiras", "Mirassol",
                 "Botafogo", "Bahia", "São Paulo", "Fluminense",
                 "Bragantino", "Vasco da Gama", "Corinthians",
                 "Grêmio", "Ceará", "Atlético MG", "Internacional",
                 "Santos", "Juventude", "Vitória", "Fortaleza", "Sport")
print(f"Os times em ordem alfabética: {sorted(classificação)}")
print(f"O Ceará está na {classificação.index('Ceará')+1}ª posição ")
print(f"Os times que estão se classificando para a libertadores são {classificação[:5]}")
print(f'os times que estão na zona de rebaixamento são {classificação[-4:]}')
