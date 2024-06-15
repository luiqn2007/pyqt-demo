import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSplitter, QTextEdit, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('Splitter 测试')
        self.setGeometry(360, 260, 300, 200)

        layout = QVBoxLayout()
        sp1 = QSplitter(Qt.Orientation.Vertical)
        sp1.addWidget(QPushButton('A'))
        sp1.addWidget(QPushButton('B'))
        sp1.setSizes([100, 100])
        sp2 = QSplitter(Qt.Orientation.Horizontal)
        sp2.addWidget(QTextEdit())
        sp2.addWidget(sp1)
        layout.addWidget(sp2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())