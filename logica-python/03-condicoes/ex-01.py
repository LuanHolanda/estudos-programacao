#Desenvolva um programa que leia dois valores numericos inteiros e compare se o primeiro é maior do que o segundo, utilizando uma condicional simples#
#Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado é mauor do que o segundo# 

first_number = int(input('Insira um valor inteiro: '))
second_number = int(input('Insira outro valor inteiro: '))

if first_number > second_number :
  print(f'O primeiro valor {first_number} é maior que o segundo valor {second_number}')

elif first_number == second_number :
 print(f'O valor {first_number} é igual ao valor {second_number}')

else: 
#  first_number < second_number
 print(f'O segundo valor {second_number} é maior que o primeiro valor {first_number}')

 #Erro no else: O else não aceita uma condição (como first_number < second_number). Ele é o "caso contrário" automático. Deves apagar essa linha ou transformá-la num comentário.
#Condicional Simples: No enunciado, pedem uma "condicional simples" para verificar se o primeiro é maior. O uso de elif e else torna a condicional composta/encadeada. Se for para um exercício rigoroso, foca-te apenas no if.
# nao seria necesseraio atribuir uma condicao ao else, se nenhuma das outras condicoes forem aplicadas ele fica automatico
# A condicional do tipo simples seria so com o if, como pede o enunicado ja a do tipo composta como fiz no exercicio utiliza do elif e else