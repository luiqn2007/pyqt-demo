import sys

from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QIntValidator, QDoubleValidator
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QLineEdit 测试')

        layout = QFormLayout()
        leBH = QLineEdit()
        leXM = QLineEdit()
        leMM = QLineEdit()
        leSR = QLineEdit()
        leGL = QLineEdit()
        leGZ = QLineEdit()
        leIP = QLineEdit()
        leCH = QLineEdit()
        layout.addRow('编    号', leBH)
        layout.addRow('姓    名', leXM)
        layout.addRow('登录密码', leMM)
        layout.addRow('出生日期', leSR)
        layout.addRow('工    龄', leGL)
        layout.addRow('基本工资', leGZ)
        layout.addRow(' IP 地址', leIP)
        layout.addRow('车    号', leCH)
        self.setLayout(layout)
        # 编号
        leBH.setPlaceholderText('6 位编号')
        leBH.setInputMask('999999')
        # 密码
        leMM.setPlaceholderText('数字与字母组合')
        leMM.setEchoMode(QLineEdit.EchoMode.Password)
        reg = QRegularExpression('[a-zA-Z0-9]+$')
        leMM.setValidator(QRegularExpressionValidator(reg, self))
        # 工龄：[1, 45]
        leGL.setValidator(QIntValidator(1, 45, self))
        # 工资：[0.00-9999.99]
        gzValidator = QDoubleValidator(self)
        gzValidator.setRange(0.00, 9999.99)
        gzValidator.setNotation(QDoubleValidator.Notation.StandardNotation)
        gzValidator.setDecimals(2)
        leGZ.setValidator(gzValidator)
        # 生日
        leSR.setInputMask('9999-00-00')
        # IP 地址
        leIP.setInputMask('000.000.000.000')
        # 车号
        leCH.setInputMask('XXXXXXX')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
