import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QIcon, QFont


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('图标和气泡')
        self.setWindowIcon(QIcon('./images/python.ico'))
        self.setGeometry(100, 300, 400, 200)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('这是<b>Widget</b>窗口')

        btn = QPushButton('按钮', self)
        btn.setToolTip('这个控件属于<b>QPushButton</b>类')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WinForm()
    w.show()
    exit(app.exec())