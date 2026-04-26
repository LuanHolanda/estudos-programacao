#Suponha que voce é um colecionador de jogos de videogame. Escreva um algoritmo que permita cadastrar esses jogos informando o nome qual videogame ele pertence
#Para isso, crie um menu de opcoes contendo: cadastrar novo item, listar tudo que foi cadastrado e sair

def valida_texto(msg):
    while True:
        texto = input(msg).strip()

        if texto == "":
            print("Não pode ser vazio!")
            continue

        return texto

def valida_opcao():
    while True:
        print("1 - Cadastrar")
        print("2 - Listar")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao in ["1", "2", "0"]:
            return opcao

        print("Opção inválida!")


jogos = []

while True:
  print("Menu de Opcoes")
  print("Para cadastrar jogo e console digite 1, para listar o que foi cadastrado 2 e para sair 0")
  opcao = valida_opcao()
  if opcao == "1":
    nome = valida_texto("Nome do jogo: ")
    console = valida_texto("Nome do console: ")
    jogos.append({
      "nome": nome,
      "console": console
    })
  elif opcao == "2":
    if not jogos:
      print("Nenhum jogo cadastrado")
    else:
      for jogo in jogos:
        print(f"| Nome: {jogo['nome']} | Console: {jogo['console']} |")
  elif opcao == "0":
    print("Encerrando programa...")
    break