opcao = 0
while opcao != 3:
  print("1- SOMAR")
  print("2- SUBTRAIR")
  print("3- SAIR")
  opcao = int(input("escolha: "))
  if opcao == 1:
    a = float(input("seu numero: "))
    b = float(input("seu numerp: "))
    print("resultado:", a+b)
    
  elif opcao == 2:
      a = float(input("1 numero: "))
      b = float(input("2 numero: "))
      print("resultado: ", a-b)
      
  else:
    print("invalido")