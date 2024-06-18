import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSpinBox, QHBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('SpinBox 测试')
        self.resize(300, 100)

        self.lb1 = QLabel('选择或输入数字：')
        self.lb2 = QLabel('')
        self.lb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sb = QSpinBox()
        self.sb.valueChanged.connect(lambda: self.lb2.setText('输入值：%d' % self.sb.value()))

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.lb1)
        hLayout.addWidget(self.sb)

        layout = QVBoxLayout(self)
        layout.addLayout(hLayout)
        layout.addWidget(self.lb2)

    def selectItem(self):
        item = self.cb.currentText()
        for i in range(self.cb.count()):
            if self.cb.itemText(i) == item:
                self.lb2.setText('选择 %d 项: %s' % (i, item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    exit(app.exec())
