while True:

    nome_completo=input("Informe o seu nome completo: ")
    ano_nasc=int(input("Informe o ano de seu nascimento (entre 1922 e 2021): "))

    try:
        ano_nasc=int(ano_nasc)
        if ano_nasc<1922 or ano_nasc>2021:
            raise ValueError
    except ValueError:
        print("Ano de nascimento inválido. Por favor, tente novamente.")
        continue

    idade=2023-ano_nasc

    print(f"Olá, {nome_completo}. No ano de 2023 você completou ou completará {idade} anos.")
    break 





