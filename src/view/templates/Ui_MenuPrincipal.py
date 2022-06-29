# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuPrincipalakhwZX.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"background-color:#170900;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #D9D9D9;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(9, 16777215))
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.leftMenu)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMaximumSize(QSize(105, 16777215))
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.buttonsContainer = QFrame(self.leftFrame)
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsContainer.sizePolicy().hasHeightForWidth())
        self.buttonsContainer.setSizePolicy(sizePolicy)
        self.buttonsContainer.setMinimumSize(QSize(70, 0))
        self.buttonsContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.buttonsContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.buttons_wrapper = QFrame(self.buttonsContainer)
        self.buttons_wrapper.setObjectName(u"buttons_wrapper")
        self.buttons_wrapper.setMaximumSize(QSize(100, 16777215))
        self.buttons_wrapper.setFrameShape(QFrame.StyledPanel)
        self.buttons_wrapper.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.buttons_wrapper)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButtonHome = QPushButton(self.buttons_wrapper)
        self.pushButtonHome.setObjectName(u"pushButtonHome")
        self.pushButtonHome.setMinimumSize(QSize(96, 35))
        self.pushButtonHome.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonHome.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	color: #FFBD59;\n"
"	font: 11pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/imagens/imagens/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHome.setIcon(icon)
        self.pushButtonHome.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.pushButtonHome)

        self.pushButtonCadastro = QPushButton(self.buttons_wrapper)
        self.pushButtonCadastro.setObjectName(u"pushButtonCadastro")
        self.pushButtonCadastro.setMinimumSize(QSize(96, 35))
        self.pushButtonCadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonCadastro.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	color: #FFBD59;\n"
"	font: 11pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/imagens/imagens/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCadastro.setIcon(icon1)
        self.pushButtonCadastro.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.pushButtonCadastro)

        self.pushButtonEstoque = QPushButton(self.buttons_wrapper)
        self.pushButtonEstoque.setObjectName(u"pushButtonEstoque")
        self.pushButtonEstoque.setMinimumSize(QSize(96, 35))
        self.pushButtonEstoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonEstoque.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	color: #FFBD59;\n"
"	font: 11pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/imagens/imagens/estoque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonEstoque.setIcon(icon2)
        self.pushButtonEstoque.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.pushButtonEstoque)

        self.pushButtonBusca = QPushButton(self.buttons_wrapper)
        self.pushButtonBusca.setObjectName(u"pushButtonBusca")
        self.pushButtonBusca.setMinimumSize(QSize(96, 35))
        self.pushButtonBusca.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonBusca.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	color: #FFBD59;\n"
"	font: 11pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/imagens/imagens/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonBusca.setIcon(icon3)
        self.pushButtonBusca.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.pushButtonBusca)

        self.pushButtonVendas = QPushButton(self.buttons_wrapper)
        self.pushButtonVendas.setObjectName(u"pushButtonVendas")
        self.pushButtonVendas.setMinimumSize(QSize(96, 35))
        self.pushButtonVendas.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonVendas.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	color: #FFBD59;\n"
"	font: 11pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/imagens/imagens/vendas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonVendas.setIcon(icon4)
        self.pushButtonVendas.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.pushButtonVendas)


        self.verticalLayout_5.addWidget(self.buttons_wrapper)


        self.verticalLayout_3.addWidget(self.buttonsContainer)


        self.verticalLayout_2.addWidget(self.leftFrame)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QFrame(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setFrameShape(QFrame.StyledPanel)
        self.mainBody.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.mainBody)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_toggle = QPushButton(self.header)
        self.pushButton_toggle.setObjectName(u"pushButton_toggle")
        self.pushButton_toggle.setMinimumSize(QSize(16, 50))
        self.pushButton_toggle.setMaximumSize(QSize(48, 50))
        self.pushButton_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/imagens/imagens/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_toggle.setIcon(icon5)
        self.pushButton_toggle.setIconSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.pushButton_toggle)

        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"color: rgb(217, 217, 217);\n"
