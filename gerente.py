from usuario import Usuario

class Gerente (Usuario):
    def _init_ (self, nome, cpf, salario, email,senha, qtde_funcionarios):
        super()._init_(nome, cpf, salario, email, senha)
        self.qtde_funcionarios = qtde_funcionarios

    @property
    def qtde_funcionarios(self):
        return self._qtde_funcionarios

    @qtde_funcionarios.setter
    def qtde_funcionarios(self, qtde_funcionarios ):
        self._qtde_funcionarios = qtde_funcionarios