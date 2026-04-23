## 🟡 EXERCÍCIO 3 – SISTEMA DE PEDIDOS
# Crie um programa com o seguinte menu:
# 1 - Hambúrguer (R$20)
# 2 - Pizza (R$35)
# 3 - Refrigerante (R$8)
# 0 - Finalizar pedido
# Regras:
# * O usuário pode fazer vários pedidos
# * Validar a opção escolhida
# * Para cada item, solicitar a quantidade
# * Não permitir quantidade menor ou igual a zero
# Ao final mostrar:
# * Valor total da compra
# * Quantidade total de itens comprados

print("Bem vindos a lanchonete")
print("Nosso cardapio: 1 - Hambúrguer (R$20) 2 - Pizza (R$35) 3 - Refrigerante (R$8) 0 - Finalizar pedido")

lista_pedidos = {
  "1":{"nome" : "Hambúrguer", "preco" : 20},
  "2":{"nome" :"Pizza", "preco": 35},
  "3":{"nome" :"Refrigerante", "preco": 8},
}
total = 0
carrinho = []

while True:
  pedido = input("Qual item gostaria de comprar: ")

  if pedido == "0":
    break

  if not pedido.isdigit():
    print("Insira um numero!")
    continue

  elif pedido not in lista_pedidos:
    print("Escolha uma opção do cardápio (1, 2 ou 3)")
    continue

  while True:
    quantidade = input("Qual a quantidade do item selecionado gostaria de compra: ")

    if not quantidade.isdigit():
     print("Insira uma quantidade valida!")
     continue
   
    quantidade = int(quantidade)

    if quantidade <= 0:
     print("Quantidade tem que ser maior que 0!")
     continue
    break
  subtotal = lista_pedidos[pedido]["preco"] * quantidade
  print(f'{quantidade} x {lista_pedidos[pedido]["nome"]} Adicionado ao carrinho!')
  total += subtotal
  carrinho.append(f"{quantidade} x {lista_pedidos[pedido]['nome']} - R$ {subtotal:.2f}")

print("\n--- Resumo do pedido ---")
for item in carrinho:
  print(item)
print(f'Total a pagar: R$ {total:.2f}')
