#Escreva um algoritmo em Python em que o usuario escolhe se quer comprar macas, laranjas ou bananas. Devera ser apresentado na tela um menu com as opcoes 1 para maca, 2 para laranja e 3 para banana
#Apos escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preco total a pagar do produto escolhido e mostra-lo na tela
#Considere que uma maca custa R$2,30, uma laranja R$3,60, e uma banana R$1,85

frutas = int(input('Menu de frutas opcao 1 para maca, 2 para laranja e 3 para banana. Qual fruta deseja comprar: '))
quantidade = int(input('Quantas unidades deseja comprar: '))

if frutas == 1:
  preco = quantidade * 2.30
  print(f'Voce comprou {quantidade} macas. O valor total a pagar é R${preco:.2f}')

elif frutas == 2:
  preco = quantidade * 3.60
  print(f'Voce comprou {quantidade} laranjas. O valor total a pagar é R${preco:.2f}')

elif frutas == 3:
  preco = quantidade * 1.85
  print(f'Voce comprou {quantidade} bananas. O valor total a pagar é {preco:.2f}')

else:
  print('Valor invalido, insira um valor de acordo com as opcoes!')


