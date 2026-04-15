# Um aluno, para passar de ano, precisa ser aprovado em todas as materias que esta cursando
# Assuma que a media para aprovacao é a partir de 7 e que o aluno cursa 3 materias, somente. Escreva um algoritmo que leia a nota final do aluno em cada materia e informe, na tela, se ele passou de ano ou nao

nota1 = float(input('Qual sua nota final em Matematica: '))
nota2 = float(input('Qual sua nota final em Biologia: '))
nota3 = float(input('Qual sua nota final em Portugues: '))


if nota1 >= 7 and nota2 >= 7 and nota3 >= 7:
  print('Nota mínima por matéria é 7. Parabens voce foi aprovado')
else: 
  print('Voce nao atingiu a media necessaria em pelo menos uma materia, reprovado!')