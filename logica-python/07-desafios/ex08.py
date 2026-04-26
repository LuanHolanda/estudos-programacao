# 🟢 EXERCÍCIO 8 – CONTADOR COM VALIDAÇÃO
# Crie um programa que:

# - Peça um número inteiro positivo
# - Valide usando função (não aceitar negativo ou texto)
# - Mostre todos os números de 1 até esse número

# Exemplo:
# Entrada: 5
# Saída: 1 2 3 4 5

def valida_numero(msg):
  print("Insira um numero Inteiro e positivo")
  numero = input(msg)
  while True:
    if numero <= 0:
      print("numero precisa ser positivo e maior que zero!")
      continue
    elif numero == "":
      print('Precisa ser um valor numerico')
      continue
    elif not int(numero):
      print("Precisa ser um valor inteiro ")