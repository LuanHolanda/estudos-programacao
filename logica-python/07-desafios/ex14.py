#Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressao para:
#notas = [9,7,7,10,3,9,6,6,2]
#a)Encontrar quantos alunos tiraram nota 7
#b)Alterar a ultima nota para 4

notas = [9,7,7,10,3,9,6,6,2]
notas[-1] = 4
print(f"{notas.count(7)}") #conta quantas notas 7 tem na lista
print(max(notas)) #encontra a maior nota
notas.sort() #ordena as notas
print(notas)

print(sum(notas) / len(notas)) #soma as notas e divide pelo tamanho para achar a media


#outr forma de fazer
# contador = 0
# for nota in notas:
#   if nota == 7:
#     contador += 1
# print(contador)
