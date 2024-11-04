# Configuração de histórico e funções auxiliares

HISTORICO_MAX = 5
historico = []

def adicionar_historico(operacao):
    """Adiciona uma operação ao histórico, removendo a mais antiga se necessário."""
    if len(historico) >= HISTORICO_MAX:
        historico.pop(0)
    historico.append(operacao)

def mostrar_historico():
    """Mostra o histórico das últimas operações realizadas."""
    print("\nHistórico das últimas operações:")
    if historico:
        for i, operacao in enumerate(historico, 1):
            print(f"{i}. {operacao}")
    else:
        print("Nenhuma operação no histórico ainda.")
# Função principal da calculadora com menu

def calculadora():
    """Executa a calculadora interativa com opções de operação e histórico."""
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Histórico")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada: ")

        # Condição de saída
        if opcao == '6':
            print("Saindo da calculadora.")
            break

        # Opção para mostrar o histórico
        elif opcao == '5':
            mostrar_historico()
        
        else:
            print("Opção inválida. Tente novamente.")
# Funções para solicitar números e realizar operações

def solicitar_numeros():
    """Solicita dois números inteiros do usuário e trata erros de entrada."""
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("Por favor, digite números válidos.")
        return None, None

def realizar_operacao(opcao, num1, num2):
    """Executa a operação selecionada e retorna a descrição do resultado."""
    if opcao == '1':
        resultado = num1 + num2
        operacao = f"{num1} + {num2} = {resultado}"
    elif opcao == '2':
        resultado = num1 - num2
        operacao = f"{num1} - {num2} = {resultado}"
    elif opcao == '3':
        resultado = num1 * num2
        operacao = f"{num1} * {num2} = {resultado}"
    elif opcao == '4':
        if num2 == 0:
            print("Erro: Divisão por zero não permitida.")
            return None
        resultado = num1 // num2
        operacao = f"{num1} // {num2} = {resultado}"
    else:
        print("Operação inválida.")
        return None
    return operacao

# Atualização da função principal com as operações

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Histórico")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '6':
            print("Saindo da calculadora.")
            break
        elif opcao == '5':
            mostrar_historico()
        elif opcao in ('1', '2', '3', '4'):
            num1, num2 = solicitar_numeros()
            if num1 is None or num2 is None:
                continue
            operacao = realizar_operacao(opcao, num1, num2)
            if operacao:
                print("Resultado:", operacao)
                adicionar_historico(operacao)
        else:
            print("Opção inválida. Tente novamente.")

# Inicia a calculadora
calculadora()
