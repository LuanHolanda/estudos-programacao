## 🟠 EXERCÍCIO 5 – CAIXA ELETRÔNICO
# Crie um programa que:
# * Solicite ao usuário um valor para saque
# * O valor deve ser inteiro e maior que zero
# O programa deve:
# * Informar quantas cédulas serão usadas:
#   * R$100, R$50, R$20, R$10, R$5 e R$1
# Extras:
# * Perguntar se o usuário deseja fazer outro saque
# * Mostrar ao final:
#   * Quantidade de saques realizados
#   * Valor total sacado

print("Caixa Eletrônico")
print("A seguir insira o valor para saque")
print("Cédulas: R$100, R$50, R$20, R$10, R$5 e R$1")

cedulas = (100, 50, 20, 10, 5, 1)

saques = 0
total_sacado = 0

while True:
    saque = input("Valor: ")

    if not saque.isdigit():
        print("Insira um valor numérico!")
        continue

    saque = int(saque)

    if saque <= 0:
        print("O valor precisa ser maior que zero!")
        continue

    valor_original = saque  # guarda o valor do saque

    print("\nCédulas utilizadas:")

    for cedula in cedulas:
        qtd = saque // cedula
        saque = saque % cedula

        if qtd > 0:
            print(f"{qtd} cédulas de R${cedula}")

    saques += 1
    total_sacado += valor_original

    sair = input("\nDeseja realizar outro saque? ")

    if sair.strip().lower() != "sim":
        break

print("\n--- RESUMO FINAL ---")
print(f"Quantidade de saques: {saques}")
print(f"Valor total sacado: R${total_sacado}")