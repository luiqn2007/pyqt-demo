import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QFrame, QComboBox, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QFrame 测试')
        self.resize(500, 350)

        self.frame = QFrame()
        self.frame.setFrameStyle(QFrame.Shape.Panel)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setFixedSize(480, 200)

        layout = QVBoxLayout(self)
        layout.addSpacing(10)
        layout.addWidget(self.frame)
        layout.addSpacing(20)
        layout.addStretch()

        self.cb1 = QComboBox()
        self.cb1.addItems(['1', '2', '3'])
        self.cb1.currentIndexChanged.connect(self.setLineWidth)
        self.cb2 = QComboBox()
        self.cb2.addItems(['1', '2', '3'])
        self.cb2.currentIndexChanged.connect(self.setMidLine)
        self.cb3 = QComboBox()
        self.cb3.addItems(['NoFrame', 'Box', 'Panel', 'StyledPanel'])
        self.cb3.currentIndexChanged.connect(self.setFrameShape)
        self.cb4 = QComboBox()
        self.cb4.addItems(['Plain', 'Raised', 'Sunken'])
        self.cb4.currentIndexChanged.connect(self.FrameShadow)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel('LineWidth: '))
        hLayout.addWidget(self.cb1)
        layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel('MidLine: '))
        hLayout.addWidget(self.cb2)
        layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel('FrameShape: '))
        hLayout.addWidget(self.cb3)
        layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel('FrameShadow: '))
        hLayout.addWidget(self.cb4)
        layout.addLayout(hLayout)

    def setLineWidth(self):
        width = int(self.cb1.currentText())
        self.frame.setLineWidth(width)

    def setMidLine(self):
        width = int(self.cb2.currentText())
        self.frame.setMidLineWidth(width)

    def setFrameShape(self):
        shape = self.cb3.currentText()
        self.frame.setFrameShape(QFrame.Shape[shape])

    def FrameShadow(self):
        shadow = self.cb4.currentText()
        self.frame.setFrameShadow(QFrame.Shadow[shadow])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
