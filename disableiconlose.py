from PyQt5.QtWidget import QMainWindow, QWidget, QApplication, QPushButton, Qlabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self,button.setText("Button1")
        self.setGeometry(0,0,300,300)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry() # cek ukuran main window app kita
        cwc = QdekstopWidget().availableGeometry().center() # pada sqreen saya: (682,363)
        #print(cwc)
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.setFixedSize(300,300) # agar tidak bisa di-resize! icon maximize juga akan otomatis hilang
        #self.setWindowFlag(QtCore.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint,False)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint,False)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()        