"font: 12pt \"Gilroy-Medium\";")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title)


        self.verticalLayout.addWidget(self.header)

        self.main_frame = QFrame(self.mainBody)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_14 = QVBoxLayout(self.pg_home)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 0, 0, 0)
        self.logo = QFrame(self.pg_home)
        self.logo.setObjectName(u"logo")
        font = QFont()
        font.setFamilies([u"Gilroy-Bold"])
        font.setPointSize(10)
        self.logo.setFont(font)
        self.logo.setStyleSheet(u"background-image: url(:/imagens/imagens/logo_mini.png);\n"
"background-repeat: no-repeat;\n"
"background-position:center;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.logo)

        self.campoUsuario = QFrame(self.pg_home)
        self.campoUsuario.setObjectName(u"campoUsuario")
        self.campoUsuario.setFrameShape(QFrame.StyledPanel)
        self.campoUsuario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.campoUsuario)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.nomeUsuarioText = QLabel(self.campoUsuario)
        self.nomeUsuarioText.setObjectName(u"nomeUsuarioText")
        self.nomeUsuarioText.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_3.addWidget(self.nomeUsuarioText)

        self.nomeUsuarioLogado = QLineEdit(self.campoUsuario)
        self.nomeUsuarioLogado.setObjectName(u"nomeUsuarioLogado")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nomeUsuarioLogado.sizePolicy().hasHeightForWidth())
        self.nomeUsuarioLogado.setSizePolicy(sizePolicy1)
        self.nomeUsuarioLogado.setMinimumSize(QSize(0, 40))
        self.nomeUsuarioLogado.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.nomeUsuarioLogado.setAlignment(Qt.AlignCenter)
        self.nomeUsuarioLogado.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.nomeUsuarioLogado)


        self.verticalLayout_14.addWidget(self.campoUsuario)

        self.campoCpf = QFrame(self.pg_home)
        self.campoCpf.setObjectName(u"campoCpf")
        self.campoCpf.setFrameShape(QFrame.StyledPanel)
        self.campoCpf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.campoCpf)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cpfText = QLabel(self.campoCpf)
        self.cpfText.setObjectName(u"cpfText")
        self.cpfText.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.cpfText)

        self.cpfUsuarioLogado = QLineEdit(self.campoCpf)
        self.cpfUsuarioLogado.setObjectName(u"cpfUsuarioLogado")
        self.cpfUsuarioLogado.setMinimumSize(QSize(0, 40))
        self.cpfUsuarioLogado.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.cpfUsuarioLogado.setAlignment(Qt.AlignCenter)
        self.cpfUsuarioLogado.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.cpfUsuarioLogado)


        self.verticalLayout_14.addWidget(self.campoCpf)

        self.campoStatus = QFrame(self.pg_home)
        self.campoStatus.setObjectName(u"campoStatus")
        self.campoStatus.setFrameShape(QFrame.StyledPanel)
        self.campoStatus.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.campoStatus)
        self.horizontalLayout_21.setSpacing(9)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.statusText = QLabel(self.campoStatus)
        self.statusText.setObjectName(u"statusText")
        self.statusText.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_21.addWidget(self.statusText)

        self.campoStatusLogado = QLineEdit(self.campoStatus)
        self.campoStatusLogado.setObjectName(u"campoStatusLogado")
        self.campoStatusLogado.setMinimumSize(QSize(0, 40))
        self.campoStatusLogado.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.campoStatusLogado.setAlignment(Qt.AlignCenter)
        self.campoStatusLogado.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.campoStatusLogado)


        self.verticalLayout_14.addWidget(self.campoStatus)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrarCliente = QWidget()
        self.pg_cadastrarCliente.setObjectName(u"pg_cadastrarCliente")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrarCliente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.container = QFrame(self.pg_cadastrarCliente)
        self.container.setObjectName(u"container")
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.campoNome = QFrame(self.container)
        self.campoNome.setObjectName(u"campoNome")
        self.campoNome.setFrameShape(QFrame.StyledPanel)
        self.campoNome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.campoNome)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.nomeTitulo = QLabel(self.campoNome)
        self.nomeTitulo.setObjectName(u"nomeTitulo")
        self.nomeTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_5.addWidget(self.nomeTitulo)

        self.campoNomeCadastro = QLineEdit(self.campoNome)
        self.campoNomeCadastro.setObjectName(u"campoNomeCadastro")
        self.campoNomeCadastro.setMinimumSize(QSize(0, 40))
        self.campoNomeCadastro.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.campoNomeCadastro.setMaxLength(80)

        self.horizontalLayout_5.addWidget(self.campoNomeCadastro)


        self.verticalLayout_9.addWidget(self.campoNome)

        self.campoCPF = QFrame(self.container)
        self.campoCPF.setObjectName(u"campoCPF")
        self.campoCPF.setFrameShape(QFrame.StyledPanel)
        self.campoCPF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.campoCPF)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cpfTitulo = QLabel(self.campoCPF)
        self.cpfTitulo.setObjectName(u"cpfTitulo")
        self.cpfTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_6.addWidget(self.cpfTitulo)

        self.campoTextoCPF = QLineEdit(self.campoCPF)
        self.campoTextoCPF.setObjectName(u"campoTextoCPF")
        self.campoTextoCPF.setMinimumSize(QSize(0, 40))
        self.campoTextoCPF.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.campoTextoCPF.setMaxLength(11)

        self.horizontalLayout_6.addWidget(self.campoTextoCPF)


        self.verticalLayout_9.addWidget(self.campoCPF)

        self.campoData = QFrame(self.container)
        self.campoData.setObjectName(u"campoData")
        self.campoData.setFrameShape(QFrame.StyledPanel)
        self.campoData.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.campoData)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dataTitulo = QLabel(self.campoData)
        self.dataTitulo.setObjectName(u"dataTitulo")
        self.dataTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_7.addWidget(self.dataTitulo)

        self.dataText = QDateEdit(self.campoData)
        self.dataText.setObjectName(u"dataText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dataText.sizePolicy().hasHeightForWidth())
        self.dataText.setSizePolicy(sizePolicy2)
        self.dataText.setMinimumSize(QSize(0, 40))
        self.dataText.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"color: #D9D9D9;\n"
"border: 1px solid #D9D9D9;")
        self.dataText.setReadOnly(False)
        self.dataText.setMaximumDateTime(QDateTime(QDate(2023, 1, 1), QTime(23, 59, 59)))
        self.dataText.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dataText.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.dataText)


        self.verticalLayout_9.addWidget(self.campoData)

        self.campoPlaca = QFrame(self.container)
        self.campoPlaca.setObjectName(u"campoPlaca")
        self.campoPlaca.setFrameShape(QFrame.StyledPanel)
        self.campoPlaca.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.campoPlaca)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.placaTitulo = QLabel(self.campoPlaca)
        self.placaTitulo.setObjectName(u"placaTitulo")
        self.placaTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_8.addWidget(self.placaTitulo)

        self.campoPlacaCadastro = QLineEdit(self.campoPlaca)
        self.campoPlacaCadastro.setObjectName(u"campoPlacaCadastro")
        self.campoPlacaCadastro.setMinimumSize(QSize(0, 40))
        self.campoPlacaCadastro.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}\n"
