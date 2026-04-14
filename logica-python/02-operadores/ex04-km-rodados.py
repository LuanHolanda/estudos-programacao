#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuario, assim como a quatidade de dias pelos quais o carro foi alugado. calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado#

kilometros = float(input('Qual a quantidade de km percorrido? '))
aluguel = float(input('Por quantos dias o carro foi alugado? '))

percorrido = (kilometros * 0.15)
dias = (aluguel * 60)
total = percorrido + dias

if total >= 500 :
 desconto = total * (10 / 100)
 conta = total - desconto
 print(f'A conta passou de R$500.00 Desconto de 10% foi aplicado!')
else:
 conta = total

print(f'Valor a ser pago referente ao aluguel R${dias:.2f}, e o valor a ser pago referente aos kms rodados R${percorrido:.2f}. Resultando em um total de R${conta:.2f}')
