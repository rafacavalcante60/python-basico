import random
z = str(input("Digite o nome do 1º aluno: "))
x = str(input("Digite o nome do 2º aluno: "))
c = str(input("Digite o nome do 3º aluno: "))
v = str(input("Digite o nome do 4º aluno: "))
a = [z,x,c,v]
random.shuffle(a)
print(f'A ordem sorteada foi {a}.')
