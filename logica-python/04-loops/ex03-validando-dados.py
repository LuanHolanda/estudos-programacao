# Validando dados de entrada com um loop

# dado = int(input('Digite um valor maior do que zero: '))
# while (dado <= 0):
#   dado = int(input('Digite um valor maior do que zero: '))
# print(f'Voce digitou {dado}. Encerrando o programa...')

#Exercicio
#Escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuario
#Encerre o algoritmo quando a palavra "sair" for digitada

print('Digite uma mensagem que irei repetir para voce')
print('Para encerrar escreva sair.')
while True:
  texto = input('')
  print(texto)
  if texto == 'sair':
    break
print('Encerrando o programa')

# while True:
#     texto = input('Digite frases ou palavras: ')
#     if texto == 'sair':
#         break
#     print(texto)
# print('Encerrando o programa')

# texto = ''
# while texto != 'sair':
#     texto = input('Digite frases ou palavras: ')
#     if texto != 'sair':
#         print(texto)
# print('Encerrando o programa')