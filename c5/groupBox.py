import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QGroupBox, QRadioButton


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QGroupBox 测试')

        self.rbJSJ = QRadioButton('计算机', self)
        self.rbRJGC = QRadioButton('软件工程', self)
        self.rbTXGC = QRadioButton('通信工程', self)
        self.rbRGZN = QRadioButton('人工智能', self)
        self.list = [self.rbJSJ, self.rbRJGC, self.rbTXGC, self.rbRGZN]




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
