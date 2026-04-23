#Condicional simples
#traduza as afirmacoes a seguir para condicionais em python
#a)Se idade é maior que 60, escreva: "Voce tem direitos aos beneficios"
idade = int(input('Insira sua idade: '))
if idade > 60:
  print("Voce tem direitos aos beneficios")
else:
  print('Voce nao tem direitos aos beneficios')
#b)Se dano é maior que 10 e escudo é igual a 0, escreva: "Voce esta morto!"
dano = float(input('Dano: '))
escudo = float(input('Escudo: '))
if (dano > 10 and escudo == 0):
 print('Voce esta morto!')
#c)Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em true, escreva: "Voce escapou"
regioes = ("norte","sul","leste","oeste")
bussola = input('Em qual regiao voce esta: ')
if bussola in regioes:
  print('Voce escapou!')

else:
  print('Voce foi pego')