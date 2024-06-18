import sys

from PyQt6.QtWidgets import QApplication, QWidget, \
                            QLabel, QComboBox, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('ComBox 测试')
        self.resize(300, 100)

        self.lb1 = QLabel('选择课程：')
        self.lb2 = QLabel('  ')
        self.cb = QComboBox()
        self.cb.addItem('计算机')
        self.cb.addItems(['软件工程', '通信工程', '人工智能'])
        self.cb.currentIndexChanged.connect(self.selectItem)

        layout = QVBoxLayout()
        layout.addWidget(self.lb1)
        layout.addWidget(self.cb)
        layout.addWidget(self.lb2)
        self.setLayout(layout)

    def selectItem(self):
        item = self.cb.currentText()
        for i in range(self.cb.count()):
            if self.cb.itemText(i) == item:
                self.lb2.setText('选择 %d 项: %s' % (i, item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())
