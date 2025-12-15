contador = 1
produto = 1 

while contador <= 10:
    numero = int(input(f"Digite o {contador}º número : "))
    produto = produto * numero 
    contador += 1

print(f"\nO produto de todos os números é: {produto}")
