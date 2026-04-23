class Calculadora():
    def __init__(self):
        self.numero = 5

    @staticmethod # metodo estatico
    #USar quando não depender de nada da classe
    def somar( a, b):
        return a + b

class Validar():
    @staticmethod
    def email_valido(email):
        return "@" in email
    
c = Calculadora()
print(Calculadora.somar(c.numero,5))
print(Validar.email_valido("danrley@teste.co,"))