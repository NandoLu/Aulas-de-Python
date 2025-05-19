# importação
from collections import defaultdict
# defaultdict capaz de criar uma chave inexistente
dicionario_lista = defaultdict(list) 
dicionario_lista["PRODUTO"] = "Macbook Pro"
dicionario_lista["MARCA"] = "Apple"

print(dicionario_lista["PREÇO"]) 
print(dicionario_lista)
# Campo preço será vazio

def funcao_exemplo():
    return "INEXISTENTE"

print(funcao_exemplo())

dicionario_funcao = defaultdict(funcao_exemplo) 
dicionario_funcao["PRODUTO"] = "Macbook Pro"
dicionario_funcao["MARCA"] = "Apple"

print(dicionario_funcao)
print(dicionario_funcao["PREÇO"])
print(dicionario_funcao)

# lambda cria um valor padrão para uma chave não existente automáticamente
dicionario_lambda = defaultdict(lambda: "Não disponível") 
dicionario_lambda["PRODUTO"] = "Macbook Pro"
dicionario_lambda["MARCA"] = "Apple"

lista = ["Python", "Cobol", "Java", "JavaScript", "C++", "C"]
print(f"Lista de linguagens: \n {lista}")

mapa = map(len, lista)
print(mapa)
mapa = list(map(len, lista))
print(mapa)
