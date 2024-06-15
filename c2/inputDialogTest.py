import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QHBoxLayout, QInputDialog


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('Input Dialog 测试')

        btn1 = QPushButton('文本测试')
        btn1.clicked.connect(self.getText)
        btn2 = QPushButton('选项测试')
        btn2.clicked.connect(self.getItem)
        btn3 = QPushButton('整型测试')
        btn3.clicked.connect(self.getInt)

        layout = QHBoxLayout(self)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

    def getText(self):
        text, ok = QInputDialog.getText(self, '文本测试', '姓名：')
        if ok:
            print(text)

    def getItem(self):
        items = ('计算机导论', 'Java', 'C++', '数据结构')
        item, ok = QInputDialog.getItem(self, '选项测试', '课程：', items, 1, True)
        if ok:
            print(item)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, '整型测试', '成绩：')
        if ok:
            print(num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())