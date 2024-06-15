import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('网格布局测试')

        layout = QGridLayout()
        self.setLayout(layout)

        txt = [['7', '8', '9', '/'],
               ['4', '5', '6', '*'],
               ['1', '2', '3', '-'],
               ['0', '00', '.', '+'],
               ['C', '<-', '', '=']]
        for i in range(0, len(txt)):
            for j in range(0, len(txt[i])):
                if txt[i][j] == '':
                    continue
                layout.addWidget(QPushButton(txt[i][j]), i, j)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())