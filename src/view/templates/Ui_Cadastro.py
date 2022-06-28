# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastrojTmwPi.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1048, 774)
        MainWindow.setMinimumSize(QSize(500, 700))
        icon = QIcon()
        icon.addFile(u":/icon/imagens/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 35))
        self.top_frame.setStyleSheet(u"background-color: #FF915D;")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame_error = QFrame(self.top_frame)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setMaximumSize(QSize(450, 16777215))
        self.frame_error.setStyleSheet(u"background-color: #170900;\n"
"border-radius: 7px;")
        self.frame_error.setFrameShape(QFrame.NoFrame)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.text_error = QLabel(self.frame_error)
        self.text_error.setObjectName(u"text_error")
        font = QFont()
        font.setFamilies([u"Gilroy-Bold"])
        font.setPointSize(12)
        self.text_error.setFont(font)
        self.text_error.setStyleSheet(u"QLabel{\n"
"color:#D9D9D9;\n"
"}\n"
"")
        self.text_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.text_error)

        self.icon_error = QPushButton(self.frame_error)
        self.icon_error.setObjectName(u"icon_error")
        self.icon_error.setMaximumSize(QSize(20, 20))
        self.icon_error.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon_error.setStyleSheet(u"background-image: url(:/imagens/imagens/x-circle-regular-24 (1).png);\n"
"background-position:center;\n"
"")

        self.horizontalLayout_3.addWidget(self.icon_error)


        self.horizontalLayout_2.addWidget(self.frame_error)


        self.verticalLayout.addWidget(self.top_frame)

        self.container_frame = QFrame(self.centralwidget)
        self.container_frame.setObjectName(u"container_frame")
        self.container_frame.setStyleSheet(u"background-color: #FF915D;")
        self.container_frame.setFrameShape(QFrame.NoFrame)
        self.container_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.container_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.content_frame = QFrame(self.container_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMaximumSize(QSize(550, 600))
        self.content_frame.setStyleSheet(u"background-color:#170900;\n"
"border-radius:10px;\n"
"box-shadow: 10px 10px 21px -7px rgba(0,0,0,0.61);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.content_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(170, 10, 210, 150))
        self.logo.setStyleSheet(u"background-image: url(:/imagens/imagens/logo_250.png);\n"
"background-repeat: no-repeat;\n"
"background-position:center;\n"
"")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.lineEdit_nome = QLineEdit(self.content_frame)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(135, 200, 280, 50))
        font1 = QFont()
        font1.setFamilies([u"Gilroy-Regular"])
        font1.setPointSize(11)
        self.lineEdit_nome.setFont(font1)
        self.lineEdit_nome.setStyleSheet(u"QLineEdit{\n"
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
        self.lineEdit_nome.setMaxLength(80)
        self.lineEdit_cpf = QLineEdit(self.content_frame)
        self.lineEdit_cpf.setObjectName(u"lineEdit_cpf")
        self.lineEdit_cpf.setGeometry(QRect(135, 260, 280, 50))
        self.lineEdit_cpf.setFont(font1)
        self.lineEdit_cpf.setStyleSheet(u"QLineEdit{\n"
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
        self.lineEdit_cpf.setMaxLength(11)
        self.lineEdit_senha = QLineEdit(self.content_frame)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(135, 320, 280, 50))
        self.lineEdit_senha.setFont(font1)
        self.lineEdit_senha.setStyleSheet(u"QLineEdit{\n"
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
        self.lineEdit_senha.setMaxLength(16)
        self.lineEdit_senha.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.content_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(135, 460, 280, 50))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 25px;\n"
"	color: #FFBD59;\n"
"	font: 14pt \"Gilroy-Bold\";\n"
"	transition:1s;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")
        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(110, 530, 330, 31))
        self.frame_2.setMinimumSize(QSize(330, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 25))
        self.label.setMaximumSize(QSize(165, 16777215))
        self.label.setStyleSheet(u"QLabel{\n"
"	color:#A6A6A6;\n"
"	font: 11pt \"Gilroy-Regular\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton_login = QPushButton(self.frame_2)
        self.pushButton_login.setObjectName(u"pushButton_login")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        self.pushButton_login.setMinimumSize(QSize(140, 20))
        self.pushButton_login.setMaximumSize(QSize(145, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Gilroy-Bold"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton_login.setFont(font2)
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: 2px solid #FFBD59;\n"
"	border-radius: 10px;\n"
"	color: #FFBD59;\n"
"	font: 11pt \"Gilroy-Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FFBD59;\n"
"	color: #170900;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_login)

        self.dataNascimento = QDateEdit(self.content_frame)
        self.dataNascimento.setObjectName(u"dataNascimento")
        self.dataNascimento.setGeometry(QRect(135, 380, 280, 50))
        self.dataNascimento.setStyleSheet(u"font: 12pt \"Gilroy-Medium\";\n"
"color: #D9D9D9;\n"
"border: 1px solid #D9D9D9;")
        self.dataNascimento.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self.container_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMaximumSize(QSize(16777215, 35))
        self.bottom_frame.setStyleSheet(u"background-color: #FF915D;")
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoTech - Cadastro", None))
        self.text_error.setText(QCoreApplication.translate("MainWindow", u"Algum campo est\u00e1 inv\u00e1lido ou vazio", None))
        self.icon_error.setText("")
        self.lineEdit_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.lineEdit_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cpf", None))
        self.lineEdit_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"J\u00e1 possui uma conta?", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Fazer Login", None))
        self.dataNascimento.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
    # retranslateUi

