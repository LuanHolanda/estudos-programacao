# Escopo de variaveis
def omelete():
 ovos = 12 #variavel local

#Programa Principal
# omelete()
# print(ovos) #escopo global #isso retorna erro pois a variavel ovos esta dentro da funcao omelete e so pode ser acessada ao chamarmos a funcao

def omelete():
 print(ovos) #escopo local

#Programa Principal
ovos = 12 #variavel global
omelete()  #Aqui ja funciona pois uma variavel global pode ser acessada atraves do escopo de uma funcao local


# Problema de usar variável global assim
# def omelete():
#     print(ovos)

# 👉 a função depende de algo externo

# Isso gera:

# código menos previsível
# mais difícil de testar
# mais difícil de reutilizar

# 💡 Forma mais correta (profissional)

# Passe o valor como parâmetro:

# def omelete(ovos):
#     print(ovos)

# ovos = 12
# omelete(ovos)
# 🧠 Agora sim:
# função é independente

# 👉 isso é MUITO mais forte

# 💪 Exemplo pra fixar de vez
# def omelete(ovos):
#     print(f"Omelete com {ovos} ovos")

# omelete(2)
# omelete(5)
# omelete(10)

# 👉 mesma função → vários usos

def omelete(): 
 ovos = 12 #cada função tem seu próprio escopo a variável ovos dentro de omelete é diferente da de bacon
 bacon()
 print(ovos)

def bacon():
 ovos = 6