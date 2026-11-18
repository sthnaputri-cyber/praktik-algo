import sys 
from PyQt5 import QtWidgets, uic 
import db_helper

class MainWindow(QtWidgets.QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__() 
        # Load the UI file dynamically 
        uic.loadUi('main.ui', self) 

        # Initialize Database
        db_helper.init_db()
 
        # Connect buttons to functions
        self.btnKeluar.clicked.connect(self.close) 
if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_()) 