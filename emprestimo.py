indeferido = "Nao pode emprestimo"
deferido = "Pode emprestimo"

negativado = input("Está com o nome negativado? ")
if(negativado == "nao"):
    carteira_ass = input("Trabalha com carteira assinada? ")
    if(carteira_ass == "sim"):
        imovel = input("Possui imovel? ")
        if(imovel == "sim"):
            print(deferido)
        else:
            print(indeferido)
    else:
        print(indeferido)  
else:
    print(indeferido)
   
        