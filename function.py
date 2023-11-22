from datetime import datetime, timedelta
import time

class Contador:
    def __init__(self):
        self.data_inicial = datetime.now()
        self.contador = 0
        self.checker()

    def checker(self):
        while True:
            if datetime.now() > self.data_inicial + timedelta(days=1):
                self.data_inicial = datetime.now()
                self.contador += 1
                print(f"Contador: {self.contador}")
            time.sleep(60)

contador_instancia = Contador()
