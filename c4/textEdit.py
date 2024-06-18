import sys

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QTextEdit 测试')
        self.resize(300, 270)

        self.te = QTextEdit()
        btn1 = QPushButton('显示 HTML')
        btn2 = QPushButton('显示文本')

        layout = QVBoxLayout()
        layout.addWidget(self.te)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

        self.te.setTextColor(QColor(0, 0, 255))
        self.te.setText('Python 编程\nPyQt6 界面编程')

        btn1.clicked.connect(self.btn1clicked)
        btn2.clicked.connect(self.btn2clicked)

    def btn1clicked(self):
        global tmp
        tmp = self.te.toPlainText()
        self.te.setHtml('<font color="red" size="6">C++程序设计<p>Spring Boot 应用开发</font>')

    def btn2clicked(self):
        global tmp
        self.te.setPlainText(tmp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
