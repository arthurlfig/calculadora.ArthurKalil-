#calculadora
A = float(input("digite o primeiro numero: "))
B = float(input("digite o segundo numero: "))
operação = input("digite o tipo de operação sendo 1- soma 2-subtração 3-multiplicação 4-divisão 5-sair : ")

if operação == "1":
     print(A + B)
elif operação == "2":
   print(A - B)
elif operação == "3":
     print(A * B)
elif operação == "4":
    print(A / B)