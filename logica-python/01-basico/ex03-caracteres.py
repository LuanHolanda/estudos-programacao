#Crie uma variavel de string que receba uma frase qualquer. Crie uma segunda variavel agora contendo a metade da string digitada. Imprima na tela somente os dois ultimos caracteres da segunda variavel do tipo string#
frase = input('Digite uma frase: ')
tam = len(frase)

frase2 = frase[0:int(tam/2)]

print(frase2[-2:])