# Use função para validar entrada
# 🟢 EXERCÍCIO 10 – LISTA DE NOMES
# Crie um sistema que:
# - Permita cadastrar nomes
# - Use lista
# - Menu:
#   1 - Cadastrar nome
#   2 - Listar nomes
#   0 - Sair
# Regras:
# - Nome não pode ser vazio
# - Mostrar mensagem se lista estiver vazia

def valida_nomes():
  while True:
    nome = input("Cadastrar Nome: ").strip()

    if nome == "":
      print("Nao pode ser vazio!")
      continue

    if not nome.replace(" ", "").isalpha(): # isalpha() verifica se a string tem APENAS letras #replace() troca um pedaço da string por outro
      print("Digite apenas letras!")
      continue

    if len(nome) < 3:
      print("Muito curto!")
      continue
    return nome
  
def valida_menu():
  while True:
    try:
      menu = int(input("Opcao: "))
    except ValueError:
      print("Insira um numero entre 1, 2, 0. das opcoes apresentadas.")
      continue
    if menu not in (0,1,2) :
      print("Insira um numero entre 1, 2, 0. das opcoes apresentadas.")
      continue
    return menu

print("Cadastro de Nomes")
nomes = []

while True:
  print("Menu:\n 1 - Cadastrar nome \n 2 - Listar nomes \n 0 - Sair")
  opcoes = valida_menu()
  
  if opcoes == 1:
      nome = valida_nomes()
      nomes.append(nome)
  
  elif opcoes == 2:
        if not nomes:
            print("Nenhum nome cadastrado")
        else:
            for nome in nomes:
                print(f"- {nome}")

  elif opcoes == 0:
    break

