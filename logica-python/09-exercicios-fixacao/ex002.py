""" EXERCÍCIO 2 - Conteúdos até aula 04
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um
app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de
desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:
• Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
• Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
• Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;
Elabore um programa em Python que:
A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu
nome e sobrenome (somente print, não usar input aqui);
B. Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente
novamente" se o usuário entra com valor diferente de CP e AC;
C. Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido.
Tente novamente" se o usuário com entra valor diferente de P, M ou G;
D. Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema
4) com cada uma das combinações de sabor e tamanho;
E. Deve-se implementar um acumulador para somar os valores dos pedidos;
F. Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”.
Se sim repetir a partir do item B, senão encerrar o programa executar o print do
acumulador;
G. Deve-se implementar as estruturas de while, break, continue (todas elas);
H. Deve-se inserir comentários relevantes no código;
Teste seu código atendendo as seguintes exigências:
I. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu
nome e sobrenome;
J. Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor;
K. Deve-se apresentar na saída de console um pedido em que o usuário errou o
tamanho;
L. Deve-se apresentar na saída de console um pedido com duas opções sabores
diferentes e com tamanhos diferentes; """


print("Boas vindas a loja de acai e cupuacu do Luan Holanda")
print("Caso queira acai basta inserir (AC) no campo sabor o mesmo pro cupuacu (CP) e o tamanho (P) R$11, (M) R$16, (G) R$20")

def valida_sabor(): #funcao para validar o input do sabor
  while True:
    sabor = input("Escolha o sabor: ").strip().upper()
    if sabor in ('AC', 'CP'):
      print(f'Sabor {sabor} selecionado')
    else:
      print('Sabor invalido! Tente novamente.')
      continue
    return sabor
  
def valida_tamanho(): #funcao para validar o input do tamanho
  while True:
    tamanho = input('Selecione o tamanho: ').strip().upper()
    if tamanho in ('P', 'M','G'):
      print(f'Tamanho {tamanho} selecionado')
    else:
      print('Tamanho invalido! Tente navamente.')
      continue
    return tamanho

def valida_quantidade():
  while True:
    try:
      qtd = int(input("Quantos deseja comprar: "))
    except ValueError:
      print("Quantidade invalida! Tente novamente.")

    return qtd
  
carrinho = 0

while True:
  print("=" * 45)
  print("CARDAPIO".center(45))
  print("=" * 45)
  print(f"| {'Tamanho':^10} | {'Cupuacu (CP)':^14} | {'Acai (AC)':^12} |")
  print("-" * 45)
  print(f"| {'P':^10} | {'R$ 9.00':^14} | {'R$ 11.00':^12} |")
  print(f"| {'M':^10} | {'R$ 14.00':^14} | {'R$ 16.00':^12} |")
  print(f"| {'G':^10} | {'R$ 18.00':^14} | {'R$ 20.00':^12} |")
  print("=" * 45)

  sabor = valida_sabor()
  tamanho = valida_tamanho()
  qtd = valida_quantidade()

  if sabor == 'AC':
    if tamanho == 'P':
      preco = 11
      valor = qtd * preco
    elif tamanho == 'M':
      preco = 16
      valor = qtd * preco
    elif tamanho == 'G':
      preco = 20
      valor = qtd * preco
    print(f'Voce pediu {qtd} acai no tamanho {tamanho}: R${preco}')

  if sabor == 'CP':
    if tamanho == 'P':
      preco = 9
      valor = qtd * preco
    elif tamanho == 'M':
      preco = 14
      valor = qtd * preco
    elif tamanho == 'G':
      preco = 18
      valor = qtd * preco
    print(f'Voce pediu {qtd} cupuacu no tamanho {tamanho}: R${preco}')

  carrinho += valor
  
  opcao = input("Deseja pedir mais alguma coisa? ").strip().lower()
  if opcao == 'sim':
    continue
  else:
    print("Encerrando o programa...")
    break

print(f"Valor total do pedido R${carrinho:.2f}")

