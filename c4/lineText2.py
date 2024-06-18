import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QLineEdit 测试')

        le1 = QLineEdit()
        le1.setValidator(QIntValidator())
        le1.setMaxLength(6)

        le2 = QLineEdit()
        le2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        le2.textChanged.connect(lambda txt: print('输入 %s' % txt))

        le3 = QLineEdit()
        le3.setInputMask('+99-0000-00000000')

        le4 = QLineEdit()
        le4.setFont(QFont('黑体', 20))
        le4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        le4.editingFinished.connect(lambda : print('输入完成'))

        le5 = QLineEdit('2022-07-28')
        le5.setReadOnly(True)

        layout = QFormLayout()
        layout.addRow('整数（0-6位）', le1)
        layout.addRow('实数（xx.xx）', le2)
        layout.addRow('文本字体字号向右', le3)
        layout.addRow('输入文本', le4)
        layout.addRow('只读文本', le5)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
