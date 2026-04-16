class Numero():
    def __init__(self, valor):
        self.valor = valor
    
    def __add__(self, other):
        return f"Soma: {self.valor + other.valor}"

v1 = Numero(12)
v2 = Numero(25)

print(v1 + v2)