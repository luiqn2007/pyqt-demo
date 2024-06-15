import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QMessageBox 测试')
        self.resize(300, 100)

        btn = QPushButton('显示 QMessageBox', self)
        btn.clicked.connect(self.myMsg)

    def myMsg(self):
        reply = QMessageBox.information(self, '标题内容', '文本内容',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            print('OK')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())