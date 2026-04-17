class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self, salario):
        return salario * (10/ 100)
    
class Gerente(Funcionario):
    def calcular_bonus(self, salario):
        return salario * (20 / 100)
    
class Desenvolvedor(Funcionario):
    def calcular_bonus(self, salario):
        return salario * (15 / 100)

funcionarios: list[Funcionario] = []   # cria uma lista do tipo Funcionario
funcionarios.append(Desenvolvedor("João", 5000))
funcionarios.append(Gerente("Maria", 7000))
funcionarios.append(Desenvolvedor("Pedro", 5000))
funcionarios.append(Funcionario("Matheus", 7000))

for func in funcionarios:
    print(f"Nome Funcionario: {func.nome} - Salario: {func.salario} - Comissão: {func.calcular_bonus(func.salario)} Total:{func.salario+func.calcular_bonus(func.salario)}")


