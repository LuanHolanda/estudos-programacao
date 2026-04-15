#Desenvolva um programa que leia um valor inteiro e descubra se ele é par ou impar
number = int(input('Insira um valor inteiro: '))
if (number % 2 == 0) :
  print(f'O numero {number} é par') 
else:
  print(f'O numero {number} é ímpar')