"")
        self.campoPlacaCadastro.setMaxLength(7)

        self.horizontalLayout_8.addWidget(self.campoPlacaCadastro)


        self.verticalLayout_9.addWidget(self.campoPlaca)


        self.verticalLayout_7.addWidget(self.container)

        self.btnWrapper = QFrame(self.pg_cadastrarCliente)
        self.btnWrapper.setObjectName(u"btnWrapper")
        self.btnWrapper.setMinimumSize(QSize(0, 75))
        self.btnWrapper.setFrameShape(QFrame.StyledPanel)
        self.btnWrapper.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.btnWrapper)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.botaoCadastrarCliente = QPushButton(self.btnWrapper)
        self.botaoCadastrarCliente.setObjectName(u"botaoCadastrarCliente")
        self.botaoCadastrarCliente.setMinimumSize(QSize(0, 50))
        self.botaoCadastrarCliente.setMaximumSize(QSize(280, 16777215))
        self.botaoCadastrarCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.botaoCadastrarCliente.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 25px;\n"
"	color: #FFBD59;\n"
"	font: 14pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")

        self.horizontalLayout_22.addWidget(self.botaoCadastrarCliente)


        self.verticalLayout_7.addWidget(self.btnWrapper)

        self.Pages.addWidget(self.pg_cadastrarCliente)
        self.pg_estoque = QWidget()
        self.pg_estoque.setObjectName(u"pg_estoque")
        self.verticalLayout_10 = QVBoxLayout(self.pg_estoque)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.campoPosto_2 = QFrame(self.pg_estoque)
        self.campoPosto_2.setObjectName(u"campoPosto_2")
        self.campoPosto_2.setFrameShape(QFrame.StyledPanel)
        self.campoPosto_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.campoPosto_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.postoTitulo_2 = QLabel(self.campoPosto_2)
        self.postoTitulo_2.setObjectName(u"postoTitulo_2")
        self.postoTitulo_2.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_23.addWidget(self.postoTitulo_2)

        self.comboBoxPosto_2 = QComboBox(self.campoPosto_2)
        self.comboBoxPosto_2.setObjectName(u"comboBoxPosto_2")
        sizePolicy2.setHeightForWidth(self.comboBoxPosto_2.sizePolicy().hasHeightForWidth())
        self.comboBoxPosto_2.setSizePolicy(sizePolicy2)
        self.comboBoxPosto_2.setMinimumSize(QSize(0, 40))
        self.comboBoxPosto_2.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"border: 1px solid #FF915D;\n"
