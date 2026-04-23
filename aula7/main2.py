class Pessoa:
    def __init__(self, nome, idade, cpf, cidade):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cidade = cidade
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome é obrigatorio!")
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if idade <= 0:
            raise ValueError("Idade invalida!")
        self._idade = idade

class PessoaPresenters():
    @staticmethod
    def apresentacao(saida):
        return {
            "nome": saida.nome,
            "idade": saida.idade,
            "cidade": saida.cidade
        }
    
    @staticmethod
    def apresentacao_erros(erro, codigo):
        return {
            "codigo":codigo,
            "erro": str(erro)
        }
try:
    p1 = Pessoa("Danrley Ramos", 30, 4568421459,"GOIANIA")
    p2 = Pessoa("Danrley Ramos", 30, 4568421459,"GOIANIA")
    p3 = Pessoa("Danrley Ramos", 30, 4568421459,"GOIANIA")

    lista = [p1,p2,p3]

    retorno = [
        PessoaPresenters.apresentacao(p)
        for p in lista

    ]
    print(retorno)
except ValueError as e:
    retorno = PessoaPresenters.apresentacao_erros(e,500)
    print(retorno)