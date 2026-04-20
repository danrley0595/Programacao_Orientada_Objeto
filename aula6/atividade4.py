class Produto():
    def __init__(self, nome, preco ):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco
        
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError(f"Valor inválido! O produto {self.nome} não pode ter preço negativo.")
        self._preco = valor

class Carrinho():
    def __init__(self):
        self.lista_prod = []

    def Adicionar(self, produto):

        self.lista_prod.append(produto)

    def Calcular_Total(self):
        total = 0
        for produto in self.lista_prod:
            total += produto.preco
        return total    

    def Listar(self):
        for produto in self.lista_prod:
            print(f"Nome Produto:{produto.nome} -- Preço:{produto.preco}")
        print(f"Total Compra: {self.Calcular_Total()}")

try:
    meu_carrinho = Carrinho()
    p1 = Produto("Teclado",200)
    p2 = Produto("TV",5000)
    p3 = Produto("Som",2500)

    meu_carrinho.Adicionar(p1)
    meu_carrinho.Adicionar(p2)
    meu_carrinho.Adicionar(p3)
    meu_carrinho.Listar()

except ValueError as e:
    print(e)