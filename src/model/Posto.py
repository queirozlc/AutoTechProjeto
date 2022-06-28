class Posto:
    __descricao: str

    def __init__(self, nome, combustivel):
        self.__id = None
        self.__nome = nome
        self.__combustivel = combustivel

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
    def get_combustivel(self):
        lista_combustivel = []
        if type(self.__combustivel) is list:
            for item in self.__combustivel:
                if type(item) == tuple:
                    lista_combustivel.append(item)
            return lista_combustivel
        else:
            return None

    def set_combustivel(self, combustivel):
        if type(combustivel) is tuple:
            self.__combustivel.append(combustivel)
        else:
            return None
