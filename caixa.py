import threading
import time

class Caixa:
    def __init__(self, nome, tempo_atendimento):
        self.nome = nome
        self.tempo_atendimento = tempo_atendimento

    def atender(self):
        print(f"{self.nome} está atendendo...")
        time.sleep(self.tempo_atendimento)
        print(f"{self.nome} terminou de atender.")

def main():
    caixa1 = Caixa("Caixa 1", 3)
    caixa2 = Caixa("Caixa 2", 2)
    caixa3 = Caixa("Caixa 3", 4)

    thread1 = threading.Thread(target=caixa1.atender)
    thread2 = threading.Thread(target=caixa2.atender)
    thread3 = threading.Thread(target=caixa3.atender)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()