"color: #D9D9D9;")

        self.horizontalLayout_23.addWidget(self.comboBoxPosto_2)


        self.verticalLayout_10.addWidget(self.campoPosto_2)

        self.campoCombustivel = QFrame(self.pg_estoque)
        self.campoCombustivel.setObjectName(u"campoCombustivel")
        self.campoCombustivel.setCursor(QCursor(Qt.ArrowCursor))
        self.campoCombustivel.setFrameShape(QFrame.StyledPanel)
        self.campoCombustivel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.campoCombustivel)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 10, 0)
        self.combustivelTitulo = QLabel(self.campoCombustivel)
        self.combustivelTitulo.setObjectName(u"combustivelTitulo")
        self.combustivelTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_11.addWidget(self.combustivelTitulo)

        self.comboBoxCombustivel = QComboBox(self.campoCombustivel)
        self.comboBoxCombustivel.setObjectName(u"comboBoxCombustivel")
        sizePolicy2.setHeightForWidth(self.comboBoxCombustivel.sizePolicy().hasHeightForWidth())
        self.comboBoxCombustivel.setSizePolicy(sizePolicy2)
        self.comboBoxCombustivel.setMinimumSize(QSize(0, 40))
        self.comboBoxCombustivel.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"border: 1px solid #FF915D;\n"
