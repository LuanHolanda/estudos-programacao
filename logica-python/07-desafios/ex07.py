## 🔴 EXERCÍCIO 7 – LOGIN COM TENTATIVAS
# Crie um sistema de login com:
# * Usuário e senha fixos (definidos no código)
# Regras:
# * Permitir no máximo 3 tentativas
# * Se errar 3 vezes:
#  * Exibir mensagem de bloqueio
# * Se acertar:
#   * Exibir mensagem de sucesso

def valida_login(msg):
    while True:
        login = input(msg).strip()

        if login == "":
            print("Login não pode ser vazio!")
            continue

        if len(login) < 3 or len(login) > 12:
            print("Login deve ter entre 3 e 12 caracteres!")
            continue

        if not login.isalpha():
            print("Login deve conter apenas letras!")
            continue

        return login


def valida_senha(msg):
    while True:
        senha = input(msg).strip()

        if senha == "":
            print("Senha não pode ser vazia!")
            continue

        if len(senha) < 6:
            print("Senha deve ter no mínimo 6 caracteres!")
            continue

        return senha


# Dados fixos
login_correto = "luan"
senha_correta = "123456"

tentativas = 0

while tentativas < 3:
    login = valida_login("Login: ")
    senha = valida_senha("Senha: ")

    if login == login_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        print(f"Login ou senha incorretos! Tentativas: {tentativas}/3")

if tentativas == 3:
    print("Acesso bloqueado!")

