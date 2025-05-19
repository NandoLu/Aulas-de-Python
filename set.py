lista = ["nome", "nome", "nome","nome1"]
conjunto = set()
conjunto = set(lista)

print(conjunto)
print(lista)

conjunto1 = {"dia", "noite","madrugada", "bom dia"}
conjunto2 = {"dia", "noite"}

conjunto.add("Bom dia")
# COMPARAR CONJUNTOS (comparações na documentação)
conjunto1.difference_update(conjunto2)
conjunto1.remove("madrugada") #Dá erro quando não existe
conjunto1.discard("bom dia")
conjunto1.discard("dia")
print(conjunto1)
print(conjunto2)