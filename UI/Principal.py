# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrincipalScreen(object):
    def setupUi(self, PrincipalScreen):
        PrincipalScreen.setObjectName("PrincipalScreen")
        PrincipalScreen.resize(881, 600)
        self.centralwidget = QtWidgets.QWidget(PrincipalScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(46, 194, 126);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnUser = QtWidgets.QPushButton(self.frame_2)
        self.btnUser.setGeometry(QtCore.QRect(90, 0, 91, 51))
        self.btnUser.setStyleSheet("background-color: rgb(62, 63, 64);\n"
"color: rgb(252, 254, 255);")
        self.btnUser.setObjectName("btnUser")
        self.btnLeito = QtWidgets.QPushButton(self.frame_2)
        self.btnLeito.setGeometry(QtCore.QRect(0, 0, 91, 51))
        self.btnLeito.setStyleSheet("background-color: rgb(62, 63, 64);\n"
"color: rgb(252, 254, 255);")
        self.btnLeito.setObjectName("btnLeito")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.paginas = QtWidgets.QStackedWidget(self.frame_3)
        self.paginas.setObjectName("paginas")
        self.cadastrarLeitos = QtWidgets.QWidget()
        self.cadastrarLeitos.setObjectName("cadastrarLeitos")
        self.nomeLeito = QtWidgets.QLineEdit(self.cadastrarLeitos)
        self.nomeLeito.setGeometry(QtCore.QRect(200, 180, 501, 41))
        self.nomeLeito.setStyleSheet("background-color: rgb(252, 254, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.nomeLeito.setAlignment(QtCore.Qt.AlignCenter)
        self.nomeLeito.setObjectName("nomeLeito")
        self.CadastrarLeito = QtWidgets.QPushButton(self.cadastrarLeitos)
        self.CadastrarLeito.setGeometry(QtCore.QRect(400, 350, 111, 51))
        self.CadastrarLeito.setStyleSheet("background-color: rgb(31, 109, 153);\n"
"color: rgb(252, 254, 255);\n"
"border-radius: 20px;")
        self.CadastrarLeito.setObjectName("CadastrarLeito")
        self.quantidade = QtWidgets.QLineEdit(self.cadastrarLeitos)
        self.quantidade.setGeometry(QtCore.QRect(200, 250, 501, 41))
        self.quantidade.setStyleSheet("background-color: rgb(252, 254, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.quantidade.setAlignment(QtCore.Qt.AlignCenter)
        self.quantidade.setObjectName("quantidade")
        self.voltar_3 = QtWidgets.QPushButton(self.cadastrarLeitos)
        self.voltar_3.setGeometry(QtCore.QRect(400, 420, 111, 61))
        self.voltar_3.setStyleSheet("background-color: rgb(82, 160, 204);\n"
"color: rgb(252, 254, 255);\n"
"border-radius: 20px;")
        self.voltar_3.setObjectName("voltar_3")
        self.paginas.addWidget(self.cadastrarLeitos)
        self.leitos = QtWidgets.QWidget()
        self.leitos.setObjectName("leitos")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leitos)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.leitos)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 839, 508))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.paginas.addWidget(self.leitos)
        self.CadastrarUsers = QtWidgets.QWidget()
        self.CadastrarUsers.setObjectName("CadastrarUsers")
        self.lineEdit = QtWidgets.QLineEdit(self.CadastrarUsers)
        self.lineEdit.setGeometry(QtCore.QRect(130, 140, 501, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(252, 254, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.CadastrarUsers)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 200, 501, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(252, 254, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.CadastrarUsers)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 260, 501, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(252, 254, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.Cadastrar = QtWidgets.QPushButton(self.CadastrarUsers)
        self.Cadastrar.setGeometry(QtCore.QRect(330, 330, 111, 51))
        self.Cadastrar.setStyleSheet("background-color: rgb(31, 109, 153);\n"
"color: rgb(252, 254, 255);\n"
"border-radius: 20px;")
        self.Cadastrar.setObjectName("Cadastrar")
        self.voltar_2 = QtWidgets.QPushButton(self.CadastrarUsers)
        self.voltar_2.setGeometry(QtCore.QRect(330, 400, 111, 61))
        self.voltar_2.setStyleSheet("background-color: rgb(82, 160, 204);\n"
"color: rgb(252, 254, 255);\n"
"border-radius: 20px;")
        self.voltar_2.setObjectName("voltar_2")
        self.paginas.addWidget(self.CadastrarUsers)
        self.users = QtWidgets.QWidget()
        self.users.setObjectName("users")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.users)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.users)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.addUsers = QtWidgets.QPushButton(self.frame_4)
        self.addUsers.setGeometry(QtCore.QRect(20, 10, 111, 61))
        self.addUsers.setStyleSheet("background-color: rgb(31, 109, 153);\n"
"color: rgb(252, 254, 255);\n"
"border-radius: 20px;")
        self.addUsers.setObjectName("addUsers")
        self.voltar = QtWidgets.QPushButton(self.frame_4)
        self.voltar.setGeometry(QtCore.QRect(330, 10, 111, 61))
        self.voltar.setStyleSheet("background-color: rgb(82, 160, 204);\n"
"color: rgb(252, 254, 255);\n"
"border-radius: 20px;")
        self.voltar.setObjectName("voltar")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.users)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 839, 422))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.paginas.addWidget(self.users)
        self.horizontalLayout_2.addWidget(self.paginas)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        PrincipalScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrincipalScreen)
        self.paginas.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PrincipalScreen)

    def retranslateUi(self, PrincipalScreen):
        _translate = QtCore.QCoreApplication.translate
        PrincipalScreen.setWindowTitle(_translate("PrincipalScreen", "MainWindow"))
        self.btnUser.setText(_translate("PrincipalScreen", "Users"))
        self.btnLeito.setText(_translate("PrincipalScreen", "ADD Leito"))
        self.nomeLeito.setPlaceholderText(_translate("PrincipalScreen", "NOME LEITO"))
        self.CadastrarLeito.setText(_translate("PrincipalScreen", "Cadastrar"))
        self.quantidade.setPlaceholderText(_translate("PrincipalScreen", "QUANTIDADE"))
        self.voltar_3.setText(_translate("PrincipalScreen", "Voltar"))
        self.lineEdit.setPlaceholderText(_translate("PrincipalScreen", "E-MAIL"))
        self.lineEdit_2.setPlaceholderText(_translate("PrincipalScreen", "SENHA"))
        self.lineEdit_4.setPlaceholderText(_translate("PrincipalScreen", "PERMISSÃO"))
        self.Cadastrar.setText(_translate("PrincipalScreen", "Cadastrar"))
        self.voltar_2.setText(_translate("PrincipalScreen", "Voltar"))
        self.addUsers.setText(_translate("PrincipalScreen", "ADDUsers"))
        self.voltar.setText(_translate("PrincipalScreen", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrincipalScreen = QtWidgets.QMainWindow()
    ui = Ui_PrincipalScreen()
    ui.setupUi(PrincipalScreen)
    PrincipalScreen.show()
    sys.exit(app.exec_())