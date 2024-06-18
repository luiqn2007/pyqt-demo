import sys

from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout
from PyQt6.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('CheckBox 测试')

        self.cb1 = QCheckBox('复选框-&1')
        self.cb1.setChecked(True)
        self.cb1.stateChanged.connect(self.btnState)

        self.cb2 = QCheckBox('复选框-&2')
        self.cb2.toggled.connect(self.btnState)

        self.cb3 = QCheckBox('复选框-&3')
        self.cb3.setTristate(True)
        self.cb3.setCheckState(Qt.CheckState.PartiallyChecked)
        self.cb3.stateChanged.connect(self.btnState)

        layout = QHBoxLayout()
        layout.addWidget(self.cb1)
        layout.addWidget(self.cb2)
        layout.addWidget(self.cb3)
        self.setLayout(layout)

    def btnState(self):
        print('复选框-1: ' + str(self.cb1.checkState()))
        print('复选框-2: ' + str(self.cb2.checkState()))
        print('复选框-3: ' + str(self.cb3.checkState()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    app.exec()
