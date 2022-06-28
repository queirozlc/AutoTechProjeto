from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QMainWindow, QMessageBox)

from src.model.Cliente import Cliente
from src.model.DAO.ClienteDAO import ClienteDAO
from src.model.DAO.CombustivelDAO import CombustivelDAO
from src.model.DAO.UsuarioDAO import UsuarioDAO
from src.view.templates.Ui_MenuPrincipal import Ui_MainWindow


class MenuPrincipalController(QMainWindow, Ui_MainWindow):
    def __init__(self, usuario_logado):
        super(MenuPrincipalController, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("AutoTech - Menu Principal")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        self.__usuario_ativo = usuario_logado
        self.preencher_informacoes_usuario()
        self.preencher_combustivel()

        # TOGGLE BUTTONS
        self.pushButton_toggle.clicked.connect(self.show_menu)
        self.botaoCadastrarCliente.clicked.connect(self.cadastrar_cliente)
        self.btnVerEstoque.clicked.connect(self.checar_estoque)
        self.btnAbastecerEstoque.clicked.connect(self.abastecer_estoque)

        ### Setando as páginas do sistema
        self.pushButtonHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.pushButtonBusca.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_buscarPlaca))
        self.pushButtonVendas.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_vendas))
        self.pushButtonEstoque.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_estoque))
        self.pushButtonCadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrarCliente))

    # métodos auxiliares

    def obter_cliente(self):
        nome = self.campoNomeCadastro.text()
        cpf = self.campoTextoCPF.text()
        data_nascimento = self.dataText.text()
        placa = self.campoPlacaCadastro.text()

        modelo_cliente = Cliente(nome, cpf, data_nascimento, placa)

        return modelo_cliente

    def preencher_combustivel(self):
        # trazer todos os combustiveis do banco de dados
        combustivel_dao = CombustivelDAO()
        lista_combustivel = combustivel_dao.select_all()

        # selecionar e armazenar o nome de todos os combustiveis
        nomes = []

        for i, nome in enumerate(lista_combustivel):
            nomes.append(nome[1])

        # setar os nomes dentro do comboBox
        for item in nomes:
            self.comboBoxCombustivel.addItem(item)

    def show_menu(self):
        width = self.leftMenu.width()

        if width == 9:
            new_width = 200
        else:
            new_width = 9

        self.animation = QtCore.QPropertyAnimation(self.leftMenu, b"maximumWidth")
        self.animation.setDuration(550)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # Metodo para home page
    def preencher_informacoes_usuario(self):
        # Pesquisa Usuário no banco de dados
        usuario_dao = UsuarioDAO()
        usuario_a_pesquisar = usuario_dao.search(self.__usuario_ativo)

        # Obter os dados separados e armazenar em variaveis
        for item in usuario_a_pesquisar:
            usuario_ativo_nome = item[1]
            usuario_ativo_cpf = item[2]

        # mostrar os dados na tela
        if usuario_ativo_nome != '' and usuario_ativo_nome is not None and usuario_ativo_cpf != '' and usuario_ativo_cpf is not None:
            self.nomeUsuarioLogado.setText(usuario_ativo_nome)
            self.cpfUsuarioLogado.setText(usuario_ativo_cpf)
            self.campoStatusLogado.setText("Ativo")

        else:
            return None

    # Método para cadastrar cliente
    def cadastrar_cliente(self):
        # buscar um modelo da tela
        cliente_a_cadastrar = self.obter_cliente()

        # fazer as verificações no banco de dados
        placa_a_pesquisar = cliente_a_cadastrar.get_placa
        cpf_a_pesquisar = cliente_a_cadastrar.get_cpf

        cliente_dao = ClienteDAO()
        cpf_pesquisado = cliente_dao.search(cpf_a_pesquisar)
        placa_pesquisada = cliente_dao.search(placa_a_pesquisar, type_s="placa")

        # se passar nas verificações, então cadastrar cliente, se não, então retornar um erro
        nome = cliente_a_cadastrar.get_nome
        cpf = cliente_a_cadastrar.get_cpf
        data_nascimento = cliente_a_cadastrar.get_data_nascimento
        placa = cliente_a_cadastrar.get_placa

        if cpf_pesquisado is not None:
            QMessageBox.warning(QMessageBox(), "Erro!", "Este cpf ja existe!")

        elif placa_pesquisada is not None:
            QMessageBox.warning(QMessageBox(), "Erro!", "Esta placa ja existe!")

        elif nome == '' or cpf == '' or data_nascimento == '' or placa == '':
            QMessageBox.warning(QMessageBox(), "Erro !", "Preencha todos os campos !")

        else:
            cliente_dao.insert(cliente_a_cadastrar.get_nome, cliente_a_cadastrar.get_cpf,
                               cliente_a_cadastrar.get_data_nascimento, None, cliente_a_cadastrar.get_placa)
            QMessageBox.warning(QMessageBox(), "Ok!", "Cadastro Realizado com Sucesso!")

    # Método para checar estoque de combustivel
    def checar_estoque(self):
        # obter modelo da tela
        combustivel = self.comboBoxCombustivel.currentText()

        # pesquisar combustivel no banco de dados

        combustivel_dao = CombustivelDAO()
        combustivel_pesquisado = combustivel_dao.search(combustivel, type_s="descricao")

        # validar se o combustivel realmente existe no banco de dados

        if combustivel_pesquisado is not None:
            quantidade = 0
            for item in combustivel_pesquisado:
                quantidade = float(item[2])

            self.doubleSpinBox.setValue(quantidade)
        else:
            QMessageBox.warning(QMessageBox(), "Erro!", "Este combustivel não existe!")

    # Método para abastecer estoque
    def abastecer_estoque(self):
        # obter modelo da tela
        combustivel = self.comboBoxCombustivel.currentText()

        # pesquisar combustivel no banco de dados

        combustivel_dao = CombustivelDAO()
        combustivel_pesquisado = combustivel_dao.search(combustivel, type_s="descricao")

        # validar se o combustivel realmente existe no banco de dados

        if combustivel_pesquisado is not None:
            quantidade = self.doubleSpinBox.value()
            quantidade_disponivel = 0
            nome = ''
            valor = 0
            observacao = ''
            combustivel_id = 0

            for item in combustivel_pesquisado:
                combustivel_id = item[0]
                nome = item[1]
                quantidade_disponivel = float(item[2])
                valor = item[3]
                observacao = item[4]

            if quantidade <= quantidade_disponivel:
                QMessageBox.warning(QMessageBox(), "Erro !",
                                    "A Quantidade A Abastecer Deve Ser Maior que a Disponível !")
            else:
                QMessageBox.warning(QMessageBox(), "Ok !", "O Estoque Foi Abastecido com Sucesso !")
                combustivel_dao.update(combustivel_id, nome, quantidade, valor, observacao)
