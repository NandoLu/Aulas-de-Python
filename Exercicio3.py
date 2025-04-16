# Luiz Fernando Balbino
# RM 566222

print("CARDÁPIO: \n 100 Cachorro quente: 13.20 \n 101 Hamburguer: 19.90 \n 102 Cheeseburguer: 21.90 \n 103 Suco Natural: 7.00 \n 104 Refrigerante: 6.50")
produto = int(input("\n Digite o codigo do produto: "))
quantidade = int(input("Digite a quantidade: "))

cachorro = 13.2
hamburguer = 19.9
cheese = 21.9
suco = 7.0
refrigerante = 6.5

if produto == 100:
    print(f"Preço final: {quantidade * cachorro}")
elif produto == 101:
    print(f"Preço final: {quantidade * hamburguer}")
elif produto == 102:
    print(f"Preço final: {quantidade * cheese}")
elif produto == 103:
    print(f"Preço final: {quantidade * suco}")
elif produto == 104:
    print(f"Preço final: {quantidade * refrigerante}")
else:
    print("Código de produto inválido!")