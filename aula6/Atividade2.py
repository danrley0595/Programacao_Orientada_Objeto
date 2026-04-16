class Caixa():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def __mul__(self, other):
        return f"Area: {self.largura * other.altura}"
    
c1 = Caixa(165,10)
print(c1 * c1)
        