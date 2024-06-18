import sys

from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QWidget, QListView, QMessageBox, QVBoxLayout, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('QListView 测试')
        self.resize(300, 260)

        listModel = QStringListModel()
        list = ['C++', 'C#', 'Java', 'Python']
        listModel.setStringList(list)
        listView = QListView(self)
        listView.setModel(listModel)
        listView.clicked.connect(
            lambda index: QMessageBox.information(self, 'ListView', '选择: ' + list[index.row()]))

        layout = QVBoxLayout()
        layout.addWidget(listView)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    exit(app.exec())