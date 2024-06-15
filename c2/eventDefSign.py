import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):

    closeWindow = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('自定义信号测试')
        self.resize(200, 100)

        btn = QPushButton('关闭窗口', self)
        btn.clicked.connect(self.onClicked)

        self.closeWindow.connect(self.onClose)

    def onClicked(self):
        self.closeWindow.emit()

    def onClose(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())