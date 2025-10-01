altura = float(input("Seu altura: "))
peso = float(input("Seu peso: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidade")