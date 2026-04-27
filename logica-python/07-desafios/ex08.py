# 🟢 EXERCÍCIO 8 – CONTADOR COM VALIDAÇÃO
# Crie um programa que:

# - Peça um número inteiro positivo
# - Valide usando função (não aceitar negativo ou texto)
# - Mostre todos os números de 1 até esse número

# Exemplo:
# Entrada: 5
# Saída: 1 2 3 4 5

def valida_numero():
    while True:
        try:
            numero = int(input("Numero: "))
            if numero < 0:
                print("Insira um numero maior que 0")
                continue
            return numero
        except ValueError:
            print("Insira um numero inteiro e positivo!")


print("A seguir insira um numero inteiro e positivo. Para sair basta inserir o 0")

while True:
    numero = valida_numero()

    if numero == 0:
        print("Encerrando o programa...")
        break

    print(f"\nO numero que voce inseriu foi {numero} e os numeros de 1 até ele são:")

    for i in range(1, numero + 1):
        print(i)
  