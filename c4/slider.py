import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import \
    QApplication, QWidget, QSlider, QVBoxLayout, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QSlide 测试')
        self.resize(300, 100)

        self.lb = QLabel('Python 程序设计')
        self.lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sl = QSlider(Qt.Orientation.Horizontal)
        self.sl.setMinimum(0)
        self.sl.setMaximum(100)
        self.sl.setSingleStep(2)
        self.sl.setValue(20)
        self.sl.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sl.setTickInterval(10)
        self.sl.valueChanged.connect(self.slideValueChanged)

        layout = QVBoxLayout()
        layout.addWidget(self.lb)
        layout.addWidget(self.sl)
        self.setLayout(layout)

    def slideValueChanged(self):
        size = self.sl.value()
        self.lb.setFont(QFont('Arial', size))
        print('当前值：%d' % size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())