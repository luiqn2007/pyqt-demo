import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(260, 240, 300, 200)
w.setWindowTitle('字体测试')

font = QFont()
font.setPointSize(16)
font.setFamily('Arial')
font.setBold(True)

lb = QLabel("标签测试 Text", w)
lb.move(60, 20)
lb.resize(160, 30)
lb.setFont(font)

w.show()
exit(app.exec())