# 🟢 EXERCÍCIO 11 – MAIOR E MENOR
# Peça vários números até digitar 0
# Mostre:
# - Maior número
# - Menor número
# Use função para validar número

def valida_numero():
  while True:
    try:
      numero = float(input("Numero: "))
    except ValueError:
      print("Insira um numero valido!")
      continue

    return numero


print("A seguir insira quantos numeros desejar e sera mostrado o menor valor e o maior.")
numeros = []
print("Para sair basta digitar 0")
while True:
  numero = valida_numero()
  if numero == 0:
    print("Encerrando o Programa...")
    break
  numeros.append(numero)

if numeros:
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
else:
    print("Nenhum número foi digitado")