"color: #D9D9D9;")

        self.horizontalLayout_11.addWidget(self.comboBoxCombustivel)


        self.verticalLayout_10.addWidget(self.campoCombustivel)

        self.campoQuantidade = QFrame(self.pg_estoque)
        self.campoQuantidade.setObjectName(u"campoQuantidade")
        self.campoQuantidade.setFrameShape(QFrame.StyledPanel)
        self.campoQuantidade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.campoQuantidade)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.quantidadeTitulo = QLabel(self.campoQuantidade)
        self.quantidadeTitulo.setObjectName(u"quantidadeTitulo")
        self.quantidadeTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.quantidadeTitulo)

        self.doubleSpinBox = QDoubleSpinBox(self.campoQuantidade)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy2)
        self.doubleSpinBox.setMinimumSize(QSize(0, 40))
        self.doubleSpinBox.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"color: #D9D9D9;\n"
"border: 1px solid #D9D9D9;")
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setMaximum(50000.000000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox)

        self.textLitros = QLabel(self.campoQuantidade)
        self.textLitros.setObjectName(u"textLitros")
        self.textLitros.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 12pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.textLitros)


        self.verticalLayout_10.addWidget(self.campoQuantidade)

        self.btnContainer = QFrame(self.pg_estoque)
        self.btnContainer.setObjectName(u"btnContainer")
        self.btnContainer.setFrameShape(QFrame.StyledPanel)
        self.btnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.btnContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btnAbastecerEstoque = QPushButton(self.btnContainer)
        self.btnAbastecerEstoque.setObjectName(u"btnAbastecerEstoque")
        self.btnAbastecerEstoque.setMinimumSize(QSize(0, 50))
        self.btnAbastecerEstoque.setMaximumSize(QSize(280, 16777215))
        self.btnAbastecerEstoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAbastecerEstoque.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 25px;\n"
"	color: #FFBD59;\n"
"	font: 14pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btnAbastecerEstoque)

        self.btnVerEstoque = QPushButton(self.btnContainer)
        self.btnVerEstoque.setObjectName(u"btnVerEstoque")
        self.btnVerEstoque.setMinimumSize(QSize(0, 50))
        self.btnVerEstoque.setMaximumSize(QSize(280, 16777215))
        self.btnVerEstoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVerEstoque.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 25px;\n"
"	color: #FFBD59;\n"
"	font: 14pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btnVerEstoque)


        self.verticalLayout_10.addWidget(self.btnContainer)

        self.Pages.addWidget(self.pg_estoque)
        self.pg_buscarPlaca = QWidget()
        self.pg_buscarPlaca.setObjectName(u"pg_buscarPlaca")
        self.verticalLayout_11 = QVBoxLayout(self.pg_buscarPlaca)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.campoPlaca_2 = QFrame(self.pg_buscarPlaca)
        self.campoPlaca_2.setObjectName(u"campoPlaca_2")
        self.campoPlaca_2.setFrameShape(QFrame.StyledPanel)
        self.campoPlaca_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.campoPlaca_2)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, -1, 0)
        self.placaTitulo_2 = QLabel(self.campoPlaca_2)
        self.placaTitulo_2.setObjectName(u"placaTitulo_2")
        self.placaTitulo_2.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.placaTitulo_2)

        self.placaText = QLineEdit(self.campoPlaca_2)
        self.placaText.setObjectName(u"placaText")
        self.placaText.setMinimumSize(QSize(0, 40))
        self.placaText.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.placaText.setMaxLength(7)
        self.placaText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.placaText)


        self.verticalLayout_11.addWidget(self.campoPlaca_2)

        self.campoCliente = QFrame(self.pg_buscarPlaca)
        self.campoCliente.setObjectName(u"campoCliente")
        self.campoCliente.setFrameShape(QFrame.StyledPanel)
        self.campoCliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.campoCliente)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, -1, 0)
        self.clienteTitulo = QLabel(self.campoCliente)
        self.clienteTitulo.setObjectName(u"clienteTitulo")
        self.clienteTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_14.addWidget(self.clienteTitulo)

        self.clienteText = QLineEdit(self.campoCliente)
        self.clienteText.setObjectName(u"clienteText")
        self.clienteText.setMinimumSize(QSize(0, 40))
        self.clienteText.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"Gilroy-Medium\";\n"
