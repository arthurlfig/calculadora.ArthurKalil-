op = 0 
while op != 5: 
    print("\n escolha sua operação \n 1-soma \n 2- subtração \n 3-multiplicação \n 4-divisão \n 5- sair ")
    op =int(input('\n digite sua escolha d eoperação: '))

    if op > 5 or op < 0:
          print("digite sua opção de 1 a 5: ")
          continue 
    elif op == 5:
         print("saiu da calculadora")
         break
    n1 = int(input('digite o primeiro numero que vai fazer parte da operação: \n'))
    n2 = int(input('digite o segundo numero que vai fazer parte da operação: \n'))

    if op == 1:
         print(f"a soma de {n1} + {n2} é de \n {n1 + n2}")
    elif op == 2:
         print(f'a subtração de {n1} - {n2} é de \n {n1 - n2}')
    elif op == 3:
         print(f'a subtração de {n1} x {n2} é de \n {n1 * n2}')
    elif op == 4:
         print(f'a subtração de {n1} / \n {n2} é de \n {n1  / n2}')