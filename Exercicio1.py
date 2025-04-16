# Luiz Fernando Balbino
# RM 566222

valor = float(input("Digite o valor da compra: "))
estado = input("Estados: \n MG, SP \n RJ, MS \n Digite o estado: ")
mg = 0.07
sp = 0.12
rj = 0.15
ms = 0.08
estado = estado.upper()

if estado == "MG":
    print(f"Preço final para MG: {(valor * mg)+valor}")
elif estado == "SP":
    print(f"Preço final para SP: {(valor * sp)+valor}")
elif estado == "RJ":
    print(f"Preço final para RJ: {(valor * rj) + valor}")
elif estado == "MS":
    print(f"Preço final para MS: {(valor * ms)+valor}")
else:
    print("Estado inválido!")