"	background-color: transparent;\n"
"	color: #AAAAAA;\n"
"	background-color: #170900;\n"
"	border:1px solid #A6A6A6;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #DADADA;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 2px solid #FFBD59;\n"
"}")
        self.clienteText.setMaxLength(80)
        self.clienteText.setAlignment(Qt.AlignCenter)
        self.clienteText.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.clienteText)


        self.verticalLayout_11.addWidget(self.campoCliente)

        self.buttonContainer = QFrame(self.pg_buscarPlaca)
        self.buttonContainer.setObjectName(u"buttonContainer")
        self.buttonContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.buttonContainer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.buttonBuscarCliente = QPushButton(self.buttonContainer)
        self.buttonBuscarCliente.setObjectName(u"buttonBuscarCliente")
        self.buttonBuscarCliente.setMinimumSize(QSize(0, 50))
        self.buttonBuscarCliente.setMaximumSize(QSize(280, 16777215))
        self.buttonBuscarCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBuscarCliente.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 25px;\n"
"	color: #FFBD59;\n"
"	font: 14pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")

        self.horizontalLayout_12.addWidget(self.buttonBuscarCliente)


        self.verticalLayout_11.addWidget(self.buttonContainer)

        self.Pages.addWidget(self.pg_buscarPlaca)
        self.pg_vendas = QWidget()
        self.pg_vendas.setObjectName(u"pg_vendas")
        self.verticalLayout_12 = QVBoxLayout(self.pg_vendas)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.campoCliente_2 = QFrame(self.pg_vendas)
        self.campoCliente_2.setObjectName(u"campoCliente_2")
        self.campoCliente_2.setFrameShape(QFrame.StyledPanel)
        self.campoCliente_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.campoCliente_2)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 9, 0)
        self.clienteTitulo_2 = QLabel(self.campoCliente_2)
        self.clienteTitulo_2.setObjectName(u"clienteTitulo_2")
        self.clienteTitulo_2.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_15.addWidget(self.clienteTitulo_2)

        self.comboBoxCliente = QComboBox(self.campoCliente_2)
        self.comboBoxCliente.setObjectName(u"comboBoxCliente")
        sizePolicy2.setHeightForWidth(self.comboBoxCliente.sizePolicy().hasHeightForWidth())
        self.comboBoxCliente.setSizePolicy(sizePolicy2)
        self.comboBoxCliente.setMinimumSize(QSize(0, 40))
        self.comboBoxCliente.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"border: 1px solid #FF915D;\n"
"color: #D9D9D9;")

        self.horizontalLayout_15.addWidget(self.comboBoxCliente)


        self.verticalLayout_12.addWidget(self.campoCliente_2)

        self.campoPosto = QFrame(self.pg_vendas)
        self.campoPosto.setObjectName(u"campoPosto")
        self.campoPosto.setFrameShape(QFrame.StyledPanel)
        self.campoPosto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.campoPosto)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, -1, 0)
        self.postoTitulo = QLabel(self.campoPosto)
        self.postoTitulo.setObjectName(u"postoTitulo")
        self.postoTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_16.addWidget(self.postoTitulo)

        self.comboBoxPosto = QComboBox(self.campoPosto)
        self.comboBoxPosto.setObjectName(u"comboBoxPosto")
        sizePolicy2.setHeightForWidth(self.comboBoxPosto.sizePolicy().hasHeightForWidth())
        self.comboBoxPosto.setSizePolicy(sizePolicy2)
        self.comboBoxPosto.setMinimumSize(QSize(0, 40))
        self.comboBoxPosto.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"border: 1px solid #FF915D;\n"
