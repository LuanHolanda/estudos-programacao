# 🟢 EXERCÍCIO 9 – SOMA DE NÚMEROS
# Crie um programa que:
# - Peça números ao usuário
# - Continue até digitar 0
# - Mostre:
#   - Soma total
#   - Quantidade de números digitados
#   - Média

soma = 0
numeros = []

def valida_numero():
  while True:
    try:
      numero = int(input("Numero: "))
    except:
      print("Insira um numero valido!")
      continue
    return numero
  
print("A seguir insira quantos numeros desejar, ao final sera feito a soma dos numeros e quais eles sao. para sair basta digitar 0")
while True:
  numero = valida_numero()
  if numero == 0:
    print("Encerrando o programa...")
    break
  soma += numero
  numeros.append(numero)
  continue
quantidade = len(numeros)
if quantidade > 0:
  media = soma / quantidade
  print(media)
else:
  print("nao ha numeros")


print(quantidade)
print(soma)
print(numeros)


