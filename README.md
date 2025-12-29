# 🧵 Thread - Caixa de Atendimento

## Um sistema de simulação de caixas de atendimento que utiliza threads para processamento paralelo, demonstrando conceitos de concorrência e programação multithreading em Python. ##

# 📋 Visão Geral
## Este projeto simula um ambiente bancário com múltiplos caixas atendendo clientes simultaneamente. Utiliza threads para processamento paralelo, mostrando como otimizar o tempo de atendimento através do uso eficiente de recursos. ##

# 🚀 Funcionalidades
# Versão Simples (caixa.py)
✅ Criação básica de threads

✅ Atendimento sequencial com paralelismo

✅ Controle manual de threads 

# Versão Avançada (thread_caixas.py) #

✅ Pool de threads com ThreadPoolExecutor

✅ Logging com timestamps precisos

✅ Coleta de métricas e estatísticas

✅ Relatório de desempenho automático

✅ Controle de threads simultâneas

✅ Tratamento de exceções

✅ Cálculo de eficiência do paralelismo

# 🛠️ Tecnologias Utilizadas #

Python 3.8+

Threading - Para execução concorrente

Concurrent.futures - Para gerenciamento de pools de threads

Datetime - Para logging com timestamps precisos

Time - Para simulação de tempo de atendimento

# 🚀 Como Executar #

## Versão Simples: ##

bash

python caixa.py

## Versão Avançada: ##

bash

python thread_caixas.py


# 🎯 Conceitos Demonstrados #
# 1. Threading Básico #
python

import threading

thread = threading.Thread(target=funcao)

thread.start()

thread.join()

# 2. ThreadPoolExecutor #
python

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:

    futuro = executor.submit(tarefa)
    
    resultado = futuro.result()
    
# 3. Sincronização #
Controle de threads simultâneas

Coleta ordenada de resultados

Logging thread-safe

# 4. Métricas de Desempenho #
Tempo total vs tempo sequencial

Cálculo de eficiência do paralelismo

# Análise de throughput #

🔧 Personalização
Ajustar Configurações:
python
# No arquivo thread_caixas.py #
NUM_CAIXAS = 10          # Número de caixas

MAX_THREADS = 4          # Threads simultâneas

TEMPOS_ATENDIMENTO = [1, 3, 2, 4, 1, 2, 3, 1, 2, 4]  # Tempos personalizados

Adicionar Novos Recursos:

Fila de clientes - Implementar queue.Queue()

Prioridades - Usar PriorityQueue

Timeout - Adicionar timeout ao future.result()

# 📈 Análise de Desempenho #
O sistema demonstra o Paradoxo de Amdahl na prática:

Tempo Sequencial: 3 + 2 + 4 + 1 + 5 = 15s

Tempo Paralelo (3 threads): 7s

Eficiência: 15 / 7 ≈ 2.14x

Speedup: T_sequencial / T_paralelo


# 🔧 Instalação e Configuração
## Clonar o repositório
bash

cd\

git clone https://github.com/seu-usuario/thread-caixa-atendimento.git





