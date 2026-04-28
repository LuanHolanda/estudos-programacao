# 🟢 EXERCÍCIO 12 – SENHA COM CONFIRMAÇÃO
# Crie um sistema que:
# - Peça uma senha
# - Peça confirmação da senha
# - Só aceita se forem iguais
# Regras:
# - mínimo 6 caracteres
# - validar com função

def registra_senha():
  while True:
  
    senha = input("Password: ")
    if len(senha) > 8:
      print("A senha nao deve ter mais que 8 caracteres!")
      continue
    elif len(senha) < 6:
      print("A senha deve ter pelo menos 6 caracteres!")
      continue
    # verifica se tem pelo menos 1 número
    tem_numero = False
    for i in senha:
      if i.isdigit():
        tem_numero = True
    # verifica se tem maiúscula
    tem_maiuscula = False
    for i in senha:
      if i.isupper():
        tem_maiuscula = True

    # verifica se tem minúscula
    tem_minuscula = False
    for i in senha:
      if i.islower():
        tem_minuscula = True

    # verifica se tem caractere especial
    tem_especial = False
    for i in senha:
      if not i.isalnum():
        tem_especial = True
    #verifica qual parte de erro e mostra pro ususario
    erro = False

    if not tem_numero:
      print("A senha precisa ter pelo menos 1 número")
      erro = True

    if not tem_maiuscula:
      print("A senha precisa ter pelo menos 1 letra maiúscula")
      erro = True

    if not tem_minuscula:
      print("A senha precisa ter pelo menos 1 letra minúscula")
      erro = True

    if not tem_especial:
      print("A senha precisa ter pelo menos 1 caractere especial")
      erro = True

    if erro:
      continue

    confirmacao = input("Confirme a senha: ")

    if senha != confirmacao:
      print("As senhas nao coincidem!")
      continue
    return senha
  
def valida_opcao():
  while True:
    try:
      menu = int(input("Menu: "))
    except ValueError:
      print("Insira um valor valido!")
      continue
    if menu not in (0,1,2) :
      print("Insira um numero entre 1, 2, 0. das opcoes apresentadas.")
      continue
    return menu

senhas = []
while True:
  print("Menu:\n 1-Cadastrar senha \n 2-Efetuar login \n 0-Sair")
  menu = valida_opcao()
  if menu == 1:
    senha = registra_senha()
    senhas.append(senha)
    print("Senha cadastrada com sucesso!")
  elif menu == 2:
    login = input("Login: ")
    if  login not in senhas:
      print("Senha invalida! Tente novamente!")
    else:
      print("Login efetuado com sucesso!")
  elif menu == 0:
    break
  else:
    print("Insira uma das opcoes validas!")