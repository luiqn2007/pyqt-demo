import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setWindowTitle('主窗口')
        self.resize(400, 200)
        self.my_center()

        btn = QPushButton('关闭', self)
        btn.move(int(self.__mySize.width() / 2 - btn.width() / 2),
                 int(self.__mySize.height() / 2 - btn.height() / 2))
        btn.clicked.connect(self.on_button_click)

    def my_center(self):
        screen = QApplication.primaryScreen().size()
        self.__mySize = self.geometry()
        self.move(int((screen.width() - self.__mySize.width()) / 2),
                  int((screen.height() - self.__mySize.height()) / 2))

    def on_button_click(self):
        mySender = self.sender()
        print(mySender.text() + '控件')
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()
    sys.exit(app.exec())