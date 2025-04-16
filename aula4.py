while True:
    comando = input("Digite um comando: ")

    match comando:
        case "iniciar":
            print("Sistema iniciado.")
        case "parar":
            print("Sistema parado.")
        case "sair":
            print("Encerrando o programa...")
            break # Sai do while e encerra o programa
        case _:
            print("Comando inválido.")

        