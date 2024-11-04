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
