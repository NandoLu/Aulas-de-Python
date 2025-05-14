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

print("Exercicio 5 ---------")

raio = float(input("Digite o raio: "))

def area(raio):
    a = 3.14 * (raio*raio)
    return(f"A aultura é: {a}")

def perimetro(raio):
    p = 3.14 * 2 * raio
    return(f"O perímetro é: {p}")




# a = area(raio)
# p = perimetro(raio)
# print(a)
# print(p)

print("No print")

print(area(raio))
print(perimetro(raio))
