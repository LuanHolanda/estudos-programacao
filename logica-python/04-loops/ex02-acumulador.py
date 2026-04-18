# Escreva um algoritmo que calcule a sua media de notas em determinada disciplina
# Vamos assumir que a media final é dada pela média aritmetica de cinco notas digitadas

contador = 1
soma = 0
quantidade = 5
while (contador <= quantidade):
  nota = int(input('Insira uma nota: '))
  soma = soma + nota
  contador = contador + 1
media = soma / quantidade
if media <= 6:
  print(f'Sua media nesta materia foi {media} voce reprovou!')
elif media > 6:
  print(f'Sua media foi {media}. Parabens voce passou na materia!')
