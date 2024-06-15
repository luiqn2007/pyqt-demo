import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(260, 240, 300, 200)
w.setWindowTitle('PyQt 窗口')

def btnFunc():
    print('窗口左上角 (x,y)=%d,%d' % (w.x(), w.y()))
    print('窗口宽高 (w,h)=%d,%d' % (w.width(), w.height()))
    print('窗口客户区左上角 (x,y)=%d,%d' % (w.geometry().x(), w.geometry().y()))
    print(w.frameGeometry())
    print('窗口内控件 (x,y)=%d,%d' % (btn.x(), btn.y()))


btn = QPushButton('Test Button', w)
btn.move(120, 150)
btn.clicked.connect(btnFunc)

w.show()
exit(app.exec())