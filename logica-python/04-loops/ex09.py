#Escreva um algoritmo que leia um valor e que imprima a quantidade de cedulas necessarias para pagar esse mesmo valor.
#Para simplificar, vamos trabalhar apenas com valores inteiros e com cedulas de R$100, R$50, R$20, R$10, R$5 E R$1

valor = int(input("Insira um valor para calcular quantas cedulas sera necessario para paga-lo: "))

cedulas = 100, 50, 20, 10, 5, 1

for cedula in cedulas:
 valor_cedulas = valor // cedula
 valor %= cedula
 if valor_cedulas > 0:
  print(f'Foram usadas {valor_cedulas} cedulas de R${cedula} para pagar.')

#Resposta do professor
# valor = int(input("Digite o valor em R$: "))
# while True:
#  if valor >= 100:
#   cont100 = valor // 100
#   valor = valor - cont100 * 100
#   print(f"Cedulas de 100: {cont100}")
#   if not valor:
#    break

#   if valor >= 50:
#    cont50 = valor // 50
#    valor = valor - cont50 * 50
#    print(f"Cedulas de 50: {cont50}")
#    if not valor:
#     break

#   if valor >= 20:
#    cont20 = valor // 20
#    valor = valor - cont20 * 20
#    print(f"Cedulas de 20: {cont20}")
#    if not valor:
#     break

#   if valor >= 5:
#    cont5 = valor // 5
#    valor = valor - cont5 * 5
#    print(f"Cedulas de 5: {cont5}")
#    if not valor:
#     break

#   if valor:
#    cont1 = valor
#    print(f"Cedulas de 1: {cont1}")
#    break