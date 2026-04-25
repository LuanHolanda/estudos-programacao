# Exemplo simples
# def calcular_preco(idade, quantidade):
#     if idade < 3:
#         return 0
#     elif idade <= 12:
#         return 15 * quantidade
#     else:
#         return 30 * quantidade

# valor = calcular_preco(idade, ingressos)

# calcular o valor por idade / deixa o codigo mais limpo e organizado. podendo ultilizar a funcao novamente em outra ocasiao no mesmo projeto

def omelete():
  ovos = 12 #variavel local de omelete
  print('Ovos = ', ovos)

def bacon():
  ovos = 6 #variavel local de bacon
  print('Ovos = ', ovos)
  omelete()
  print('Ovos = ', ovos)

#Programa principal
ovos = 2 #variavel global
bacon()
print('Ovos = ', ovos)

# bacon começa
# ↓
# imprime 6
# ↓
# chama omelete
#    ↓
#    imprime 12  ← AQUI aparece o 12
#    ↓
# volta pra bacon
# ↓
# imprime 6 de novo
# ↓
# volta pro principal
# ↓
# imprime 2

