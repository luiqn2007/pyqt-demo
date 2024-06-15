import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('水平布局测试')

        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(QPushButton('A'), 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(QPushButton('B'), 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(QPushButton('C'), 0)
        layout.addWidget(QPushButton('D'), 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(QPushButton('E'), 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())