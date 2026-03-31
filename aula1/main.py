#class Pessoa  a primeira letra da classe em maiusculo
#self declarar atributo
# class representação do objeto
# init utilizado para iniciarlizar os valores das variaveis p
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print("Olá sou o",self.nome)

p1 = Pessoa("João", 20)
p2 = Pessoa("Maria", 25)

print(f"Nome: {p1.nome} nome:{p1.idade}")

p1.falar()