#Escreva um algoritmo que realize um login em um sistema
#O usuario deve informar seu nome e senha

print('Para realizar o login digite Usuario e a Senha')

while True:
  user = input('Usuario: ')
  password = input('Senha: ')
  if user == 'Luan' and password == '5826':
    print('Voce logou')
    break
  else:
    print('Login ou senha invalidos')