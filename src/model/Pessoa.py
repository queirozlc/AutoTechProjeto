import abc


class Pessoa(abc.ABC):
    def __init__(self, nome, cpf, data_nascimento=None):
        self.__endereco: str
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def get_nome(self):
        if type(self.__nome) is str:
            return self.__nome
        else:
            return None

    def set_nome(self, nome):
        if type(nome) is str:
            self.__nome = nome
        else:
            return None

    @property
    def get_cpf(self):
        if type(self.__cpf) is str:
            return self.__cpf
        else:
            return None

    def set_cpf(self, cpf):
        if type(cpf) is str:
            self.__cpf = cpf
        else:
            return None

    @property
    def get_data_nascimento(self):
        if type(self.__data_nascimento) is str:
            return self.__data_nascimento
        else:
            return None

    def set_data_nascimento(self, data_nascimento):
        if type(data_nascimento) is str and data_nascimento != "":
            self.__data_nascimento = data_nascimento
        else:
            return None

    @property
    def get_endereco(self):
        if type(self.__endereco) is str:
            return self.__endereco
        else:
            return None

    def set_endereco(self, endereco):
        if type(endereco) is str and endereco != "":
            self.__endereco = endereco
        else:
            return None

    ## método para habilitar a abstração da classe
    @abc.abstractmethod
    def abs(self):
        pass
