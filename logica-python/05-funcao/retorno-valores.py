# Retorno de valors em funcoes
#Funcao x Procedimento
#procedimento(procedure) - uma rotina sem retorno
# Funcao = uma rotina que retorna um dado a quem a invocou


#Retorno de valors em funcoes
def soma3(x = 0, y = 0, z = 0):
  res = x + y + z
  return res

#Programa principal
retornado = soma3(1, 2, 3)
print(retornado)

#forma alternativa simplificada
print(soma3(2,2))