from src.model.Pessoa import Pessoa


class Usuario(Pessoa):

    def __init__(self, nome, cpf, senha, data_nascimento, nivel_acesso="Usuário"):
        super().__init__(nome, cpf)
        self.__id = None
        self.__senha = senha
        self.__data_nascimento = data_nascimento
        self.__nivel_acesso = nivel_acesso

    @property
    def get_id(self):
        if type(self.__id) is int:
            return self.__id
        else:
            return None

    def set_id(self, id):
        if type(id) is int:
            self.__id = id
        else:
            return None

    @property
    def get_senha(self):
        if type(self.__senha) is str:
            return self.__senha
        else:
            return None

    def set_senha(self, senha):
        if type(senha) is str:
            self.__senha = senha
        else:
            return None

    @property
    def get_data_nascimento(self):
        if type(self.__data_nascimento) is str:
            return self.__data_nascimento
        else:
            return None

    def set_data_nascimento(self, data_nascimento):
        if type(data_nascimento) is str:
            self.__data_nascimento = data_nascimento
        else:
            return None


    @property
    def get_nivel_acesso(self):
        if type(self.__nivel_acesso) is str:
            return self.__nivel_acesso
        else:
            return None

    def set_nivel_acesso(self, nivel_acesso):
        if type(nivel_acesso) is str and nivel_acesso != '' and nivel_acesso != "Administrador" and nivel_acesso != "Usuario":
            self.__nivel_acesso = nivel_acesso
        else:
            return None

    def abs(self):
        pass
