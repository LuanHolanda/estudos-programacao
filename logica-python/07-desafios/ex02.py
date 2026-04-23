#EXERCÍCIO 2 – NÚMEROS PARES NO INTERVALO
# Crie um algoritmo que:
# Solicite ao usuário um valor inicial
# Solicite ao usuário um valor final
# O programa deve:
# Mostrar todos os números pares dentro do intervalo (incluindo os limites)
# Informar quantos números pares existem no intervalo
# Calcular e mostrar a média dos números pares

valor_inicial = int(input("Insira o valor inicial: "))
valor_final = int(input("Insira o valor final: "))
numeros_pares = 0
qtd_pares = 0
for i in range(valor_inicial, valor_final + 1):
  if i % 2 == 0:
   print(i)
   numeros_pares += i
   qtd_pares += 1
if qtd_pares > 0:
 media = numeros_pares / qtd_pares
 print(f'A media de pares nesse intervalo é {media}, e a quantidade é {qtd_pares}')
else:
 print("Nao existe numeros pares nesse intervalo!")
