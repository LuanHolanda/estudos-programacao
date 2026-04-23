#Escreva um algoritmo que leia dois valores numericos e que pergunte ao usuario qual operacao ele deseja realizar: adicao (+), subtracao(-), multiplicacao (*), ou divisao (/).Exiba na tela o resultado da operacao desejada

valor1 = float(input('Insira um valor: '))
valor2 = float(input('Insira outro valor: '))
operacao = input('Qual operacao deseja realizar: ')

if operacao not in ('+','-', '*', '/'):
  print('Insira uma operacao valida!')
elif operacao == '+':
  resultado = valor1 + valor2
  print(f'{valor1} + {valor2} = {resultado}')
elif operacao == '-':
  resultado = valor1 - valor2
  print(f'{valor1} - {valor2} = {resultado}')
elif operacao == '*':
  resultado = valor1 * valor2
  print(f'{valor1} * {valor2} = {resultado}')
elif operacao == '/':
  if valor2 == 0:
   print('Nao se faz divisao por 0!')
  else:
   resultado = valor1 / valor2
   print(f'{valor1} / {valor2} = {resultado}')