n1 = float(input("Digite o 1° número: "))
n2 = float(input("Digite o 2° número: "))
n3 = float(input("Digite o 3° número: "))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2 
else:
    maior = n3 
print("O maior número é:", maior)