import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFontDialog, QColorDialog, QPushButton, QTextEdit


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('Font Dialog 测试')
        self.setGeometry(300, 200, 360, 200)

        self.btn = QPushButton('字体颜色\n测试', self)
        self.btn.move(260, 60)
        self.btn.resize(60, 40)
        self.btn.clicked.connect(self.getFont)

        self.te = QTextEdit(self)

    def getFont(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.te.setFont(font)
            color = QColorDialog.getColor()
            self.te.setTextColor(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())