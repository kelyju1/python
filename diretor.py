from usuario import Usuario

class Diretor (Usuario):
    def _init_ (self, nome, cpf, salario, email, senha):
        super()._init_(nome, cpf, salario, email, senha)