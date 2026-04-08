class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #gettors  obter osvalores
    @property
    def nome(self):
        return f"meu nome é: {self.__nome}"
    #Definir os valores
    @nome.setter
    def  nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return f"Minha idade é: {self.__idade}"
    
    @idade.setter
    def idade(self, valor):
        if valor <= 0:
            print("valor incorreto")
        self.__idade = valor


p = Pessoa("Danrley", -29)
print(p.nome)