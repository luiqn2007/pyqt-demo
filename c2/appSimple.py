import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("<font color=blue size=64><b>程序正在启动...</b></font>")
label.setWindowFlags(Qt.WindowType.SplashScreen | Qt.WindowType.FramelessWindowHint)
label.show()
exit(app.exec())