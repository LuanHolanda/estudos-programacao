## 🟠 EXERCÍCIO 6 – CINEMA (VERSÃO COMPLETA)

# Crie um programa que:

# * Solicite idade e quantidade de ingressos
# * O programa deve continuar até o usuário digitar 0 na idade

# Regras de preço:

# * Menor que 3 anos: gratuito
# * Entre 3 e 12 anos: R$15
# * Acima de 12 anos: R$30

# O programa deve:

# * Validar idade (não pode ser negativa)
# * Validar quantidade (deve ser maior que zero)

# Ao final mostrar:

# * Total de pessoas atendidas
# * Total de ingressos vendidos
# * Valor total arrecadado
# * Média de idade
# * Qual faixa etária comprou mais ingressos:

#   * Menores de 3
#   * Entre 3 e 12
#   * Maiores de 12

# ---

print("Bem vindos ao Cinema")
print("Menores de 3 anos ingresso gratuito, entre 3 e 12 anos:R$15, acima de 12:R$30")
print("A seguir insira a idade e quantidade de ingressos.")

soma_idades = 0
total_ingressos = 0
total_arrecadado = 0
total_pessoas = 0

menor_3 = 0
entre_3_12 = 0
maior_12 = 0

while True:
    print("Para fechar o carrinho basta inserir 0 na idade.")
    idade = input("Idade: ")

    if not idade.isdigit():
        print("Idade precisa ser um valor numerico Inteiro e positivo!")
        continue

    idade = int(idade)

    if idade == 0:
        break

    if idade < 0:
        print("Idade não pode ser negativa!")
        continue

    ingresso = input("Quantidade de Ingressos: ")

    if not ingresso.isdigit():
        print("O ingresso tambem deve ser um valor numerico!")
        continue

    ingresso = int(ingresso)

    if ingresso <= 0:
        print("Quantidade precisa ser um numero acima de 0")
        continue

    # CONTADOR DE PESSOAS (corrigido)
    total_pessoas += 1
    soma_idades += idade

    if idade < 3:
        valor = 0
        menor_3 += ingresso
    elif idade <= 12:
        valor = 15 * ingresso
        entre_3_12 += ingresso
    else:
        valor = 30 * ingresso
        maior_12 += ingresso

    total_ingressos += ingresso
    total_arrecadado += valor


print("\n---RESUMO DO PEDIDO---")

print(f"Total de pessoas atendidas: {total_pessoas}")
print(f"Total de ingressos vendidos: {total_ingressos}")

if total_pessoas > 0:
    media = soma_idades / total_pessoas
else:
    media = 0

print(f"Média de idade: {media}")
print(f"Total arrecadado: R${total_arrecadado}")

# COMPARAÇÃO CORRETA
if menor_3 > entre_3_12 and menor_3 > maior_12:
    print("Faixa etária que mais comprou: Menores de 3 anos")
elif entre_3_12 > menor_3 and entre_3_12 > maior_12:
    print("Faixa etária que mais comprou: Entre 3 e 12 anos")
elif maior_12 > menor_3 and maior_12 > entre_3_12:
    print("Faixa etária que mais comprou: Maiores de 12 anos")
else:
    print("Houve empate entre as faixas etárias")