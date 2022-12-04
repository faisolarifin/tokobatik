import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class UTS01(QWidget):
    def __init__(self):
        super().__init__()
        form = QFormLayout()
        form.addRow(QLabel('Nama'),QLineEdit())
        form.addRow(QLabel('Alamat'), QTextEdit())
        form.addRow(QLabel(), QPushButton('Simpan'))
        form.addRow(QLabel(), QPushButton('Reset'))
        self.setLayout(form)
        self.setWindowTitle('UTS No 1')
        self.setGeometry(300,120,450,340)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = UTS01()
    ex.show()
    sys.exit(app.exec_())
