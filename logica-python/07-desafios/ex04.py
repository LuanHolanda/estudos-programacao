## 🟡 EXERCÍCIO 4 – CADASTRO DE PESSOAS
# Crie um programa que:
# * Solicite o nome e idade de várias pessoas
# * O programa deve parar quando o usuário digitar "sair"
# Ao final mostrar:
# * Quantidade de pessoas cadastradas
# * Média de idade
# * Quantas pessoas têm 18 anos ou mais
# * Nome da pessoa mais velha
print("Cadastro de pessoas. Insira nome e idade")
pessoas = []

while True:
  nome = input("Nome: ")
  idade = input("Idade: ")
  if not idade.isdigit():
    print("Idade invalida")
    continue
  else:
    idade = int(idade)
  if idade <= 0:
    print("Idade invalida")
    continue
  saida = input("Deseja sair: ")
  if saida.strip().lower() == "sim":
    break
  break

