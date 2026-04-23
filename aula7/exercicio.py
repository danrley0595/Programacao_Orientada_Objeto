class Pedido():
    def __init__(self, valor):
        self.valor = valor 

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValueError("Valor Incorreto!")
        else:
            self._valor = valor


    @staticmethod
    def calcular_Desconto(valor):
        if valor > 100:
            desconto = (valor*10)/100

        else: desconto = 0
        return desconto

try:
    pedido = Pedido(-500)
    print(Pedido.calcular_Desconto(pedido.valor))
except ValueError as e:
    print(e)