class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo<0):
            raise ValueError("Valor invalido!")
        else:
            self._saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        self.saldo = self.saldo - valor

    def __gt__(self, other):
        return self.saldo > other.saldo
    
    def __str__(self):
        return f"Ola {self.titular} seu saldo é {self._saldo}"
    
class ContaCorrente(ContaBancaria):

    def sacar(self, valor):
        taxa = 2
        self.saldo = self.saldo - valor - taxa
try:
    c1 = ContaCorrente("Maria", 1000)
    c2 = ContaCorrente("Pedro", 10000)

    c2.sacar(500)
    c1.depositar(200)

    print(c1>c2)

    print(c1)
    print(c2)
except ValueError as e:
    print(e)


    

