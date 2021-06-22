from Presenters.Principal import Ui_PrincipalScreen
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

class PrincipalScreen(QMainWindow):
    def apagarLista(self):
        for x in self.listLeitos:
            x.setParent(None)
    
    def apagarListaU(self):
        for x in self.listUsers:
            x.setParent(None)

    def toCadastrarLeito(self):
        self.ui.paginas.setCurrentWidget(self.ui.cadastrarLeitos)
    
    def toPrincipal(self):
        self.ui.paginas.setCurrentWidget(self.ui.leitos)

    def toUsers(self,user):
        self.ui.paginas.setCurrentWidget(self.ui.users)
        self.getuser(user)
    
    def toCadastrarUsers(self):
        self.ui.paginas.setCurrentWidget(self.ui.CadastrarUsers)

    def cadastrarLeito(self, user):
        json = {"nome": self.ui.nomeLeito.text(), "qtd": int(self.ui.quantidade.text()), "cnes": user['cnes']}
        requests.post('https://sos-leito.herokuapp.com/register/leito', json = json)
        self.apagarLista()
        self.leito(user)
        self.toPrincipal()

    def CadastrarUser(self, user):
        json = {"email": self.ui.lineEdit.text(),"senha": self.ui.lineEdit_2.text(),"permissao": int(self.ui.lineEdit_4.text()),"cnes": user['cnes']}
        requests.post('https://sos-leito.herokuapp.com/register/user', json = json)
        self.apagarListaU()
        self.getuser(user)
        self.toUsers(user)

    def deletarleito(self,name,cnes,qtdTotal,user):
        json = {"nome": name, "cnes": cnes,"qtdTotal": qtdTotal}
        requests.post('https://sos-leito.herokuapp.com/delete/leitos', json = json)
        print('foi')
        self.apagarLista()
        self.leito(user)
    
    def deletarUser(self,name,cnes,permissao,user):
        json = {"email": name, "cnes": cnes,"permissao": permissao}
        requests.post('https://sos-leito.herokuapp.com/delete/user', json = json)
        self.apagarListaU()
        self.getuser(user)
    
    def setQtd(self,qtd,name,cnes,qtdtotal,user):
        json = {'old':{"nome": name, "cnes": cnes,"qtdTotal": qtdtotal}, "new":{"$set":{"qtd":qtd}}}
        requests.post('https://sos-leito.herokuapp.com/setqtd', json = json)
        self.apagarLista()
        self.leito(user)

    def leitos(self, r,row,collum,user):
        newname = "frame_" + str(row) + "_" + str(collum)
        self.newname = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        self.newname.setMinimumSize(QtCore.QSize(331,221))
        self.newname.setMaximumSize(QtCore.QSize(331,221))
        self.newname.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.newname.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newname.setObjectName(""+newname+"")
        self.add = QtWidgets.QSpinBox(self.newname)
        self.add.setGeometry(QtCore.QRect(220, 180, 42, 27))
        self.add.setMaximum(r['qtdTotal'])
        self.add.setValue(r['qtd'])
        self.add.valueChanged.connect(lambda: self.setQtd(self.add.value(),r['nome'],r['cnes'],r['qtdTotal'],user))
        if(self.add.value() < r['qtdTotal']/2):
            self.newname.setStyleSheet("background-color: rgb(224, 27, 36);")
        else:
            self.newname.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.add.setObjectName("add")
        self.leitoName = QtWidgets.QLabel(self.newname)
        self.leitoName.setGeometry(QtCore.QRect(10, 10, 58, 18))
        self.leitoName.setObjectName("leitoName")
        self.leitoName.setStyleSheet("color: rgb(62, 63, 64);")
        self.leitoName.setText(r['nome'])
        self.pushButton = QtWidgets.QPushButton(self.newname)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 80, 26))
        self.pushButton.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Deletar')
        self.listLeitos.append(self.newname)
        self.pushButton.clicked.connect(lambda: self.deletarleito(r['nome'],r['cnes'],r['qtdTotal'],user))
        self.ui.gridLayout.addWidget(self.newname,row,collum,1,1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)


    def users(self,r,row,collum,user):
        framename = "userframe_" + str(row) + "_" + str(collum)
        self.framename = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_2)
        self.framename.setMinimumSize(QtCore.QSize(550, 50))
        self.framename.setMaximumSize(QtCore.QSize(550, 50))
        self.framename.setStyleSheet("background-color: rgb(252, 254, 255);\n""color: rgb(0, 0, 0);")
        self.framename.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framename.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framename.setObjectName(""+framename+"")
        self.label = QtWidgets.QLabel(self.framename)
        self.label.setGeometry(QtCore.QRect(0, 0, 481, 51))
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label.setText(r['nome'])
        self.pushButton = QtWidgets.QPushButton(self.framename)
        self.pushButton.setGeometry(QtCore.QRect(480, 0, 80, 51))
        self.pushButton.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Deletar')
        self.pushButton.clicked.connect(lambda: self.deletarUser(r['nome'],r['cnes'],r['permissao'],user))
        self.listUsers.append(self.framename)
        self.ui.gridLayout_2.addWidget(self.framename,row,collum,1,1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def getuser(self,user):
        json = {"cnes": user['cnes']}
        r = requests.get('https://sos-leito.herokuapp.com/getusers', json = json)
        n = 0
        linha = 0
        c = 1
        for l in r.json()['users']:
            n += 1
            if(n == 1):
                linha = linha + 1
                n = 0

        if(linha == 0):
            c = 0
            linha = 0
            if(n != 0):
                linha = 1
                c = n

        qt = 0
        for x in range(0,linha):
            for y in range(0,c):
                if(r.json()['users'][qt]['nome'] != user['email']):
                    self.users(r.json()['users'][qt],x,y,user)
                qt += 1

    def leito(self,user):
        json = {"cnes": user['cnes']}
        r = requests.get('https://sos-leito.herokuapp.com/leitos', json = json)
        n = 0
        linha = 0
        c = 3
        for l in r.json()['leitos']:
            n += 1
            if(n == 3):
                linha = linha + 1
                n = 0

        if(linha == 0):
            c = 0
            linha = 0
            if(n != 0):
                linha = 1
                c = n

        qt = 0
        for x in range(0,linha):
            for y in range(0,c):
                self.leitos(r.json()['leitos'][qt],x,y,user)
                qt += 1

    def __init__(self,user):
        self.listLeitos = []
        self.listUsers = []
        QMainWindow.__init__(self)
        self.ui = Ui_PrincipalScreen()
        self.ui.setupUi(self)
        self.ui.btnLeito.clicked.connect(lambda: self.toCadastrarLeito())
        self.ui.voltar_3.clicked.connect(lambda: self.toPrincipal())
        self.ui.btnUser.clicked.connect(lambda: self.toUsers(user))
        self.ui.voltar.clicked.connect(lambda: self.toPrincipal())
        self.ui.addUsers.clicked.connect(lambda: self.toCadastrarUsers())
        self.ui.voltar_2.clicked.connect(lambda: self.toPrincipal())
        self.ui.Cadastrar.clicked.connect(lambda: self.CadastrarUser(user))
        self.ui.CadastrarLeito.clicked.connect(lambda: self.cadastrarLeito(user))
        if(user['permissao'] != 3):
            self.ui.btnUser.hide()
            if(user['permissao'] != 2):
                self.ui.btnLeito.hide()
        
        self.leito(user)
    
        self.show()