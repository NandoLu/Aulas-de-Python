def menu():
    print("---MENU---")
    print("1 ---- Calcular velocidade media")
    print("2 ---- Converter temperatura")
    print("3 ---- Sair do sistema")

def calc_velocidade_media(distancia:float, tempo:float, uni_medida="km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia/tempo
    return f"{velocidade_media} {uni_medida}"

def converter_temp(temperatura:float, uni_medida="celsius"):
    if uni_medida == "celsius":
        return temperatura * 1.8 * 32
    elif uni_medida == "fahrenheit":
        return (temperatura - 32) /1.8
    else:
        return 0
    
def aluno():
    op = 0
    while op != 3:
        menu()
        op = int(input("Informe qual opção desejada: "))
        match op:
            case 1:
                distancia = float(input("Informe a distancia: "))
                tempo = float(input("Informe o tempo: "))
                medida = input("Informe a unidade de medida: ")
                print(f"A velocidade média é: {calc_velocidade_media(distancia, tempo, medida)}")
            case 2:
                temperatura = float(input("Informe a temperatura desejada: "))
                medida = input("Informe a medida (celsius ou fahrenheit): ")
                print(f"A temperatura convertida é {converter_temp(temperatura, medida)}")
            case 3:
                print("saindo do sistema...")
                break
            case _:
                print("Opção inválida!!!")