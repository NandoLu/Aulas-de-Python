x = 10
y = 5

dias_letivos = 10
carga_horaria = 10

limite_faltas = (dias_letivos*carga_horaria) / 4


mediaf = float(input("Media final do aluno: "))
faltas = int(input("Numero de falta: "))
if (mediaf >= 6 and faltas < 15):
    print("aprovado")
else:
    print("reprovado")


print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

idade = int(input("Sua idade: "))
print(f"Maior de idade: {idade >= 18}" )
print(f"Você é doador: {idade >=16 and idade <=69}")

