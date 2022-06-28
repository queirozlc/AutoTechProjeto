from src.model.Pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, cpf, data_nascimento, placa):
        Pessoa.__init__(self, nome, cpf, data_nascimento)
        self.__id = None
        self.__placa = placa

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
    def get_placa(self):
        if type(self.__placa) is str:
            return self.__placa
        else:
            return None

    def set_placa(self, placa):
        if type(placa) is str:
            self.__placa = placa

    def abs(self):
        pass
