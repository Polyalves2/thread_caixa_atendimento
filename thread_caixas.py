
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class Caixa:
    def __init__(self, nome, tempo_atendimento):
        self.nome = nome
        self.tempo_atendimento = tempo_atendimento
    
    def atender(self):
        """Versão otimizada com logging"""
        inicio = datetime.now()
        thread_id = threading.current_thread().name
        
        print(f"[{inicio.strftime('%H:%M:%S')}] {self.nome} ({thread_id}) iniciou")
        time.sleep(self.tempo_atendimento)
        
        fim = datetime.now()
        duracao = (fim - inicio).total_seconds()
        print(f"[{fim.strftime('%H:%M:%S')}] {self.nome} terminou ({duracao:.1f}s)")
        
        return {
            'caixa': self.nome,
            'duracao': duracao,
            'thread': thread_id
        }

def main():
    """Versão produção-ready"""
    # Configuração
    NUM_CAIXAS = 5
    MAX_THREADS = 3  # Não criar mais que 3 threads simultâneas
    
    # Criar caixas
    caixas = [
        Caixa(f"Caixa-{i+1}", tempo)
        for i, tempo in enumerate([3, 2, 4, 1, 5])
    ]
    
    print(f" Iniciando simulação com {NUM_CAIXAS} caixas")
    print(f" Usando pool de {MAX_THREADS} threads")
    print("-" * 40)
    
    # Usar ThreadPoolExecutor (gerencia automaticamente)
    with ThreadPoolExecutor(
        max_workers=MAX_THREADS,
        thread_name_prefix="CaixaThread"
    ) as executor:
        
        # Submeter todas as tarefas
        futuros = [executor.submit(c.atender) for c in caixas]
        
        # Coletar resultados
        resultados = []
        for i, futuro in enumerate(futuros, 1):
            try:
                resultado = futuro.result()  # Aguarda e pega resultado
                resultados.append(resultado)
                print(f" Tarefa {i} completada: {resultado['caixa']}")
            except Exception as e:
                print(f" Erro na tarefa {i}: {e}")
    
    # Relatório final
    print("\n" + "=" * 40)
    print("RELATÓRIO DE ATENDIMENTO:")
    print("=" * 40)
    
    for res in sorted(resultados, key=lambda x: x['duracao']):
        print(f"{res['caixa']}: {res['duracao']:.1f}s (Thread: {res['thread']})")
    
    tempo_total = max(r['duracao'] for r in resultados) if resultados else 0
    print(f"\n⏱️  Tempo total (paralelo): {tempo_total:.1f}s")
    print(f" Eficiência: {sum(r['duracao'] for r in resultados)/tempo_total:.1f}x")

if __name__ == "__main__":
    main()