#Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete:
#Coxinha - R$5,00
#Pastel - R$7,00
#Cafe - R$4,00
#Suco - R$6,00

print("Lanchonete")
print("1 - Coxinha R$ 5,00")
print("2 - Pastel  R$ 7,00")
print("3 - Cafe    R$ 4,00")
print("4 - Suco    R$ 6,00")

cardapio = {
    "1": {"nome": "Coxinha", "preco": 5.00},
    "2": {"nome": "Pastel",  "preco": 7.00},
    "3": {"nome": "Cafe",    "preco": 4.00},
    "4": {"nome": "Suco",    "preco": 6.00},
}

total = 0
carrinho = []  # guarda o que foi comprado

while True:
    print("\nPara fechar o carrinho digite: sair")
    escolha = input("Qual produto deseja: ")

    if escolha == "sair":
        break
    elif escolha not in cardapio:
        print("Insira um numero valido dos produtos!")
        continue

    while True:
        quantidade = input("Quantos deseja comprar: ")
        if not quantidade.isdigit():
            print("Insira apenas números!")
            continue
        quantidade = int(quantidade)
        if quantidade <= 0:
            print("Insira uma quantidade valida!")
            continue
        break

    subtotal = cardapio[escolha]["preco"] * quantidade
    total += subtotal
    carrinho.append(f'{quantidade}x {cardapio[escolha]["nome"]} - R$ {subtotal:.2f}')

# resumo do pedido
print("\n--- Resumo do pedido ---")
for item in carrinho:
    print(item)
print(f'Total a pagar: R$ {total:.2f}')