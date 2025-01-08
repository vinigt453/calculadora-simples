def calculadora():
    print("Bem-vindo à Calculadora Simples!\n")
    print("Selecione a operação que deseja realizar:")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - [Sair]")

    while True:
        opção = input("\nDigite o número da operação: ")

        if opção == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if opção not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
            continue

        if opção == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opção == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opção == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opção == '4':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")

if __name__ == "__main__":
    calculadora()
