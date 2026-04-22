#Desafio 1 - media com validacao
#peca ao usuario 5 notas
#Regras: nao aceita nota negativa, nao aceita nota maior que 10, se errar pedir denovo
#no final: mostrar media, dizer se foi aprovado (>= 6) ou reprovado

soma_nota = 0
contador = 0
while contador < 5:
 notas = int(input('Em sequencia insira 5 notas: '))
 if notas < 0:
  print("Insira uma nota valida!")
  continue
 elif notas > 10:
  print("Insira uma nota valida!")
  continue
 contador += 1
 soma_nota += notas
media = soma_nota / contador
if media >= 6:
 print(f"Sua média de notas foi {media}, Parabens voce foi aprovado!")
else:
 print(f"Sua média de notas foi {media}, voce foi reprovado!")