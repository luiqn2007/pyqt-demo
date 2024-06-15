from PyQt6.QtCore import pyqtSignal, QObject

class StandardItem(QObject):

    data_changed = pyqtSignal(str, str, name='statusChanged')

    def update(self):
        self.data_changed.emit('oldValue', 'newValue')