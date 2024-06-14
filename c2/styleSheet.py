import sys
from PyQt6.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("样式测试")
        pb1 = QPushButton('命令按钮1')
        pb2 = QPushButton('命令按钮2')
        pb3 = QPushButton('命令按钮3')
        lb = QLabel('标签文本')

        vLay = QVBoxLayout()
        vLay.addWidget(pb1)
        vLay.addWidget(pb2)
        vLay.addWidget(pb3)
        vLay.addWidget(lb)
        self.setLayout(vLay)

        lb.setStyleSheet("color: rgb(20, 20, 255); font-size: 20px;\
                          font-weight: bold; font-family: Courier New;")


app = QApplication(sys.argv)
pbStyle = """
QPushButton {
  background-color: red;
  color: blue;
  font-family: 黑体;
  font-size: 16px;
}
"""
w = MyWidget()
w.setStyleSheet(pbStyle)
w.show()
exit(app.exec())