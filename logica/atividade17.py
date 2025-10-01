n1 = float(input("Digite o 1 numero: "))
n2 = float(input("Digite o 2 numero: "))
if n2 == 0:
    print("não é possível dividir por 0")
elif n1 % n2 == 0:
    print("n1 é divisivel por n2")
else:
    print("n1 não é divisível por n2")