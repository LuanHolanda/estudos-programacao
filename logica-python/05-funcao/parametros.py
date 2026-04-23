#Parametros em funcao
#Definicao
#Parametros: dados recebidos pelas funcoes
#O ato de enviar um dado para uma funcao é chamado de passagem de parametro

#Parametros opcionais
#Podemos dar maior flexibilidade para nossas funcoes permintindo que nem sempre se use todos os parametros na chama da funcao
#vamos ver parametros opcionais em python

# def soma3(x, y, z):
#   res = x + y + z
#   print(res)
def soma3(x = 0, y = 0, z = 0):
  res = x + y + z
  print(res)

soma3(1,2,3)
soma3(1,2) #z foi omitido
soma3(1,3)
soma3()