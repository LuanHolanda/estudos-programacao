# 🟢 EXERCÍCIO 13 – CONTADOR DE VOGAIS
# Peça uma palavra
# Mostre:
# - Quantas vogais existem
# Exemplo:
# "python" → 1
# "programacao" → 5

vogais = "a", "e", "i", "o", "u"
while True:
  contador = 0
  print("Insira uma palavra e mostrarei quantas vogais ela tem")
  palavra = input("Palavra: ").lower().strip()
  
  for letra in palavra:
    if letra in vogais:
      contador += 1

  print(f"A palavra {palavra} tem {contador} vogais")
  
