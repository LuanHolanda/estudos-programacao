#Execute as seguintes atribuicoes:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
#Agora, utilizando operadores + e *, crie as saidas a seguir
#a)'ant bat cod'
print(s1 + ' ' +  s2 + ' ' + s3)
#b)'ant ant ant ant ant ant ant ant ant ant'
print((s1 + ' ')*10)
#c) 'ant bat bat cod cod'
print(s1, (s2+' ')*2 + (s3 + ' ')*3 ) 
# print(f"{s1} {(s2 + ' ') * 2}{(s3 + ' ') * 3}") melhor forma
#d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print((s1 + ' ' + s2 + ' ') * 7)
#e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print(((s2*2)+s3 + ' ')*5)