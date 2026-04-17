#Condicional composta
#Traduza as afirmacoes a seguir para condicionais em python
#a)Se ano é divisivel por 4, escreva: "Pode ser um ano bissexto". Caso contratrio, escreva: "Definitivamente nao é um ano bissexto"
# ano = int(input('Ano: '))
# if ano % 4 == 0:
#   print('Pode ser um ano bissexto')
# else:
#   print('Definitivamente nao é um ano bissexto')
#b)Se ambas as variaveis booleanas cima e baixo forem true, esvreva: "Decida-se", caso contrario, escreva: "Voce escolheu um caminho!"
direcao1 = input('Qual direcao seguir: ')
direcao2 = input('Insira outra direcao: ')
cima = direcao1 == "cima"
baixo = direcao2 == "baixo"
if cima and baixo:
 print('Decida-se')
else:
  print('Voce escolheu um caminho!')