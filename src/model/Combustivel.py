class Combustivel:
    def __init__(self, descricao, quantidade, valor):
        self.__id = None
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__valor = valor
        self.__observacao = None

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
    def get_quantidade(self):
        if type(self.__quantidade) is float:
            return self.__quantidade
        else:
            return None

    def set_quantidade(self, quantidade):
        if type(quantidade) is float:
            self.__quantidade = quantidade
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
    def get_observacao(self):
        if type(self.__observacao) is str:
            return self.__observacao
        else:
            return None

    def set_observacao(self, observacao):
        if type(observacao) is str:
            self.__observacao = observacao
        else:
            return None
