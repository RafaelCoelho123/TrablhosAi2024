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
