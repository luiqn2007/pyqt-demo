import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import \
    QApplication, QWidget, QDial, QVBoxLayout, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QDial 测试')
        self.resize(400, 300)

        dial = QDial(self)
        dial.setRange(0, 100)
        dial.setNotchesVisible(True)

        lb = QLabel('0', self)
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb.setFont(QFont('Arial Black', 16))

        dial.valueChanged.connect(lambda: lb.setText(str(dial.value())))

        layout = QVBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(lb)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())