#Escreva um algoritmo em python que calcule a tabuada de todos os numeros de 1 ate 10, e, para cada numero, vamos calcular a tabuada multiplicando- o pelo intervalo de 1 até 10
numero = 0
multiplicador = 1

while (multiplicador <= 10):
  for i in range (1, 11):
    numero = i * multiplicador
    print(f'{multiplicador}x{i} = {numero}')
  multiplicador += 1


#Esse é um padrão MUITO importante

# Sempre que usar loop, pensa assim:

# 1. O que muda a cada repetição?

# 👉 (variável de controle)

# 2. O que deve acontecer dentro?

# 👉 (cálculo)

# 3. Quando mostrar o resultado?

# 👉 (print no lugar certo)

# Forma do professor
# 2x while
# tabuada = 1
# while tabuada <= 10:
#   print(f'TABUADA DO {tabuada}')
#   i = 1
#   while i <= 10:
#     print(f'{tabuada} x {i} = {tabuada * i}')
#   tabuada += 1

#2x for
# for tabuada in range (1, 11, 1):
#   print(f'TABUADA DO {tabuada}:')
#   for i in range(1, 11, 1):
#     print(f'{tabuada} x {i} = {tabuada * i} ')

#while + for
# tabuada = 1
# while tabuada <= 10:
#   print(f'TABUADA DO {tabuada}:')
#   for i in range (1, 11, 1):
#     print(f'{tabuada} x {i} = {tabuada * i}')
#   tabuada += 1