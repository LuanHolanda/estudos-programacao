# Escreva as seguintes expressoes algebricas em linguagem python:
#a) O somatorio dos 5 primeiros numero inteiros e positivos
soma = (1 + 2 + 3 + 4 + 5)
print(f'A soma dos 5 primeiros numeros inteiros e positivos é: {soma}')
#forma diferente de fazer
soma = 0
for i in range(1, 6):
    soma += i
print(f'A soma é: {soma}')
#forma mais avancada
soma = sum(range(1, 6))
print(f'A soma é: {soma}')
#---------------------------------------------
#b) A media entre 23, 19 e 31
media = (23 + 19 + 31) / 3
print(f'A media entre 23, 19 e 31 é: {media:.2f}')
#c) O numero de vezes que 73 cabe em 403
media = 403 // 73
print(f'O numero 73 cabe {media} vezes dentro do numero 403')
#d) A sobra quando 403 é dividido por 73
sobra = 403 % 73
print(f'A sobra da divisao 403 / 73 é: {sobra}')

#REGRAS IMPORTANTES
# // → divisão inteira
# %  → resto da divisão

#e) 2 elevado a 10 potencia
potencia = (abs(2**10)) #abs pega o valor absoluto
print(f'2 elevado a decima potencia é: {potencia}')
#f) O valor absoluto da diferenca entre 54 e 57
diferenca = (54 - 57)
print(f'A diferenca absoluta entre 54 e 57 é: {diferenca}')
#g) O menor valor entre 34, 29 e 31
valor = (min(34, 29, 31)) #min pega o valor minimo
print(f'O menor valor entre 34, 29 e 31 é: {valor}')