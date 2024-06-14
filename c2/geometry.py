import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(260, 240, 300, 200)
w.setWindowTitle('窗口测试')
w.show()

print(w.x(), w.y(), w.width(), w.height())
print(w.pos(), w.size())
print(w.geometry())

exit(app.exec())