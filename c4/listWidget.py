import sys

from PyQt6.QtWidgets import QWidget, QFormLayout, QApplication, \
                            QListWidget, QPushButton, QLineEdit


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QListWidget 测试')
        self.resize(400, 300)

        self.list = QListWidget()
        self.btn = QPushButton('确定')
        self.btn.clicked.connect(self.addFunc)
        self.le = QLineEdit()

        layout = QFormLayout()
        layout.addRow('输入课程名称: ', self.list)
        layout.addRow(self.le, self.btn)
        self.setLayout(layout)

    def addFunc(self):
        s = self.le.text()
        if s != '':
            self.list.addItem(s)
            self.list.setCurrentRow(self.list.currentRow() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())
