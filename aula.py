# Lista sobre operadores artiméticos
x=10; a=5;b=2; c=9; d=20

print("Ex_1: ",x + a / b)
print("Ex_2: ",x + a // b)
print("Ex_3: ",(x + a ) % b)
print("Ex_4: ",d - d * a + c )
print("Ex_5: ",2 * b % 9 + 7)
print("Ex_6: ",d - b *( a + c ))
print("Ex_7: ",(d - b ) * (a + c))
print("Ex_8: ",x + d % b + a * c * b - a)
print("Ex_9: ",((x + d) // b)+(a *(c + b - a)))


# Desafio de distancia percorrida
distancia = int(input("Digite a distancia: "))
print(f"A distancia percorrida de \n Km corresponde a {distancia*1000} metros")

# Comandos de entrada e saída em Python 
a = input("Digite um numero: ")
b = input("Digite um numero: ")
print (a+b)
a = int

# Valor booleano

# booleano = bool(int(input("Digite um número: ")))
booleano = input("É verdade? ").strip().lower() == "sim"
print(booleano)

# Exercicio com nome

nome = input("Digite o nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f" Olá, {nome}! \n Você tem {idade} anos \n Sua altura e {altura} metros ou {int(altura*100)} cm")

# outro exercicio

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = n1 + n2
print(f"Vamos printar {n1} + {n2} = {n3}")

breakpoint