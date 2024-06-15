import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.resize(400, 300)

        self.btn = QPushButton('弹出对话框', self)
        self.btn.move(150, 150)
        self.btn.clicked.connect(self.show_dialog)

    def show_dialog(self):
        self.dialog = Dialog(self)
        self.dialog.show()
        self.dialog.exec()


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle('对话框')
        self.resize(200, 200)
        self.setModal(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())