from src.model.Posto import Posto


class Servico:
    def __init__(self, descricao, cliente, posto, quantidade):
        self.__id = None
        self.__descricao = descricao
        self.__cliente = cliente
        self.__posto = posto
        self.__valor = 0
        self.__quantidade = quantidade

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
        lista_cliente = []
        if type(self.__cliente) is list:
            for item in self.__cliente:
                if type(item) == tuple:
                    lista_cliente.append(item)
            return lista_cliente
        else:
            return None

    def set_cliente(self, cliente):
        if type(cliente) is tuple:
            self.__cliente.append(cliente)
        else:
            return None

    @property
    def get_posto(self):
        lista_posto = []
        if type(self.__posto) is list:
            for item in self.__posto:
                if type(item) == Posto:
                    lista_posto.append(item)
            return lista_posto
        else:
            return None

    def set_posto(self, posto):
        if type(posto) is Posto:
            self.__posto.append(posto)
        else:
            return None

    @property
    def get_valor(self):
        if type(self.__valor) is float:
            valor_total = (self.__valor * self.get_posto().get_combustivel().get_valor())
            return valor_total
        else:
            return None

    def set_valor(self, valor):
        if type(valor) is float:
            self.__valor = valor
        else:
            return None

    @property
    def get_quantidade(self):
        if type(self.__quantidade) is float:
            return self.__quantidade
        else:
            return None

    def set_quantidade(self, quantidade):
        if type(quantidade) is float:
            self.__quantidade = quantidade


