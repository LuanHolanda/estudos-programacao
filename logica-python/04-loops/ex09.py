#Escreva um algoritmo que leia um valor e que imprima a quantidade de cedulas necessarias para pagar esse mesmo valor.
#Para simplificar, vamos trabalhar apenas com valores inteiros e com cedulas de R$100, R$50, R$20, R$10, R$5 E R$1

valor = int(input("Insira um valor para calcular quantas cedulas sera necessario para paga-lo: "))

cedulas = 100, 50, 20, 10, 5, 1

for cedula in cedulas:
 valor_cedulas = valor // cedula
 valor %= cedula
 if valor_cedulas > 0:
  print(f'Foram usadas {valor_cedulas} cedulas de R${cedula} para pagar.')
