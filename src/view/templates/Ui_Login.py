# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginKUOCSU.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QSize(500, 700))
        icon = QIcon()
        icon.addFile(u":/icon/imagens/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 700))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 35))
        self.top_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.top_frame.setStyleSheet(u"background-color:#FF915D;")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.frame_4 = QFrame(self.top_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setStyleSheet(u"background-color: #170900;\n"
"border-radius: 7px;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.label_error = QLabel(self.frame_4)
        self.label_error.setObjectName(u"label_error")
        font = QFont()
        font.setFamilies([u"Gilroy-Bold"])
        font.setPointSize(12)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet(u"color:#D9D9D9;")
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close = QPushButton(self.frame_4)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"background-image: url(:/imagens/imagens/x-circle-regular-24 (1).png);\n"
"background-position:center;\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_close)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.top_frame)

        self.container_frame = QFrame(self.centralwidget)
        self.container_frame.setObjectName(u"container_frame")
        self.container_frame.setStyleSheet(u"background-color:#FF915D;")
        self.container_frame.setFrameShape(QFrame.NoFrame)
        self.container_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.content = QFrame(self.container_frame)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(450, 550))
        self.content.setStyleSheet(u"background-color: #170900;\n"
"border-radius:10px;\n"
"box-shadow: 10px 10px 21px -7px rgba(0,0,0,0.61);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.content)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(100, 60, 250, 250))
        self.logo.setStyleSheet(u"background-image: url(:/imagens/imagens/logo_250.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.lineEdit_usuario = QLineEdit(self.content)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        self.lineEdit_usuario.setGeometry(QRect(85, 310, 280, 50))
        font1 = QFont()
        font1.setFamilies([u"Gilroy-Regular"])
        font1.setPointSize(11)
        self.lineEdit_usuario.setFont(font1)
        self.lineEdit_usuario.setStyleSheet(u"QLineEdit{\n"
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
        self.lineEdit_usuario.setMaxLength(11)
        self.lineEdit_senha = QLineEdit(self.content)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(85, 370, 280, 50))
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
        self.pushButton_login = QPushButton(self.content)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(85, 440, 280, 50))
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.setStyleSheet(u"QPushButton{\n"
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
        self.frame = QFrame(self.content)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 500, 330, 30))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(160, 25))
        self.label.setStyleSheet(u"QLabel{\n"
"	color:#A6A6A6;\n"
"	font: 11pt \"Gilroy-Regular\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton_cadastro = QPushButton(self.frame)
        self.pushButton_cadastro.setObjectName(u"pushButton_cadastro")
        self.pushButton_cadastro.setMinimumSize(QSize(146, 20))
        self.pushButton_cadastro.setMaximumSize(QSize(150, 16777215))
        self.pushButton_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cadastro.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_4.addWidget(self.pushButton_cadastro)


        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.container_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMaximumSize(QSize(16777215, 35))
        self.bottom_frame.setStyleSheet(u"background-color:#FF915D;")
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoTech - Login", None))
        self.label_error.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio ou senha inv\u00e1lidos", None))
        self.pushButton_close.setText("")
        self.lineEdit_usuario.setText("")
        self.lineEdit_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cpf", None))
        self.lineEdit_senha.setText("")
        self.lineEdit_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ainda n\u00e3o tem conta?", None))
        self.pushButton_cadastro.setText(QCoreApplication.translate("MainWindow", u"Fazer Cadastro", None))
    # retranslateUi

