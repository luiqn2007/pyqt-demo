import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt6.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('布局嵌套测试')

        # 最外层 Layout
        layout = QVBoxLayout()

        # 中部表单
        formLayout = QFormLayout()
        formLayout.addRow(QLabel('学号'), QLineEdit())
        formLayout.addRow(QLabel('姓名'), QLineEdit())
        formLayout.addRow(QLabel('出生日期'), QLineEdit())
        formLayout.addRow(QLabel('专业'), QLineEdit())
        form = QWidget()
        form.setLayout(formLayout)

        # 底部按钮
        footerLayout = QHBoxLayout()
        footerLayout.addWidget(QPushButton('确定'))
        footerLayout.addWidget(QPushButton('取消'))
        footerLayout.addWidget(QPushButton('清除'))
        footer = QWidget()
        footer.setLayout(footerLayout)

        layout.addWidget(QLabel('<b>学生信息输入</b>'), 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(form)
        layout.addWidget(footer)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())