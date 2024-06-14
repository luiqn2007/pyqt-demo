import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(260, 240, 300, 200)
w.setWindowTitle('窗口测试')

palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.red)
lb = QLabel('测试标签文本', w)
lb.move(100, 20)
lb.resize(100, 20)
lb.setAutoFillBackground(True)
lb.setPalette(palette)

color = QColor(10, 50, 255)
te = QTextEdit('文本框测试文本', w)
te.move(100, 60)
te.resize(100, 20)
te.setTextColor(color)

w.show()
exit(app.exec())