"color: #D9D9D9;")

        self.horizontalLayout_16.addWidget(self.comboBoxPosto)


        self.verticalLayout_12.addWidget(self.campoPosto)

        self.campoCombustivel_2 = QFrame(self.pg_vendas)
        self.campoCombustivel_2.setObjectName(u"campoCombustivel_2")
        self.campoCombustivel_2.setFrameShape(QFrame.StyledPanel)
        self.campoCombustivel_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.campoCombustivel_2)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, 0)
        self.combustivelTitulo_2 = QLabel(self.campoCombustivel_2)
        self.combustivelTitulo_2.setObjectName(u"combustivelTitulo_2")
        self.combustivelTitulo_2.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_17.addWidget(self.combustivelTitulo_2)

        self.comboBoxCombustivel_2 = QComboBox(self.campoCombustivel_2)
        self.comboBoxCombustivel_2.setObjectName(u"comboBoxCombustivel_2")
        sizePolicy2.setHeightForWidth(self.comboBoxCombustivel_2.sizePolicy().hasHeightForWidth())
        self.comboBoxCombustivel_2.setSizePolicy(sizePolicy2)
        self.comboBoxCombustivel_2.setMinimumSize(QSize(0, 40))
        self.comboBoxCombustivel_2.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"border: 1px solid #FF915D;\n"
"color: #D9D9D9;")

        self.horizontalLayout_17.addWidget(self.comboBoxCombustivel_2)


        self.verticalLayout_12.addWidget(self.campoCombustivel_2)

        self.campoQuantidade_2 = QFrame(self.pg_vendas)
        self.campoQuantidade_2.setObjectName(u"campoQuantidade_2")
        self.campoQuantidade_2.setFrameShape(QFrame.StyledPanel)
        self.campoQuantidade_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.campoQuantidade_2)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, -1, 0)
        self.quantidadeTitulo_2 = QLabel(self.campoQuantidade_2)
        self.quantidadeTitulo_2.setObjectName(u"quantidadeTitulo_2")
        self.quantidadeTitulo_2.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_18.addWidget(self.quantidadeTitulo_2)

        self.quantidadeSpinBox = QDoubleSpinBox(self.campoQuantidade_2)
        self.quantidadeSpinBox.setObjectName(u"quantidadeSpinBox")
        sizePolicy2.setHeightForWidth(self.quantidadeSpinBox.sizePolicy().hasHeightForWidth())
        self.quantidadeSpinBox.setSizePolicy(sizePolicy2)
        self.quantidadeSpinBox.setMinimumSize(QSize(0, 40))
        self.quantidadeSpinBox.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"color: #D9D9D9;\n"
"border: 1px solid #D9D9D9;")
        self.quantidadeSpinBox.setAlignment(Qt.AlignCenter)
        self.quantidadeSpinBox.setMinimum(1.000000000000000)
        self.quantidadeSpinBox.setMaximum(50000.000000000000000)
        self.quantidadeSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_18.addWidget(self.quantidadeSpinBox)

        self.textLitros_2 = QLabel(self.campoQuantidade_2)
        self.textLitros_2.setObjectName(u"textLitros_2")
        self.textLitros_2.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 11pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_18.addWidget(self.textLitros_2)


        self.verticalLayout_12.addWidget(self.campoQuantidade_2)

        self.campoPreco = QFrame(self.pg_vendas)
        self.campoPreco.setObjectName(u"campoPreco")
        self.campoPreco.setFrameShape(QFrame.StyledPanel)
        self.campoPreco.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.campoPreco)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, -1, 0)
        self.precoTitulo = QLabel(self.campoPreco)
        self.precoTitulo.setObjectName(u"precoTitulo")
        self.precoTitulo.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 16pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_19.addWidget(self.precoTitulo)

        self.textReais = QLabel(self.campoPreco)
        self.textReais.setObjectName(u"textReais")
        self.textReais.setStyleSheet(u"QLabel{\n"
"	color:#FF915D;\n"
"	font: 11pt \"Gilroy-SemiBold\";\n"
"}")

        self.horizontalLayout_19.addWidget(self.textReais)

        self.precoSpinBox = QDoubleSpinBox(self.campoPreco)
        self.precoSpinBox.setObjectName(u"precoSpinBox")
        sizePolicy2.setHeightForWidth(self.precoSpinBox.sizePolicy().hasHeightForWidth())
        self.precoSpinBox.setSizePolicy(sizePolicy2)
        self.precoSpinBox.setMinimumSize(QSize(0, 40))
        self.precoSpinBox.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"color: #D9D9D9;\n"
