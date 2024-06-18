import sys

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QListView, QVBoxLayout, QApplication, QLineEdit, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QListView 测试')
        self.resize(300, 260)

        data = ['C++', 'C#', 'Java', 'Python']
        mode = QStandardItemModel(4, 1)
        for i in range(mode.rowCount()):
            mode.setItem(i, 0, QStandardItem(data[i]))
        mode.insertRow(4, QStandardItem('数据结构'))
        lv = QListView()
        lv.setModel(mode)

        le = QLineEdit()
        add = QPushButton('增加项')
        add.clicked.connect(lambda: mode.appendRow(QStandardItem(le.text())))
        remove = QPushButton('移除项')
        remove.clicked.connect(lambda: mode.removeRow(mode.rowCount() - 1))
        sort = QPushButton('排序项')
        sort.clicked.connect(lambda: mode.sort(0))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(le)
        layout.addWidget(add)
        layout.addWidget(remove)
        layout.addWidget(sort)
        layout.addWidget(lv)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())