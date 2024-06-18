import sys

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import \
    QApplication, QWidget, QDateTimeEdit, QPushButton, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QDateTimeEdit 测试')
        self.setGeometry(100, 100, 300, 240)

        self.dt = QDateTimeEdit()
        self.dt.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.dt.setMinimumDate(QDate.currentDate().addYears(-1))
        self.dt.setMaximumDate(QDate.currentDate().addYears(1))
        self.dt.setCalendarPopup(True)
        self.dt.dateChanged.connect(lambda dtime: print(dtime))
        self.dt.timeChanged.connect(lambda dtime: print(dtime))
        self.dt.dateTimeChanged.connect(lambda dtime: print(dtime))

        btn = QPushButton('获取日期时间')
        btn.clicked.connect(self.clickd)

        layout = QVBoxLayout()
        layout.addWidget(self.dt)
        layout.addWidget(btn)
        self.setLayout(layout)

    def clickd(self):
        datetime = self.dt.dateTime()
        maximum = self.dt.maximumDateTime()
        print('日期时间=%s' % str(datetime))
        print('最大日期时间=%s' % str(maximum))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    exit(app.exec())
