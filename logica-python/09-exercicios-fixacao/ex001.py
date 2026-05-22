""" EXERCÍCIO 1 – Conteúdos até Aula 3
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção
de um app de vendas para uma determinada empresa X que vende em atacado. Uma das
estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra,
conforme a listagem abaixo:os futuros chats."
• Se valor_total for menor que 2500 o desconto será de 0%;
• Se valor_total for maior ou igual que 2500 e menor que 6000 o desconto será de
4%;
• Se valor_total for maior ou igual que 6000 e menor que 10000 o desconto será
de 7%;
• Se valor_total for maior ou igual que 10000 o desconto será de 11%;
Elabore um programa em Python que:
A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu
nome e sobrenome (somente print, não usar input aqui);
B. Deve-se implementar o input do valor unitário e da quantidade do produto;
C. Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se
as condições de menor, igual e maior;
D. Deve-se implementar o valor total sem desconto e o valor total com desconto;
E. Deve-se implementar as estruturas if, elif e else (todas elas);
F. Deve-se inserir comentários relevantes no código;
Teste seu código atendendo as seguintes exigências:
G. Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu
nome e sobrenome;
H. Deve-se apresentar na saída de console um pedido recebendo desconto (valor total
sem desconto maior ou igual a 2500); """


def valida_valores(): # FUNCAO PARA VALIDAR OS CAMPOS DE QUANTIDADE E VALOR
  while True:
    try:
      valor = int(input("Insira o valor da unidade: "))
    except ValueError:
      print("Insira um valor valido!")
      continue
    return valor


print("Bem-vindo a Loja do Luan Holanda")

valor_unitario = valida_valores()
qtd = valida_valores()

valor_total = valor_unitario * qtd

if valor_total < 2500:
  desconto = valor_total * 0 / 100 # CALCULO DA PORCENTAGEM DO DESCONTO
  valor_desconto = valor_total - desconto
  print(f'Valor total a pagar R${valor_desconto:.2f}')

elif 2500 <= valor_total < 6000: #valor_total >= 2500 and valor_total < 6000 equivalente
  desconto = valor_total * 4 / 100
  valor_desconto = valor_total - desconto
  print(f'Valor total de R${valor_total:.2f} com desconto aplicado de 4% (R${desconto:.2f}). Total a pagar com desconto R${valor_desconto:.2f}')
  
elif 6000 <= valor_total < 10000:
  desconto = valor_total * 7 / 100
  valor_desconto = valor_total - desconto
  print(f'Valor total de R${valor_total:.2f} com desconto aplicado de 7% (R${desconto:.2f}). Total a pagar com desconto R${valor_desconto:.2f}')

else:
  desconto = valor_total * 11 / 100
  valor_desconto = valor_total - desconto
  print(f'Valor total de R${valor_total:.2f} com desconto aplicado de 11% (R${desconto:.2f}). Total a pagar com desconto R${valor_desconto:.2f}')

  

