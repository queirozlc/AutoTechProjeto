from src.Controller.LoginController import LoginController
from src.Controller.helper.IHelper import IHelper
from src.model.Usuario import Usuario


class LoginHelper(LoginController, IHelper):

    def __init__(self):
        super(LoginHelper, self).__init__()

    def obter_modelo(self):
        cpf = self.lineEdit_usuario.text()
        senha = self.lineEdit_senha.text()

        modelo = Usuario(None, cpf, senha)

        return modelo

    def limpar_tela(self):
        self.lineEdit_usuario.setText("")
        self.lineEdit_senha.setText("")
