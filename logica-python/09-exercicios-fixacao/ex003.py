""" EXERCÍCIO 3 - Conteúdos até aula 05
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de
uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:
• Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
• Serviço de Impressão Colorida (ICO) o custo por página é de um real;
• Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta
centavos;
• Serviço de Fotocópia (FOT) o custo por página é de vinte centavos;
▪ Se número de páginas for menor que 20 retornar o número de página sem desconto;
▪ Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número
de páginas com o desconto é de 15%;
▪ Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o
número de páginas com o desconto é de 20%;
▪ Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o
número de páginas com o desconto é de 25%;
▪ Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa
quantidade de páginas;
♦ Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
♦ Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40
reais;
♦ Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;
O valor final da conta é calculado da seguinte maneira:
total = (servico * num_pagina) + extra """

#FUNCAO PARA  VALIDAR A ESCOLHA DOS SERVICOS
def escolha_servico():
  while True:
    servico = input("Qual servico desejado: ").strip().lower()
    if not servico in ("dig", "ico", "ipb", "fot", "sair"):
      print("Servico invalido! Tente navamente.")
      continue
    else:
      print("Servico Selecionado com sucesso!")
      return servico
    
#FUNCAO PARA  VALIDAR O NUMERO DE PAGINAS
def num_pagina():
  while True:
    try:
      paginas = int(input("Numero de paginas: "))
    except ValueError:
      print("Valor invalido! Tente novamente.")
      continue
    if 1 <= paginas < 20000:
      return paginas
    else:
      print("O numero de paginas nao pode ser 0 ou negativo nem exceder 20.000! Tente novamente.")
#FUNCAO PARA  VALIDAR O SERVICO EXTRA
def servico_extra(): 
  while True:
    servico = input("Deseja o servico extra? ")
    if not servico in ('1', '2', '0'):
      print("Servico extra invalido! Insira algum servico que fornecemos.")
    else:
      print(f"Servico {extras[servico][0]} extra selecionado.")
      return servico
    
#FUNCAO PARA O DESCONTO
def aplicar_desconto(paginas):
  if paginas < 20:
    desconto = 0
  elif paginas < 200:
    desconto = 15
  elif paginas < 2000:
    desconto = 20
  else:
    desconto = 25
  return desconto
    
# MENU DE APRESENTACAO DOS SERVICOS
print("=" * 55)
print("BEM-VINDO À COPIADORA DO LUAN HOLANDA".center(55))
print("=" * 55)
print("\nSERVIÇOS DISPONÍVEIS:\n")
print(f"| {'CÓDIGO':^10} | {'SERVIÇO':^30} | {'PREÇO':^10} |")
print("-" * 55)
print(f"| {'DIG':^10} | {'Digitalização':^30} | {'R$ 1.10':^10} |")
print(f"| {'ICO':^10} | {'Impressão Colorida':^30} | {'R$ 1.00':^10} |")
print(f"| {'IPB':^10} | {'Impressão Preto e Branco':^30} | {'R$ 0.40':^10} |")
print(f"| {'FOT':^10} | {'Fotocópia':^30} | {'R$ 0.20':^10} |")
print("=" * 55)
print("\nSERVIÇOS ADICIONAIS:\n")
print(f"| {'CÓDIGO':^10} | {'ADICIONAL':^30} | {'VALOR':^10} |")
print("-" * 55)
print(f"| {'1':^10} | {'Encadernação Simples':^30} | {'R$ 15':^10} |")
print(f"| {'2':^10} | {'Encadernação Capa Dura':^30} | {'R$ 40':^10} |")
print(f"| {'0':^10} | {'Sem Adicional':^30} | {'R$ 0':^10} |")
print("=" * 55)
#DICIONARIO DOS VALORES DOS SERVICOS
servicos = {
    'dig': 1.10,
    'ico': 1.00,
    'ipb': 0.40,
    'fot': 0.20
}
#DICIONARIO DOS VALORES DOS SERVICOS EXTRAS
extras = {
    '1': ('Encadernação Simples',15),
    '2': ('Encadernação Capa Dura',40),
    '0': ('Sem adicional',0)
}

carrinho = 0

# PROGRAMA PRINCIPAL
while True:
  servico = escolha_servico()

  if servico == "sair":
      print("Encerrando...")
      break
  
  paginas = num_pagina()

  valor = servicos[servico] * paginas

  valor_desconto = valor * aplicar_desconto(paginas) / 100

  valor_com_desconto = valor - valor_desconto

  extra = servico_extra()

  valor_total = extras[extra][1] + valor_com_desconto
  carrinho += valor_total

  print(f"valor total a pagar {carrinho}")

  

    