from src.model.Posto import Posto


class Servico:
    def __init__(self, descricao, cliente, posto, combustivel, quantidade, valor):
        self.__id = None
        self.__descricao = descricao
        self.__cliente = cliente
        self.__posto = posto
        self.__combustivel = combustivel
        self.__quantidade = quantidade
        self.__valor = valor

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
    def get_descricao(self):
        if type(self.__descricao) is str:
            return self.__descricao
        else:
            return None

    def set_descricao(self, descricao):
        if type(descricao) is str:
            self.__descricao = descricao
        else:
            return None

    @property
    def get_cliente(self):
        if type(self.__cliente) is str:
            return self.__cliente
        else:
            return None

    def set_cliente(self, cliente):
        if type(cliente) is str:
            self.__cliente = cliente
        else:
            return None

    @property
    def get_posto(self):
        if type(self.__posto) is str:
            return self.__posto
        else:
            return None

    def set_posto(self, posto):
        if type(posto) is str:
            self.__posto = posto
        else:
            return None

    @property
    def get_combustivel(self):
        if type(self.__combustivel) is str:
            return self.__combustivel
        else:
            return None

    def set_combustivel(self, combustivel):
        if type(combustivel) is str:
            self.__combustivel = combustivel
        else:
            return None

    @property
    def get_valor(self):
        if type(self.__valor) is float:
            return self.__valor
        else:
            return None

    def set_valor(self, valor):
        if type(valor) is float:
            self.__valor = valor
        else:
            return None

    @property
    def get_quantidade(self):
        if type(self.__quantidade) is str and self.__quantidade != '':
            return float(self.__quantidade)
        else:
            return None

    def set_quantidade(self, quantidade):
        if type(quantidade) is float:
            self.__quantidade = quantidade


