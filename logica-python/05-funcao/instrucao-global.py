# A instrucao global

#Forca nosso programa a nao criar uma variavel local de mesmo nome e manipular somente a global dentro de uma funcao

def omelete():
  global ovos
  ovos = 6

#programa principal
ovos = 12
omelete()
print(ovos)