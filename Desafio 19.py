import random
z = str(input("Digite o nome do 1º aluno: "))
x = str(input("Digite o nome do 2º aluno: "))
c = str(input("Digite o nome do 3º aluno: "))
v = str(input("Digite o nome do 4º aluno: "))
a = [z,x,c,v]
p = random.choice(a)
print(f'O aluno sorteado foi {p}.')
