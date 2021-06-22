from features.Login_Cadastro.Login_cadastro import Login_Cadastro
import sys
from PyQt5 import QtWidgets




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Login_Cadastro()
    sys.exit(app.exec_())