n = int(input("Digite um número: "))
soma = 0
contador = 1
while contador <= n:
    soma += contador
    contador += 1
print(f"A soma dos números de 1 até o {n} é o {soma}.")