import sys

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QTextEdit


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('File Dialog 测试')

        layout = QVBoxLayout()
        btn1 = QPushButton('选择图片文件')
        btn1.clicked.connect(self.img_file)
        layout.addWidget(btn1)

        self.lb = QLabel('')
        layout.addWidget(self.lb)

        btn2 = QPushButton('选择文本文件')
        btn2.clicked.connect(self.text_file)
        layout.addWidget(btn2)

        self.te = QTextEdit()
        layout.addWidget(self.te)

        self.setLayout(layout)

    def img_file(self):
        fname, _tmp = QFileDialog.getOpenFileName(self, 'Open File', '/', '*.png *.ico')
        self.lb.setPixmap(QPixmap(fname))

    def text_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.AnyFile)
        dlg.setFilter(QDir.Filter.Files)

        if dlg.exec():
            files = dlg.selectedFiles()
            f = open(files[0], 'r')
            with f:
                text = f.read()
                self.te.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())