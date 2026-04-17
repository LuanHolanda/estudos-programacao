#Faca um algoritmo que recebe tres valores, repesentando os lados de um triangulo fornecidos pelo usuario. verifique se os valores formam um triangulo e classifique como
#a) Equilatero(tres lados iguais)
#b) Isosceles (dois lados iguais)
#c) Escaleno (tres lados diferentes)
valor1 = int(input('Insira o valor de um lado: '))
valor2 = int(input('Insira o valor de outro lado: '))
valor3 = int(input('Insira o valor de mais um lado: '))
if(valor1 == 0 or valor2 == 0 or valor3 == 0):
  print('Nenhum dos lados pode ser igual a zero!')
elif (valor1 + valor2 <= valor3 or valor1 + valor3 <= valor2 or valor2 + valor3 <= valor1):
  print('Um lado nao pode ser maior do que a soma dos dois lados')
elif (valor1 == valor2 == valor3):
  print("Este triangulo é Equilatero")
elif (valor1 == valor2 or valor1 == valor3 or valor2 == valor3):
 print('Este triangulo é Isosceles')
else:
  print('Este triangulo é Escaleno com todos lados diferentes')

  #Professor fez de outra forma 
  # if (A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and C + B > A):