vinhos = ["Luara Tempranillo", 2, "Vinho1", 20]

def BoasVindas():
    print("---"*5)
    print("Seja Bem Vindo!")
    print("---"*5)

def cadastrar_vinho():
    nome = input("Digite o nome do vinho: ")
    quantidade = int(input("Digite a quantidade: "))
    vinhos.append(nome)
    vinhos.append(quantidade)

def menu():
    print("MENU:")
    for i in range(0, len(vinhos), 2 ):
        print(vinhos[i], "----",vinhos[i+1])

print(vinhos[0]) 
system = True
BoasVindas()
menu()
while system == True:
    print("opções: sair (digite 0)  cadastrar (digite 1)")
    opcao = int(input("sua opcao: "))
    match opcao:
        case 0:
            menu()
            print("Obrigado por usar nosso sistema!")
            system = False
        case _:
            cadastrar_vinho()
            system = True