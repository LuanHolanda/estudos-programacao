#Estrutura de repeticao while(enquanto)
#Repete um bloco de instrucoes enquanto determinada condicao se mantiver verdadeira
#Caso contrario, ocorre o desvio para a primeira linha de codigo apos este bloco de repeticao

#    Python
#   while ( x>y ):
# x = 1
# while (x <= 100):
#   print(x)
#   x = x + 3 

#Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo usuario e que sejam numeros pares

inicial = int(input('Digite um valor inicial: '))
final = int(input('Digite o valor final: '))

x = inicial
while (x <= final):
  if (x % 2 == 0):
    print(x)
  x = x + 1