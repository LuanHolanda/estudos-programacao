#Escreva um programa que calcule o preco a pagar pelo fornecimento de energia eletrica. Pergunte a quantidade de kWh consumida e o tipo de instalacao: R para residencias, I para industrias e c para comercios
#Calcule o preco de acordo com a tabela a serguir

consumo = float(input('Insira a quantidade de kWh consumida: '))
instalacao = input('Insira o tipo de instalacao:(r)para residencias,(i)para industrias e (c)para comercios: ')

if instalacao not in ('r', 'c', 'i'):
  print('Insira uma instalacao valida!')
elif instalacao == 'r':
  if consumo <= 500:
    valor_pagar = consumo * 0.40
    print(f'Valor a pagar: {valor_pagar}')
  else:
   valor_pagar = consumo * 0.65
   print(f'Valor a pagar: {valor_pagar}')
elif instalacao == 'i':
  if consumo <= 5000:
   valor_pagar = consumo * 0.55
   print(f'Valor a pagar: {valor_pagar}')
  else:
   valor_pagar = consumo * 0.60
   print(f'Valor a pagar: {valor_pagar}')
elif instalacao == 'c':
  if consumo <= 1000:
    valor_pagar = consumo * 0.40
    print(f'Valor a pagar: {valor_pagar}')
  else:
   valor_pagar = consumo * 0.60
   print(f'Valor a pagar: {valor_pagar}')

  #forma que o professor fez (CODIGO MAIS LIMPO E PRATICO)
# if (instalacao == 'r'):
#     if consumo >= 500:
#         preco = 0.65
#     else:
#         preco = 0.4
#     print(f'Total a pagar: {consumo * preco}')
# elif (instalacao == 'c'):
#     if consumo >= 1000:
#         preco = 0.6
#     else:
#         preco = 0.55
#     print(f'Total a pagar: {consumo * preco}')
# elif (instalacao == 'i'):
#     if consumo >= 5000:
#         preco = 0.6
#     else:
#         preco = 0.55
#     print(f'Total a pagar: {consumo * preco}')
# else:
#    print('Instalacao invalida. Encerrando...')