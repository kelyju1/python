from usuario import Usuario
class Funcionario(Usuario):
    def __init__ (self, nome, cpf, salario, email, senha):
        super().__init__(nome, cpf, salario, email, senha)
        
       
    def Informacoes_funcionarios(self):
        print("------INFORMAÇÕES-------")
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        print("Sálario: ", self.salario)
        print("E-mail:;", self.email )
        print("------------------------")

    def Bonificacao(self):
        reajuste = float
        print("------Calculando bonificação------")
        reajuste = self._salario * 0.10 
        print("Sálario reajustado: ", reajuste)