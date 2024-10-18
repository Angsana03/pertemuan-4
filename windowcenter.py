# =================== Window Management ================
from PyQtWidgets import QMainWindow, QWidgets, QApplication, QPushButton, QLabel, QDekstopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry() # cek ukuran main window app kita
        cwc = QDekstopWidget().availableGeometry().center() # pada screen saya: (682,363)
        #print(cwc)
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()        