import math
import sys

from PyQt6.QtWidgets import QApplication, QDialog

from circleCal2ui import Ui_Dialog


class CircleCal(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def calCircle(self):
        r = float(self.ui.leRadius.text())
        if r >= 0:
            self.ui.leLength.setText(str(2 * math.pi * r))
            self.ui.leArea.setText(str(math.pi * r * r))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.instance()
    dlg = CircleCal()
    dlg.show()
    sys.exit(app.exec())