from abc import ABC, abstractmethod


class IHelper(ABC):
    @abstractmethod
    def obter_modelo(self):
        pass

    @abstractmethod
    def limpar_tela(self):
        pass
