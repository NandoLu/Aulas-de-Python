# cont = 0
# limite = int(input("Digite até que número voce deseja:"))
# while cont < limite:
   


#     cont+=1
#     print(cont)

# print("Acabou, mané")

# import os
# os.system('cls' if os.name == 'nt' else 'clear')

# par = 0
# cont = 0
# while cont < 10:
#     num = int(input("Digite o número voce deseja:"))
#     if num%2 == 0:
#         par+=1
#     cont += 1

# print("Acabou, mané")
# print(f"Voce digitou {par} numeros pares")

# ------------ MEDIA


# import os

# media = float(input("Digite a media: "))
# while media < 0 or media > 10:
#     os.system('cls')
#     print("Media errada, digite novamente")
#     media = float(input("Digite a media: "))

# if media < 6:
#     print("Reprovado")
# elif media >= 6 and media <= 7:
#     print("Aprovado, mas pode melhorar!")
# else:
#     print("Aprovado, muito bem!")

# ------------ MEDIA

# x = 0
# y = 0

# while x < 10:
#     x+=1
#     y+=x
# print(f"Somatório dos números é {y}")

# ------------ TABUADA

# x = 0
# y = int(input("A tabuada:"))
# while x <= 10:
#     print(f"{y} x {x} = {x*y}")
#     x+=1

# -------------- DESAFIO

# Luiz Fernando Balbino
# RM 566222
import os
print("CARDÁPIO: \n 100 Cachorro quente: 13.20 \n 101 Hamburguer: 19.90 \n 102 Cheeseburguer: 21.90 \n 103 Suco Natural: 7.00 \n 104 Refrigerante: 6.50 \n 105 Terminar Compra")


cachorro = 13.2
hamburguer = 19.9
cheese = 21.9
suco = 7.0
refrigerante = 6.5
sistema = True
total = 0


while sistema == True :
    os.system('cls')

    print("CARDÁPIO: \n 100 Cachorro quente: 13.20 \n 101 Hamburguer: 19.90 \n 102 Cheeseburguer: 21.90 \n 103 Suco Natural: 7.00 \n 104 Refrigerante: 6.50 \n 105 Terminar Compra")

    produto = int(input("\n Digite o codigo do produto: "))
    
    
    match produto:
        case 100:
            quantidade = int(input("Digite a quantidade: "))
            total = total + cachorro * quantidade
        case 101:
            quantidade = int(input("Digite a quantidade: "))
            total = total + quantidade * hamburguer
        case 102:
            quantidade = int(input("Digite a quantidade: "))
            total = total + quantidade * cheese
        case 103:
            quantidade = int(input("Digite a quantidade: "))
            total = total + quantidade * suco
        case 104:
            quantidade = int(input("Digite a quantidade: "))
            total = total + quantidade * refrigerante
        case 105:
            print(f"O valor total é: {total:.2f}")
            sistema = False
        case _:
            print("Codigo inválido!")