class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def ver_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo :
            print("Saldo Insuficiente.")  
        else : 
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")

    def transferir_valor(self, valor, conta_destino):
        if valor > self.__saldo :
            print("Saldo Insuficiente.")  
        else : 
            self.__saldo -= valor
           # self.sacar(valor)
            conta_destino.depositar(valor)


c1 = ContaBancaria("Danrley", 10000.00)
c2 = ContaBancaria("João", 5000.00)


print(f"Seu saldo atual é: {c1.ver_saldo()}")
c1.depositar(225.69)
print(f"Seu saldo atual é: {c1.ver_saldo()}")
c1.sacar(200)
c1.transferir_valor(200,c2)
print(f"Seu saldo atual é: {c1.ver_saldo()}")
print(f"Seu saldo atual é: {c2.ver_saldo()}")