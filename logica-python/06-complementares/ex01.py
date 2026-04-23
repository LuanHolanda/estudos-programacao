#Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela. Para fins de simplificação, despreze o dia e o mês do ano. Após o cálculo, verifique se a idade é maior ou igual a 18 anos e apresente na tela uma mensagem informando que já é possível tirar a carteira de motorista caso seja de maior.

ano_nascimento = int(input('Insira seu ano de nascimento: '))
ano_atual = int(input('Insira o ano atual: '))

idade = (ano_atual - ano_nascimento)

if idade >= 18:
  print(f'Voce tem {idade} anos, ja é possivel tirar carteira de motorista')
else:
  print(f'Voce so tem {idade} anos, nao é possivel tirar carteira de motorista')

