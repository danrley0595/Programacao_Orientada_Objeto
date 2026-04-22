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

    def __add__(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor

        else: raise ValueError("Valor invalido!")
        return self

    def __sub__(self, valor):
        if valor > 0:
            self.saldo = self.saldo - valor
        else: raise ValueError("Valor invalido!")
        return self
    
    def __str__(self):
        return f"Ola {self.titular} seu saldo é {self._saldo}"
    
try:
    c1 = ContaBancaria("Maria", 1000)
    c2 = ContaBancaria("Pedro", 10000)

    c2 + 500
    c1 - 100

    print(c1)
    print(c2)
except ValueError as e:
    print(e)
