import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout


class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setWindowTitle('QPushButton 测试')

        self.btn1 = QPushButton('文本按钮')
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda : print('点击 btn1'))

        self.btn2 = QPushButton('图片按钮')
        self.btn2.setIcon(QIcon('images/蜘蛛.png'))
        self.btn2.clicked.connect(lambda : print('点击 btn2'))

        self.btn3 = QPushButton('&Change')
        self.btn3.setDefault(True)
        self.btn3.clicked.connect(self.btnChange)
        self.btn3.clicked.connect(lambda : print('点击 btn3'))

        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

    def btnChange(self):
        if self.btn1.isChecked():
            print('文本按钮选择')
        else:
            print('文本按钮释放')

        self.btn2.setEnabled(not self.btn2.isEnabled())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())