import sys

from PyQt6.QtCore import QBasicTimer
from PyQt6.QtWidgets import \
    QApplication, QWidget, QProgressBar, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QProgressBar 测试')
        self.resize(300, 200)

        self.pvalue = 0
        self.timer = QBasicTimer()

        self.pb = QProgressBar(self)
        self.pb.move(50, 50)
        self.pb.resize(250, 20)
        self.pb.setRange(0, 100)
        self.pb.setValue(0)

        self.btn = QPushButton('开始', self)
        self.btn.move(120, 100)
        self.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100, self)
            self.pb.setValue(self.pvalue)
            self.btn.setText('停止')

    def timerEvent(self, ev):
        if self.pvalue == 100:
            self.timer.stop()
        else:
            self.pvalue += 1
            self.pb.setValue(self.pvalue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())