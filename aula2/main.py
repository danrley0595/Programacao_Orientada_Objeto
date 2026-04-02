class Conta:
# declarando a classe

    # criando o construtor e seus atributos
    def __init__(self, saldo):
        self.__saldo = saldo

    def saldo_atual(self):
        return self.__saldo
    
    def adicionar_valor(self, valor):
        self.__saldo += valor

    def debitar(self, valor):
        if valor > self.__saldo:
            print("Saldo Insuficiente!")
        else:
            self.__saldo -= valor
    
    #consulta saldo, mas não pode alterar
    @property
    def saldo(self):
        return self.__saldo
    
    # alterar valor via parametro
    @saldo.setter
    def saldo(self, valor):
        if valor< 0:
            print("Não pode menor que 0")
        else : saldo = valor


c1 = Conta(1690.99)
c1.adicionar_valor(50)
c2 = Conta(2655)
c2.debitar(100)

print(c1.saldo_atual())
print(c2.saldo_atual())
#acessando o parametro saldo que é publico