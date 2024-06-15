import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFormLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('表单布局测试')

        layout = QFormLayout()
        layout.addRow(QLabel('学号'), QLineEdit())
        layout.addRow(QLabel('姓名'), QLineEdit())
        layout.addRow(QLabel('出生日期'), QLineEdit())
        layout.addRow(QLabel('专业'), QLineEdit())
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())