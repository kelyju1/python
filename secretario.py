from usuario import Usuario

class Secretario (Usuario):
    def _init_ (self, nome, cpf, salario, email, senha):
        super()._init_(nome, cpf, salario, email, senha)