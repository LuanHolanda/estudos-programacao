# Estrutura de repeticao for(para)
# for i in range(6):
#   print(i)

# com tres parametros 0 sendo o valor inicial, 6 o valor final, e 1 o passo do iterador
# for i in range (0 , 6, 1):
#   print(i)

#Varredura de string com for
# frase = "Logica de programacao e algoritmos"
# for i in range(0, len(frase), 1):
#   print(frase[i], end = "")

#Comparativo while e for
# x = 1               
# while (x < 6):    for i in range(1,6,1):
#   print(x)          print(i)
#   x = x + 1

#Exercicio escreva um algrotimo que calcule a media dos numeros pares de 1 até 100(1 e 100 inlcusos).Implemente o laco usando for
soma = 0
contador = 0
for i in range(1,101):
  if i % 2 == 0:
   contador += 1
   soma += i
print(f'A quantidade de numeros pares do 1 ao 100 é {contador} e a media deles é {soma / contador}')
