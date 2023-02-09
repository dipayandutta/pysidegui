from PySide6.QtWidgets import QApplication 
from multiWindow import MainWindow
import sys

app = QApplication(sys.argv)

widget = MainWindow()
widget.show()

app.exec()
