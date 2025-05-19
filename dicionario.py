dicionario = {}
print(type(dicionario))
dicionario = {
    "nome": "Poderoso Chefão",
    "diretor": "Lucas Filme",
    "ano de lançamento": 2005,
    "bilheteria": "R$2.500,97"
}

print(dicionario)
print(dicionario["nome"])
print(dicionario["nome"])

# Inserção de uma chave e valor no dicionário
dicionario["gênero"] = "ação"
print(dicionario)

# Retornar todos as chaves do dicionário
# Estrutura iterável, pode ser utilizada num loop for 
print(dicionario.keys())
print(dicionario.values())

for chave in dicionario.keys():
    print(chave)
for chave in dicionario.values():
    print(chave)

# Retornar chaves e valores - formato "lista de tuplas"
# por ser uma lista de tuplas - pode ser "desempacotado"
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")


# Método get (exibir chaves que não existe)
# print(dicionario["público"]) #erro
print(dicionario.get("público"))
print(dicionario.get("nome"))

# Método setdefault: Inserir 
dicionario.setdefault("público", 1000)
dicionario.setdefault("público", 9000) #não altera quando já existe
print(dicionario)

op = 0
ficha = {
    "nome": "Luiz",
}
while op != 4:
    print("MENU")
    op = int(input("Informe a opção desejada: "))
    match op:
        case 1:
            chave = input("Informe o campo que deseja cadastrar na ficha: ")
            valor = input("Informe o dado que deseja cadastrar no campo: ")
            # ficha[chave] = valor
            ficha.update({chave:valor})
            print(ficha)
        case 2:
            print(f"Os campos disponíveis são: {ficha.keys}")
            chave = input("Informe qual campo deseja exibir: ")
            # print(ficha.get(chave))
            if chave in ficha.keys():
                print(f"O campo: {chave} contém o dado: {ficha.get(chave)}")
            else:
                print("Você digitou um campo inexistente")
        case 3:
            print("FICHA CADASTRAL")
            for campo, dado in ficha.items():
                print(f"{campo.upper()} --> {dado}")
        case 4:
            print("Saindo do sistema")
            break
        case _:
            print("Escolha um opção válida")