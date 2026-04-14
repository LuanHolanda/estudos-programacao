#Exercício 2.4: desenvolva um algoritmo que converta uma temperatura
#de Celsius (C) em Fahrenheit (F). A equação de conversão é:
 # 𝐹 = 9 × 𝐶 + 32
 #       5

temperatura = float(input('Digite uma temperatura: '))
conversao = (temperatura * 9 / 5) + 32
print(f'A temperatura em Fahrenheit é: {conversao:.2f}')