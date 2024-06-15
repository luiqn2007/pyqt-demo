from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

import sys


class MyLabel(QLabel):
    def __init__(self, parent):
        super(MyLabel, self).__init__(parent)
        self.setFont(QFont('楷体', 16))

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.setText('点击鼠标左键')
        elif event.buttons() == Qt.MouseButton.RightButton:
            self.setText('点击鼠标右键')
        elif event.buttons() == Qt.MouseButton.MiddleButton:
            self.setText('点击鼠标中键')
        elif event.buttons() == Qt.MouseButton.LeftButton | Qt.MouseButton.RightButton:
            self.setText('点击鼠标左键和右键')

    def wheelEvent(self, event):
        angle = event.angleDelta() / 8

        if angle.y() > 0:
            self.setText("滚轮向上滚动 %f" % angle.y())
        elif angle.y() < 0:
            self.setText("滚轮向下滚动 {}".format(-angle.y()))

    def mouseDoubleClickEvent(self, event):
        self.setText('鼠标双击')

    def mouseReleaseEvent(self, ev):
        self.setText('鼠标释放')


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('事件测试')
        self.resize(300, 120)
        self.lb = MyLabel(self)
        self.lb.setText('----------------')
        self.lb.setGeometry(60, 40, 200, 50)

    def mouseMoveEvent(self, event):
        print("鼠标移动", event.pos().x(), event.pos().y())

    def resizeEvent(self, event):
        print("窗口大小", event.size())

    def keyPressEvent(self, event):
        print("按键按下", event.key())
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def event(self, event):
        if event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Q:
            print("Q Key")
            self.close()
            return True
        return QWidget.event(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())