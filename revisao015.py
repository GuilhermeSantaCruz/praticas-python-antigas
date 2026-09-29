peso = float(input("Qual o seu peso: Kg "))
altura = float(input("Qual a sua altura: Mt "))
imc = peso / altura ** 2
print(f"Seu IMC é {imc}")

if imc < 17:
    print("Muito abaixo do peso") 
elif imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso Ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade")
elif imc < 40:
    print("Obesidade severa")
else:
    print("Obesidade mórbida")
                