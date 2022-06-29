from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)

from src.Controller.MenuPrincipalController import MenuPrincipalController
from src.model.DAO.UsuarioDAO import UsuarioDAO
from src.model.Usuario import Usuario
from src.view.templates.Ui_Cadastro import Ui_MainWindow


class CadastroController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CadastroController, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("AutoTech - Cadastro")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        # Toggle Buttons
        self.frame_error.hide()
        self.pushButton_login.clicked.connect(self.levar_para_tela_login)
        self.pushButton.clicked.connect(self.cadastrar_usuario)
        self.icon_error.clicked.connect(self.frame_error.hide)

    def exibe_mensagem(self, message):
        self.frame_error.show()
        self.text_error.setText(message)

    def levar_para_tela_login(self):
        from src.Controller.LoginController import LoginController
        self.window = LoginController()
        self.window.show()
        self.close()

    def obter_modelo(self):
        nome = self.lineEdit_nome.text()
        cpf = self.lineEdit_cpf.text()
        senha = self.lineEdit_senha.text()
        data_nascimento = self.dataNascimento.text()

        modelo = Usuario(nome, cpf, senha, data_nascimento)

        return modelo

    def cadastrar_usuario(self):
        # pegar os dados da tela
        usuario = self.obter_modelo()
        nome = usuario.get_nome
        cpf = usuario.get_cpf
        senha = usuario.get_senha
        data_nascimento = usuario.get_data_nascimento

        # validar os dados
        if nome != "" and nome is not None and cpf != "" and cpf is not None and senha != "" and senha is not None and data_nascimento != "" and data_nascimento is not None:
            # verificar se ja existe no banco de dados
            usuario_cadastrado = UsuarioDAO()
            cpf_pesquisar = usuario_cadastrado.search(cpf)
            senha_pesquisar = usuario_cadastrado.search(senha, type_s="senha")

            if cpf_pesquisar is not None:
                self.exibe_mensagem("Cpf ja existe!")
            elif senha_pesquisar is not None:
                self.exibe_mensagem("Senha ja existe")
            else:
                usuario_cadastrado.insert(usuario.get_nome, usuario.get_cpf, usuario.get_senha,
                                          usuario.get_data_nascimento, None, usuario.get_nivel_acesso)
                self.usuario_logado = cpf
                self.w = MenuPrincipalController(self.usuario_logado)
                self.w.show()
                self.close()

        elif usuario.get_nome == '' or usuario.get_nome is None:
            self.exibe_mensagem("Preencha o Campo Nome!")

        elif usuario.get_cpf == '' or usuario.get_cpf is None:
            self.exibe_mensagem("Preencha o campo Cpf")

        elif usuario.get_senha == '' or usuario.get_senha is None:
            self.exibe_mensagem("Preencha o campo senha")
