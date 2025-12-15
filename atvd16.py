print("Contagem de Números Positivos")

positivos = 0

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > 0:
        positivos += 1

print(f"Quantidade de números positivos digitados: {positivos}")