while True:
    try:
        nome = input("Digite seu nome completo: ")
        ano = int(input("Digite o ano de nascimento (entre 1922 e 2024): "))
        if 1922 <= ano <= 2024:
            idade = 2024 - ano
            print(f"{nome}, você completou ou completará {idade} anos em 2024.")
            break
        else:
            print("Erro: O ano de nascimento deve estar entre 1922 e 2024. Tente novamente.")
    except ValueError:
        print("Erro: Você deve digitar um número válido para o ano de nascimento. Tente novamente.")