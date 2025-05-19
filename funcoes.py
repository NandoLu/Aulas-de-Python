# def SomaDois(n):
#     resultado = 2 + n
#     print(resultado)
#     return resultado

# def par_ou_impar():
#     if 2 % 2 == 0:
#         return("Par")
#     else:
#         return("Ímpar")

# def calcular_area(base, altura):
#     area = (base * altura) / 2
#     print(f"Área do triângulo: {area}")

# base = float(input('Informe a base: '))
# altura = float(input('Informe a altura: '))

# calcular_area(base, altura)

# a = 5
# b = 6

# def exibir (a,b):
#     a = 10
#     b = 20
#     # print(a, '\n', b)
#     return(a, b)
# print("Exibir ---- ")
# exibir(a, b)
# print(exibir(a,b))
# # print(a, "-", b)

# print("Exercicio 5 ---------")

# raio = float(input("Digite o raio: "))

# def area(raio):
#     a = 3.14 * (raio*raio)
#     return(f"A aultura é: {a}")

# def perimetro(raio):
#     p = 3.14 * 2 * raio
#     return(f"O perímetro é: {p}")

# # a = area(raio)
# # p = perimetro(raio)
# # print(a)
# # print(p)

# print("No print")

# print(area(raio))
# print(perimetro(raio))

# # print("\n Calculando velocidade média ------- \n")
# print("\n Calculando velocidade média ------- \n")

# # def calcular_velocidade_media(distancia, tempo):
# def calcular_velocidade_media(distancia: float, tempo: float, unidade_medida="km/h"):
#     velocidade_media = distancia / tempo
#     print(f"A velocidade média é: {velocidade_media} {unidade_medida}")

# distancia = int(input("Digite a distância: "))
# tempo = int(input("Digite o tempo: "))
# calcular_velocidade_media(distancia, tempo)
# calcular_velocidade_media(distancia, tempo, "m/s")

# # Funções com argumentos e sem argumentos
# # Uma função não precisa de argumentos quando ela trabalha com valores pré existentes
# # Argumentos variáveis
# def exibe_promocao(*clientes):
#     for cliente in clientes:
#         print(f"Olá, {cliente} \n Queremos avisar que temos promoção!")

# lista_clientes = ["Bob", "Roger", "Claudio", "Michele"]
# exibe_promocao(*lista_clientes)
# exibe_promocao("Joao")
# exibe_promocao("Mateus", "Lucas", "Marcos", "Joao")

print("-----KEYWORD ARGS------")

def exibe_ficha(**dados):
    print("----FICHA----")
    for chave, valor in dados.items():
        print(f"{chave}- {valor}")

exibe_ficha(nome = "Luiz", estado_civil = "Casado")

ficha_cliente = {
    "nome": "Dino",
    "idade": 7,
    "filhos": True,
}

exibe_ficha(**ficha_cliente)

print("---------RETURN-----")

def soma(a,b):
    resultado = a + b

    return resultado

valor1 = int(input("Digite o valor"))
valor2 = int(input("Digite o valor"))

soma(valor1, valor2)
resposta = soma(valor1, valor2)
print(f"A resposta é: {resposta}")
print(f"A resposta é: {soma(valor1, valor2)}")