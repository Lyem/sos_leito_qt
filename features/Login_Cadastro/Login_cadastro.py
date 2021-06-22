from features.Principal.Principal import PrincipalScreen
from Presenters.Login import Ui_LoginScreen
from PyQt5.QtWidgets import QMainWindow
import requests
import json

class Login_Cadastro(QMainWindow):
    def cadastrar(self):
        privado = self.ui.radioPrivado.isChecked()
        publico = self.ui.radioPublico.isChecked()
        campo = None
        if(privado != False or publico != False):
            if(privado):
                campo = False
            else:
                campo = True
        if(campo != None):
            json = {"nome": self.ui.Hospital.text(),"endereco":{"logradouro": self.ui.Rua.text(),"numero": self.ui.Numero.text(),"cep": self.ui.Cep.text(),"cidade": self.ui.Cidade.text(),"bairro": self.ui.Bairro.text(),"estado": self.ui.Estado.text()},"telefone": self.ui.Telefone.text(),"publico?": campo,"cnes": self.ui.Cnes.text()}
            requests.post('https://sos-leito.herokuapp.com/register/hospital', json = json)
            json2 = {"email": self.ui.Email.text(),"senha": self.ui.SenhaC.text(),"permissao": 3,"cnes": self.ui.Cnes.text()}
            requests.post('https://sos-leito.herokuapp.com/register/user', json = json2)
            self.toLogin()

    def toCadastro(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Cadastrar)

    def toLogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)

    def fecharAviso(self):
        self.ui.Aviso.hide()
    
    def logar(self):
        error = ""
        if(self.ui.User.text() == ''):
            error = "Digite um usuario"
            self.ui.avisoLabel.setText(error)
            self.ui.Aviso.show()
            if(self.ui.Senha.text() == ''):
                error += " Digite uma senha"
                self.ui.avisoLabel.setText(error)
                self.ui.Aviso.show()
        elif(self.ui.Senha.text() == ''):
            error += "Digite uma senha"
            self.ui.avisoLabel.setText(error)
            self.ui.Aviso.show()
        else:
            error = ""
            self.ui.Aviso.hide()
            json = {"user": self.ui.User.text() ,"senha": self.ui.Senha.text()}
            try:
                r = requests.post('https://sos-leito.herokuapp.com/login', json = json)
                if(r.json()['status']):
                    self.principal = PrincipalScreen(r.json())
                    self.principal.show()
                    self.close()
            except:
                error = "erro na conexão"
                self.ui.avisoLabel.setText(error)
                self.ui.Aviso.show()
            else:
                error = "senha ou usuario incorretos"
                self.ui.avisoLabel.setText(error)
                self.ui.Aviso.show()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.Aviso.hide()
        self.ui.btnFecharAviso.clicked.connect(lambda: self.fecharAviso())
        self.ui.btnVoltar.clicked.connect(lambda: self.toLogin())
        self.ui.btnCadastro.mousePressEvent = self.toCadastro
        self.ui.btnCadastrar.clicked.connect(lambda: self.cadastrar())
        self.ui.btnLogar.clicked.connect(lambda: self.logar())
        self.show()