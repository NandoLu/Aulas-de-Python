from collections import OrderedDict

dicionario_ordenado = OrderedDict()
print(dicionario_ordenado)

# Adicionando chaves e valores
dicionario_ordenado["NOME"] = "Iphone"
dicionario_ordenado["MARCA"] = "Apple"
dicionario_ordenado["MODELO"] = "14 pro max"

for chave, dado in dicionario_ordenado.items():
    print(f"{chave} -> {dado}")

# Alerando um item
dicionario_ordenado["MARCA"] = "Maça"

for chave, dado in dicionario_ordenado.items():
    print(f"{chave} -> {dado}")

# remover elemento
dicionario_ordenado.pop("MARCA")
print()
for chave, dado in dicionario_ordenado.items():
    print(f"{chave} -> {dado}")

# reincerir
dicionario_ordenado["MARCA"] = "Apple"
for chave, dado in dicionario_ordenado.items():
    print(f"{chave} -> {dado}")