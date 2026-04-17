class Produto():
    def __init__(self, nome, preco):
        self._nome = nome
        self.preco = preco

    @property # getter
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        if (preco<0):
            raise ValueError("Valor invalido!")
        else:
            self._preco = preco
    def __str__(self):
        return f"Nome produto: {self._nome} preço: {self.preco}"

try:
    p1 = Produto("Teste", -100)
    print(p1)
except ValueError as e:
    print(e)