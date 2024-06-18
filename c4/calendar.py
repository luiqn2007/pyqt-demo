import sys

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QCalendar 测试')
        self.setGeometry(100, 100, 300, 240)

        cal = QCalendarWidget(self)
        cal.setMinimumDate(QDate(2000, 1, 1))
        cal.setMaximumDate(QDate(2100, 1, 1))
        cal.setGridVisible(True)
        cal.move(10, 10)

        lb = QLabel(self)
        lb.setText(cal.selectedDate().toString('yyyy-MM-dd ddd'))
        lb.move(10, 210)

        cal.clicked[QDate]\
           .connect(lambda date: lb.setText(date.toString('yyyy-MM-dd ddd')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    exit(app.exec())
