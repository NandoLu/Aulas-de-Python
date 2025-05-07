# lista = ['oi',12,True]
# print(lista)

# lista.append("Teste")

# print(lista)
# print("Ultimo")
# print(lista[-1])
# print(lista[0:3])

# print("FOR")
# for valor in lista:
#     print (valor)

vinhos = ["azul", "vermelho", "amarelo"]
quant = [1,2,3]

vinho_novo = input("Digite o vinho desejado: ")
quant_nova = int(input("Digite a quantidade: "))
vinhos.append(vinho_novo)
quant.append(quant_nova)
print(vinhos)
print(quant)
print(vinhos[1])
print(quant[1])
print("----")
for i in vinhos:
    vinhos[i] = input("Nome novo vinho: ")
    print(vinhos)
