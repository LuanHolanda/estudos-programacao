#Um cinema cobra precos diferentes para os ingressos, de acordo coma idade da pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso sera gratuito; se tiver entre 3 e 12 anos, o ingresso custará R$15; se tiver mais de 12 anos, custara R$30
print("Bem vindos a compra de ingressos do cinema: a seguir insira a idade e quantidade de ingressos")
print("Se tiver menos de 3 anos, o ingresso é gratuito, entre 3 a 12, custa RS15 e maiores de 12 anos pagam R$30")
total = 0
total_pessoas = 0
soma_idades = 0
while True:
  print("Para sair basta digitar '0'")
  idade = int(input("Qual qual sua idade: "))
  
  if idade == 0:
    break
 
  ingressos = int(input("Quantos ingressos deseja compra: "))

  if idade < 3:
    preco = 0
  elif idade <= 12:
    preco = 15
  else:
    preco = 30

  subtotal = preco * ingressos
  total += subtotal

  total_pessoas += 1
  soma_idades += idade
if total_pessoas > 0:
 media = soma_idades / total_pessoas 
else:
 media = 0

print(f'Total de pessoas que compraram ingressos: {total_pessoas}')
print(f'Valor total a pagar: R${total:.2f}')
print(f'Media de idade: {media}')


