import sys

from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('RadioButton 测试')

        rb1 = QRadioButton('南京大学')
        rb1.toggled.connect(lambda: self.toggledButton(rb1))
        rb2 = QRadioButton('东南大学')
        rb2.toggled.connect(lambda: self.toggledButton(rb2))
        rb3 = QRadioButton('南京师范大学')
        rb3.toggled.connect(lambda: self.toggledButton(rb3))

        layout = QHBoxLayout()
        layout.addWidget(rb1)
        layout.addWidget(rb2)
        layout.addWidget(rb3)
        self.setLayout(layout)

    def toggledButton(self, rb):
        if rb.isChecked():
            print(rb.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())