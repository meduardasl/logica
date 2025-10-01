temperatura = float(input("Termômetro: "))
if temperatura <= 18:
    print("Frio")
elif 19 <= temperatura <= 25:
    print("Agradável")
else:
    print("Quente")