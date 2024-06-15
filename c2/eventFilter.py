import sys

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setWindowTitle('事件委托测试')
        self.resize(400, 300)

        self.lb1 = QLabel('第==1==标签', self)
        self.lb1.setGeometry(20, 20, 300, 60)
        font = self.lb1.font()
        font.setPointSize(16)
        font.setBold(True)
        self.lb1.setFont(font)
        self.lb1.installEventFilter(self)

        self.lb2 = QLabel('第==2==标签', self)
        self.lb2.setGeometry(20, 100, 300, 60)
        self.lb2.setFont(font)
        self.lb2.installEventFilter(self)

    def eventFilter(self, lb, event):
        if lb == self.lb1:
            if event.type() == QEvent.Type.Enter:
                lb.setStyleSheet('background-color: rgb(170, 255, 255);')
            if event.type() == QEvent.Type.Leave:
                lb.setStyleSheet('')

        if lb == self.lb2:
            if event.type() == QEvent.Type.Enter:
                lb.setStyleSheet('background-color: rgb(255, 0, 0);')
            if event.type() == QEvent.Type.MouseButtonPress:
                lb.setStyleSheet('background-color: rgb(0, 255, 0);')
            if event.type() == QEvent.Type.MouseButtonRelease:
                lb.setStyleSheet('background-color: rgb(0, 0, 255);')
            if event.type() == QEvent.Type.Leave:
                lb.setStyleSheet('')

        return super().eventFilter(lb, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
