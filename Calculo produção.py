from datetime import datetime, timedelta
import os

def calcular_conclusao_loop():
    while True:
        # Limpa a tela a cada nova simulação para manter o visual limpo
        # (Usa 'cls' para Windows e 'clear' para Linux/Mac)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("--- Simulador de Produção Contínua (24h) ---")
        
        # 1. Coleta de dados do usuário
        try:
            quantidade_total = float(input("Digite a quantidade TOTAL de produtos: "))
            qtd_por_hora = float(input("Quantos produtos a máquina faz POR HORA?: "))
            
            data_inicio_str = input("Qual o dia e hora de início? (Formato: DD/MM/AAAA HH:MM): ")
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")
        except ValueError:
            print("\n[Erro]: Certifique-se de digitar números e a data no formato correto.")
            input("\nPressione ENTER para tentar novamente...")
            continue  # Volta para o início do loop

        # 2. Cálculos de tempo
        horas_totais = quantidade_total / qtd_por_hora
        data_final = data_inicio + timedelta(hours=horas_totais)

        # 3. Exibição dos resultados
        print("\n" + "="*40)
        print("           RESUMO DA PRODUÇÃO")
        print("="*40)
        print(f"• Ritmo de produção: {qtd_por_hora} unidades/hora")
        print(f"• Total de horas necessárias: {horas_totais:.2f} horas")
        print(f"• **Previsão exata de conclusão:** {data_final.strftime('%d/%m/%Y às %H:%M')}")
        print("="*40)

        # 4. Comando de Reinício ou Saída
        print("\n" + "-"*40)
        resposta = input("Deseja fazer outra simulação? [S/N] (Pressione ENTER para Sim): ").strip().lower()
        
        # Se o usuário digitar 'n' ou 'nao', o programa quebra o loop e fecha
        if resposta in ['n', 'nao', 'não']:
            print("\nSimulador encerrado. Até logo!")
            break

if __name__ == "__main__":
    calcular_conclusao_loop()