class Intervalo:
    def __init__(self, inicio , fin):
        if(inicio <= fin):
            print("El intervalo tiene que tener distancia > 0")
        else:
            self.inicio = inicio
            self.fin = fin

