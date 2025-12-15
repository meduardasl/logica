quantidade = 0
soma = 0
maior = None
menor = None
pares = 0

while True:
    num = float(input("Digite um número (0 para parar): "))

    if num == 0:
        break

    quantidade += 1
    soma += num

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    if num % 2 == 0:
        pares += 1

if quantidade > 0:
    media = soma / quantidade
    print("\n RESULTADOS ")
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Quantidade de números pares: {pares}")
else:
    print("Nenhum número foi digitado.")