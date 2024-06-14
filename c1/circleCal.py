from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton
import math
import sys

class CircleCal(QDialog):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.leRadius = self.addInput('半径', 40, True)
        self.leRadius.returnPressed.connect(self.calCircle)
        self.leLength = self.addInput('周长', 80)
        self.leArea = self.addInput('面积', 120)

        self.pbCal = QPushButton('计算', self)
        self.pbCal.setGeometry(140, 160, 93, 28)
        self.pbCal.clicked.connect(self.calCircle)

        self.resize(350, 200)
        self.move(300, 300)
        self.setWindowTitle('计算圆面积')

    def calCircle(self):
        r = eval(self.leRadius.text())
        if r >= 0:
            self.leLength.setText(str(2 * math.pi * r))
            self.leArea.setText(str(math.pi * r * r))

    def addInput(self, label, height, enable = False):
        QLabel(label + '=', self).setGeometry(80, height, 71, 21)
        le = QLineEdit(self)
        le.setGeometry(140, height, 200, 21)
        le.setEnabled(enable)
        return le


app = QApplication(sys.argv)
dlg = CircleCal()
dlg.show()
sys.exit(app.exec())