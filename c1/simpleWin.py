from PyQt6.QtWidgets \
    import QApplication, QWidget, QPushButton
import sys


def btnFunc():
    print('Button!')


app = QApplication(sys.argv)

w = QWidget()
w.resize(300, 200)
w.move(260, 240)
w.setWindowTitle('PyQt Window')

btn = QPushButton(w)
btn.setText('Click Me')
btn.move(120, 150)
btn.clicked.connect(btnFunc)

w.show()
sys.exit(app.exec())