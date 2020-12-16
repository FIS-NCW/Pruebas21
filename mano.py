from carta import Carta

class Mano:       
    
    def __init__(self):
        self.cartas=[]
        

    def mano_con_lista(self, lista):
         for t in lista:
            valor, pinta = t[1:-1].split(",")
            self.cartas.append(Carta(valor, pinta))

    def agregar_carta(self,valor,pinta):
        self.cartas.append(Carta(valor, pinta))

    def evaluar(self):
        valor = 0
        for c in self.cartas:
            valor += c.evaluar()
        if self.tiene_a() and valor <= 11:
            valor += 10
        return valor

    def tiene_a(self):
        for c in self.cartas:
            if c.evaluar() == 1:
                return True
        return False

    def dar_cantidad_cartas(self):
        return len(self.cartas)

    def plantar(self,valor):
            return (valor>=18)

        