"border: 1px solid #D9D9D9;")
        self.precoSpinBox.setAlignment(Qt.AlignCenter)
        self.precoSpinBox.setMaximum(200000.000000000000000)
        self.precoSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_19.addWidget(self.precoSpinBox)


        self.verticalLayout_12.addWidget(self.campoPreco)

        self.buttonContainer_2 = QFrame(self.pg_vendas)
        self.buttonContainer_2.setObjectName(u"buttonContainer_2")
        self.buttonContainer_2.setFrameShape(QFrame.StyledPanel)
        self.buttonContainer_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.buttonContainer_2)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.buttonVenda = QPushButton(self.buttonContainer_2)
        self.buttonVenda.setObjectName(u"buttonVenda")
        self.buttonVenda.setMinimumSize(QSize(0, 50))
        self.buttonVenda.setMaximumSize(QSize(280, 16777215))
        self.buttonVenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonVenda.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 25px;\n"
"	color: #FFBD59;\n"
"	font: 14pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")

        self.horizontalLayout_20.addWidget(self.buttonVenda)


        self.verticalLayout_12.addWidget(self.buttonContainer_2)

        self.Pages.addWidget(self.pg_vendas)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer = QFrame(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 30))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.footer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButtonCadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.pushButtonEstoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.pushButtonBusca.setText(QCoreApplication.translate("MainWindow", u"Busca", None))
        self.pushButtonVendas.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.pushButton_toggle.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Auto Tech - Sistema de Gerenciamento de Posto", None))
        self.nomeUsuarioText.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.cpfText.setText(QCoreApplication.translate("MainWindow", u"Cpf:", None))
        self.statusText.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.nomeTitulo.setText(QCoreApplication.translate("MainWindow", u"Nome Completo:", None))
        self.cpfTitulo.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.dataTitulo.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento:", None))
        self.dataText.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.placaTitulo.setText(QCoreApplication.translate("MainWindow", u"Placa:", None))
        self.botaoCadastrarCliente.setText(QCoreApplication.translate("MainWindow", u"CadastrarCliente", None))
        self.postoTitulo_2.setText(QCoreApplication.translate("MainWindow", u"Posto:", None))
        self.combustivelTitulo.setText(QCoreApplication.translate("MainWindow", u"Combustivel:", None))
        self.quantidadeTitulo.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.textLitros.setText(QCoreApplication.translate("MainWindow", u"Litros", None))
        self.btnAbastecerEstoque.setText(QCoreApplication.translate("MainWindow", u"Abastecer Estoque", None))
        self.btnVerEstoque.setText(QCoreApplication.translate("MainWindow", u"Ver Estoque", None))
        self.placaTitulo_2.setText(QCoreApplication.translate("MainWindow", u"Placa:", None))
        self.clienteTitulo.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.buttonBuscarCliente.setText(QCoreApplication.translate("MainWindow", u"Buscar Cliente", None))
        self.clienteTitulo_2.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.postoTitulo.setText(QCoreApplication.translate("MainWindow", u"Posto:", None))
        self.combustivelTitulo_2.setText(QCoreApplication.translate("MainWindow", u"Combustivel:", None))
        self.quantidadeTitulo_2.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.textLitros_2.setText(QCoreApplication.translate("MainWindow", u"Litros", None))
        self.precoTitulo.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o:", None))
        self.textReais.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.buttonVenda.setText(QCoreApplication.translate("MainWindow", u"Realizar Venda", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AutoTech - All Rights Reserved", None))
    # retranslateUi

