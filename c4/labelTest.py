import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QLabel 测试')

        lbl1 = QLabel('初始文本标签', self)
        lbl1.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        lbl2 = QLabel('<font size="6" color="red">红色 3 号文本标签</font>', self)
        lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)
        lbl2.setPalette(palette)

        lbl3 = QLabel(self)
        lbl3.setToolTip('图片标签')
        lbl3.setPixmap(QPixmap('images/蜘蛛.png'))
        lbl3.linkActivated.connect(lambda: print('鼠标点击图片标签'))

        lbl4 = QLabel('<a href="https://www.baidu.com">Baidu</a>', self)
        lbl4.setAlignment(Qt.AlignmentFlag.AlignRight)
        lbl4.setOpenExternalLinks(True)
        lbl4.openExternalLinks()
        lbl4.linkHovered.connect(lambda: print('鼠标滑过超链接'))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(lbl2)
        vbox.addWidget(lbl3)
        vbox.addStretch()
        vbox.addWidget(lbl4)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())