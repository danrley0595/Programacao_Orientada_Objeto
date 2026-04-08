class Produto():
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

    @property
    def nome(self):
        return f"Produto:{self.__nome}"
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            print("Preço Inválido")
        else:
            self.__preco = valor

p1 = Produto("Teclado", 100)
p2 = Produto("Monitor", 950.66)

p1.nome = "Mini Teclado"
p2.preco = -999

print(f"{p1.nome} - {p1.preco}")
print(f"{p2.nome} - {p2.preco}")

        