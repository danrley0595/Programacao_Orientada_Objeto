class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __gt__(self, other):
        return self.preco > other.preco
    
    def __eq__(self, other):
        return self.preco == other.preco        

p1 = Produto("Teclado", 150)
p2 = Produto("Mouse", 150)
if((p1>p2) == True):
    print("Comparação dos produtos é verdadeira")
else: 
    print("Comparação dos produtos é falsa")

print(p1==p2)

if((p1==p2) == True):
    print(f"Os valores dos produtos {p1.nome} e {p2.nome} são iguais!")
else: 
    print(f"Os valores dos produtos {p1.nome} e {p2.nome} são diferentes!")