#Escreva uma funcao que calcule o fatorial de um numero recebido como parametro e retorne o seu resultado
#faca uma validacao dos dados por meio de outra funcao, permitindo que somente valores positivos sejam aceitos
#crie o help da sua funcao

def ler_numero():
  while True:
    try:
      number = int(input("Insira um numero para calcularmos seu fatorial: "))
    except ValueError:
      print("Digite um número válido!")
      continue

    if number <= 0:
      print("Insira um numero positivo e maior que zero!")
      continue

    return number

def fatorial(number):
  """
  Calcula o fatorial de um número inteiro positivo.

  Parâmetro:
  number (int): número positivo

  Retorno:
  int: valor do fatorial
  """
     
  resultado = 1
  for i in range(1, number + 1):
    resultado *= i
  return resultado

numero = ler_numero()
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")