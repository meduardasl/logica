print("Adivinhe o Número")

numero_secreto = range.randint(1, 20)
tentativas = 0
acertou = False

while not acertou:
    palpite = int(input("Digite seu palpite (1 a 20): "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        acertou = True 