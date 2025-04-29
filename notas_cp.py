# Cadastro de Aluno:

nome = input("Digite o nome do aluno:")
rm = int(input("Digite o RM do aluno:"))
senha = int(input("Digite a senha do aluno:"))
senhav = int(input("Digite a senha novamente:"))
while senhav != senha:
    senhav = int(input("Senha não coincide, digite novamente:"))

print("--- Aluno cadastrado! ---")
print("--- Boletim ---")

rmlog = int(input("Digite o RM do aluno:"))
while rmlog != rm:
    rmlog = int(input("RM não encontrado, digite novamente:"))

senhalog = int(input("Digite a senha do aluno:"))

cont = 0
if senhalog != senha:
    while cont < 3:
        senhalog = int(input("Senha errada, digite novamente!"))
        if senhalog == senha:
            print("Acesso permitido!")
            break
        else:
            cont+=1
            print(f"Senha errada, {3 - cont} tentativas restante!")
    if cont == 3:
        print("Numero de tentativas esgotado!")
    
cp1 = float(input("Digite o valor do Checkpoint 1: "))
while cp1 < 0 or cp1 > 10:
    cp1 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))
cp2 = float(input("Digite o valor do Checkpoint 2: "))
while cp2 < 0 or cp2 > 10:
    cp2 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))
cp3 = float(input("Digite o valor do Checkpoint 3: "))
while cp3 < 0 or cp3 > 10:
    cp3 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))

cps = 0
if cp1 < cp2 and cp1 < 3:
    cps = cp2 + cp3
elif cp2 < cp1 and cp2 < cp3:
    cps = cp1 + cp3
else:
    cps = cp1 + cp2

sprint1 = float(input("Digite o sprint 1: "))
while sprint1 < 0 or sprint1 > 10:
    sprint1 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))

sprint2 = float(input("Digite o sprint 2: "))
while sprint2 < 0 or sprint2 > 10:
    sprint2 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))

resultado = ((sprint1 + sprint2 + cps)/4)*0.4
resultado = ((6 - resultado)*10)/6
print(f"A nota necessária para passar é {resultado:.2f}") 
