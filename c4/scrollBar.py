import sys

from PyQt6.QtWidgets import \
    QApplication, QWidget, QScrollBar, QHBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QScrollBar 测试')

        s1 = QScrollBar()
        s1.setMaximum(255)
        s1.sliderMoved\
          .connect(lambda: print(s1.value(), s2.value(), s3.value()))
        s2 = QScrollBar()
        s2.setMaximum(255)
        s2.sliderMoved\
          .connect(lambda: print(s1.value(), s2.value(), s3.value()))
        s3 = QScrollBar()
        s3.setMaximum(255)
        s3.sliderMoved\
          .connect(lambda: print(s1.value(), s2.value(), s3.value()))

        layout = QHBoxLayout()
        layout.addWidget(s1)
        layout.addWidget(s2)
        layout.addWidget(s3)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())