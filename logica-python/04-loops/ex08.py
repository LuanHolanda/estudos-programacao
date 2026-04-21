#Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete:
#Coxinha - R$5,00
#Pastel - R$7,00
#Cafe - R$4,00
#Suco - R$6,00
# print('Lanchonete') essa forma fiz com ajuda
# print('Escolha um produto que deseja comprar')
# print('1-Coxinha - R$5,00/', '2-Pastel - R$7,00/', '3-Cafe - R$4,00/', '4-Suco - R$6,00')
# cardapio = {
#     "1": {"nome": "Coxinha", "preco": 5.00},
#     "2": {"nome": "Pastel", "preco": 7.00},
#     "3": {"nome": "Cafe", "preco": 4.00},
#     "4": {"nome": "Suco", "preco": 6.00},
# }

# while True:
#   escolha = input("Qual o número? ")
#   if escolha not in cardapio:
#    print('Insira um item que esteja no nosso cardapio')
#    continue

#   item = cardapio[escolha]
#   print(f"Selecionaste: {item['nome']}")

#   quantidade = int(input("Quantos deseja comprar: "))
#   if quantidade <= 0:
#     print("A quantidade deve ser maior que zero!")
#     continue

#   print(f'Voce comprou {quantidade}, {item['nome']}. Valor total a pagar R${quantidade * item["preco"]}')
#   break
print("Lanchonete")
print("1 - Coxinha R$ 5,00")
print("2 - Pastel R$ 7,00")
print("3 - Cafe R$ 4,00")
print("4 - Suco R$ 6,00")

cardapio = {
    "1": {"nome": "Coxinha", "preco": 5.00},
    "2": {"nome": "Pastel", "preco": 7.00},
    "3": {"nome": "Cafe", "preco": 4.00},
    "4": {"nome": "Suco", "preco": 6.00},
}
total = 0
while True:
  print("\nPara fechar o carrinho basta digitar sair")
  escolha = input('Qual produto deseja: ')
  if escolha == "sair":
   break
  elif escolha not in cardapio:
    print('Insira um numero valido dos produtos')
    continue 
  while True:
   quantidade = input('Quantos deseja comprar: ')
   if not quantidade.isdigit():
        print('Insira apenas números!')
        continue
   quantidade = int(quantidade)
   if quantidade <= 0:
     print('Insira uma quantidade valida')
     continue
   break
  total += cardapio[escolha]["preco"] * quantidade
print(f'Voce comprou {quantidade}. total a pagar {total}')

# Versão 1 - meu primeiro código com while e dicionário
# Data: 21/04/2025
# O que aprendi: while True, break, continue, dicionários


  
  