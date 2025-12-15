contador = 1
soma_pares = 0
soma_impares = 0

while contador <= 10:
    numero = int(input(f"Digite o {contador}º número: "))

    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

    contador += 1

print("\nSoma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)