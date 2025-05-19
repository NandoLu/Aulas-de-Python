# Batalha naval
inimigos = [(10,90), (23,24)]
tupla = ("D", "A", "B")

for x, y in inimigos:
    print(f"A posição: x = {x} y = {y}")

x = int(input("Informe a posição x:"))
y = int(input("Informe a posição y:"))

if(x, y) in inimigos:
    inimigos.remove((x, y))
    print("Você acertou um inimigo!")
else:
    print("Água, você errou!")
print(inimigos)