#Exercicio 2
#Escreva um algoritmo que leia um nome e uma idade
#Caso o nome digitado seja Vinicius, escreva isso na tela
#Caso o usuario digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for maior que 100 anos, informe que esta pessoa possivelmente nao existe

nome = input('Insira um nome: ')
idade = int(input('Insira uma idade: '))

if nome == 'Vinicius':
  print('Ola, Vinicius')

elif idade < 18:
 print('Voce é menor de idade')

elif idade > 100:
 print('Essa pessoa possivelmente nao existe')

else:
 print(f'Seu nome é {nome} e sua idade é {idade}')