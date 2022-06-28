import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QMainWindow, QApplication)

from src.Controller.CadastroController import CadastroController
from src.Controller.MenuPrincipalController import MenuPrincipalController
from src.model.DAO.UsuarioDAO import UsuarioDAO
from src.model.Usuario import Usuario
from src.view.templates.Ui_Login import Ui_MainWindow


class LoginController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("AutoTech - Login")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        # Toggle Buttons
        self.frame_4.hide()
        self.pushButton_close.clicked.connect(self.frame_4.hide)
        self.pushButton_login.clicked.connect(self.entrar_no_sistema)
        self.pushButton_cadastro.clicked.connect(self.levar_para_tela_cadastro)

    def exibe_mensagem(self, message):
        self.frame_4.show()
        self.label_error.setText(message)

    def obter_modelo(self):
        cpf = self.lineEdit_usuario.text()
        senha = self.lineEdit_senha.text()

        modelo = Usuario(None, cpf, senha, None)

        return modelo

    def limpar_tela(self):
        self.lineEdit_usuario.setText("")
        self.lineEdit_senha.setText("")

    def entrar_no_sistema(self):

        # pegar usuario da view
        usuario = self.obter_modelo()

        cpf = usuario.get_cpf
        senha = usuario.get_senha

        # pesquisar usuario no banco de dados
        usuario_dao = UsuarioDAO()
        usuario_autenticado_cpf = usuario_dao.search(cpf)
        usuario_autenticado_senha = usuario_dao.search(senha, type_s="senha")

        if usuario_autenticado_cpf is not None and usuario_autenticado_senha is not None:
            self.exibe_mensagem("Login Efetuado com sucesso!")
            self.limpar_tela()
            self.usuario_logado = cpf
            self.w = MenuPrincipalController(self.usuario_logado)
            self.w.show()
            self.close()
        elif cpf == '':
            self.exibe_mensagem("Preencha o campo Cpf!")
        elif senha == '':
            self.exibe_mensagem("Preencha o campo Senha!")
        elif cpf == '' and senha == '':
            self.exibe_mensagem("Preencha os Campos!")
        else:
            self.exibe_mensagem("Usuário ou senha inválidos!")


    def levar_para_tela_cadastro(self):
        self.window = CadastroController()
        self.window.show()
        self.close()

