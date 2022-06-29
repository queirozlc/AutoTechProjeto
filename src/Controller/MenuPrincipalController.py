from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QMainWindow, QMessageBox)

from src.model.Cliente import Cliente
from src.model.DAO.ClienteDAO import ClienteDAO
from src.model.DAO.CombustivelDAO import CombustivelDAO
from src.model.DAO.PostoCombustivelDAO import PostoCombustivelDAO
from src.model.DAO.PostoDAO import PostoDAO
from src.model.DAO.ServicoDAO import ServicoDAO
from src.model.DAO.UsuarioDAO import UsuarioDAO
from src.model.Servico import Servico
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
        self.preencher_clientes()
        self.preencher_posto(self.comboBoxPosto)
        self.preencher_posto(self.comboBoxPosto_2)
        self.comboBoxPosto_2.currentTextChanged.connect(
            lambda: self.preencher_combustivel(self.comboBoxCombustivel, self.comboBoxPosto_2))
        self.comboBoxPosto.currentTextChanged.connect(
            lambda: self.preencher_combustivel(self.comboBoxCombustivel_2, self.comboBoxPosto))
        self.comboBoxCombustivel_2.currentTextChanged.connect(lambda: self.exibir_preco_servico())
        self.quantidadeSpinBox.valueChanged.connect(lambda: self.exibir_preco_servico())
        self.precoSpinBox.valueChanged.connect(lambda: self.exibir_quantidade_servico())

        # TOGGLE BUTTONS
        self.pushButton_toggle.clicked.connect(self.show_menu)
        self.botaoCadastrarCliente.clicked.connect(self.cadastrar_cliente)
        self.btnVerEstoque.clicked.connect(self.checar_estoque)
        self.btnAbastecerEstoque.clicked.connect(self.abastecer_estoque)
        self.buttonBuscarCliente.clicked.connect(self.buscar_cliente_pela_placa)
        self.buttonVenda.clicked.connect(self.realizar_venda)

        ### Setando as páginas do sistema
        self.pushButtonHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.pushButtonBusca.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_buscarPlaca))
        self.pushButtonVendas.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_vendas))
        self.pushButtonEstoque.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_estoque))
        self.pushButtonCadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrarCliente))

    # MÉTODOS AUXILIARES

    def obter_cliente(self):
        nome = self.campoNomeCadastro.text()
        cpf = self.campoTextoCPF.text()
        data_nascimento = self.dataText.text()
        placa = self.campoPlacaCadastro.text()

        modelo_cliente = Cliente(nome, cpf, data_nascimento, placa)

        return modelo_cliente

    def limpar_tela_cliente(self):
        self.campoNomeCadastro.setText("")
        self.campoTextoCPF.setText("")
        self.campoPlacaCadastro.setText("")

    def preencher_combustivel(self, combustivel_combobox, posto_combobox):
        lista_combustiveis = []
        # limpar combobox de combustivel
        combustivel_combobox.clear()

        # buscar posto selecionado da view
        posto_selecionado = posto_combobox.currentText()

        # validar posto no banco de dados e retornar os dados
        posto_combustivel_dao = PostoCombustivelDAO()

        combustivel_data = posto_combustivel_dao.buscar_combustivel_por_nome(posto_selecionado)

        for item in combustivel_data:
            lista_combustiveis.append(item[0])

        # retornar informação para a view
        combustivel_combobox.addItems(lista_combustiveis)

    def preencher_clientes(self):
        # trazer todos os clientes do banco de dados
        cliente_dao = ClienteDAO()
        lista_clientes = cliente_dao.select_all()

        # selecionar e armazenar o nome de todos os clientes
        nomes = []

        for nome in lista_clientes:
            nomes.append(nome[1])

        # setar os nomes dentro do comboBox
        for item in nomes:
            self.comboBoxCliente.addItem(item)

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

    def remove_repetidos(self, lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        return l

    def preencher_posto(self, element):
        # trazer todos os postos do banco de dados
        posto_combustivel_dao = PostoCombustivelDAO()

        lista_postos = posto_combustivel_dao.select_tabelas_relacionadas()
        lista_nomes = []
        for item in lista_postos:
            lista_nomes.append(item[0])

        lista_nomes_filtrados = self.remove_repetidos(lista_nomes)
        element.addItems(lista_nomes_filtrados)

    def pegar_dados_para_venda(self):
        # pegar dados da view

        cliente = self.comboBoxCliente.currentText()
        posto = self.comboBoxPosto.currentText()
        combustivel = self.comboBoxCombustivel_2.currentText()
        quantidade = self.quantidadeSpinBox.text()
        preco = self.precoSpinBox.value()

        servico = Servico("Abastecer", cliente, posto, combustivel, quantidade, preco)
        return servico

    def limpar_campos_servico(self):
        self.quantidadeSpinBox.setValue(1)
        self.precoSpinBox.setValue(0)

    def exibir_preco_servico(self):
        data = self.pegar_dados_para_venda()
        combustivel_dao = CombustivelDAO()
        combustivel_pesquisado = combustivel_dao.search(data.get_combustivel, type_s="descricao")

        for item in combustivel_pesquisado:
            preco_combustivel = item[3]

        preco_servico = (preco_combustivel * data.get_quantidade)

        preco = "{0:.2f}".format(preco_servico)

        if self.quantidadeSpinBox.value() <= 1:
            self.precoSpinBox.setMinimum(preco_combustivel)

        self.precoSpinBox.setValue(float(preco))

        return preco

    def exibir_quantidade_servico(self):
        data = self.pegar_dados_para_venda()
        combustivel_dao = CombustivelDAO()
        combustivel_pesquisado = combustivel_dao.search(data.get_combustivel, type_s="descricao")
        preco_view = self.precoSpinBox.value()

        for item in combustivel_pesquisado:
            preco_combustivel = item[3]

        quantidade_total = (preco_view / preco_combustivel)

        if preco_view <= 1:
            self.precoSpinBox.setMinimum(preco_combustivel)

        self.quantidadeSpinBox.setValue(quantidade_total)

    # ================== MÉTODOS PRINCIPAIS ==================

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
            self.limpar_tela_cliente()

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

    # Método para buscar cliente pela placa do carro

    def buscar_cliente_pela_placa(self):
        # buscar placa da view
        placa = self.placaText.text()

        # consultar e validar placa no banco de dados
        if placa != "" or placa is not None:
            cliente_dao = ClienteDAO()
            cliente_pesquisado = cliente_dao.search(placa, type_s="placa")

            # retornar informações do cliente ou erro para view de acordo com a placa
            if cliente_pesquisado is not None:
                for item in cliente_pesquisado:
                    nome_cliente = item[1]
                self.clienteText.setText(nome_cliente)
            else:
                QMessageBox.warning(QMessageBox(), "Erro !", "Não existe nenhum cliente com a placa informada !")

    # Método para realizar venda
    def realizar_venda(self):
        # pegar dados da view
        data = self.pegar_dados_para_venda()
        if data is not None:
            if data.get_cliente == '' or data.get_cliente is None or data.get_posto == '' or data.get_posto is None or data.get_combustivel == '' or data.get_combustivel is None or data.get_quantidade is None or data.get_valor is None or data.get_valor == 0:
                QMessageBox.warning(QMessageBox(), "Erro !", "Preencha Todos Os Campos !")
            else:
                # validar os dados existem usando o banco de dados
                cliente_modelo = data.get_cliente
                posto_modelo = data.get_posto
                combustivel_modelo = data.get_combustivel

                cliente_dao = ClienteDAO()
                cliente_pesquisado = cliente_dao.search(cliente_modelo, type_s="nome")

                for item in cliente_pesquisado:
                    id_cliente = item[0]

                posto_combustivel_dao = PostoCombustivelDAO()
                posto_pesquisado = posto_combustivel_dao.search(posto_modelo, combustivel_modelo,
                                                                type_s="nome_combustivel")

                if cliente_pesquisado is not None and posto_pesquisado is not None:
                    for item in posto_pesquisado:
                        id_posto_objeto = item[0]
                        id_combustivel_objeto = item[2]
                        quantidade = item[4]

                    pesquisa_produto_servico = posto_combustivel_dao.search(id_posto_objeto, id_combustivel_objeto, type_s='id_posto_combustivel')

                    for item in pesquisa_produto_servico:
                        id_posto_servico = item[0]
                        id_combustivel_servico = item[2]

                    # Verifica se a quantidade digitada pelo cliente é maior que a quantidade informada pelo banco de dados, se não for, realiza a venda
                    if data.get_quantidade > quantidade:
                        QMessageBox.warning(QMessageBox(), "Erro !",
                                            "Infelizmente Não Temos essa Quantidade em Estoque !")
                    else:
                        # Atualiza quantidade do banco de dados conforme a quantidade vendida
                        combustivel_dao = CombustivelDAO()
                        combustivel_pesquisado = combustivel_dao.search(data.get_combustivel, type_s="descricao")

                        for item in combustivel_pesquisado:
                            id_combustivel = item[0]
                            nome_combustivel = item[1]
                            preco_combustivel = item[3]

                        quantidade_atualizada = (quantidade - data.get_quantidade)
                        combustivel_dao.update(id_combustivel, nome_combustivel, quantidade_atualizada,
                                               preco_combustivel, None)

                        preco_servico = self.exibir_preco_servico()
                        servico_dao = ServicoDAO()
                        servico_dao.insert(data.get_descricao, data.get_quantidade, preco_servico, None, id_cliente,
                                           id_posto_servico)
                        QMessageBox.warning(QMessageBox(), "Sucesso !", "Venda Realizada com Sucesso! Volte Sempre !")
                        self.limpar_campos_servico()

                else:
                    print(f"Erro:", {data})
