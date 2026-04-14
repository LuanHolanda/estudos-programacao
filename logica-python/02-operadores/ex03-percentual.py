#Exercício 2.3: desenvolva um algoritmo que solicite ao usuário o preço
#de um produto e um percentual de desconto a ser aplicado a ele. Calcule-o e
#exiba o valor do desconto e o preço final do produto.

preco = float(input('Qual é o valor do produto? '))
desconto = float(input('Qual valor do desconto a ser aplicado? '))


resultado = preco * (desconto / 100)
total = preco - resultado
#MANEIRA MAIS UTILIZADA
print(f'O valor do desconto é: {resultado}%')
print(f'O valor a ser pago é: {total}')

#MANEIRA CLASSICA
print('O preco do produto é %.2f Desconto de %0f%.' % (preco, desconto))
print('O valor calculado de desconto: %.2f% Valor fianl do produto: %.2f' %(desconto, resultado))
#MANEIRA MODERNA
print('O preco do produto é {}, Desconto de {}%'.format(preco, desconto))
print('O valor calculado de desconto: {}. Valor fianl do produto: {}' .format(desconto, resultado))
