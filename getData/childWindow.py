from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QMainWindow

class ChildWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Child Window")
        self.setFixedSize(640,480)
        layout = QVBoxLayout()
        self.label = QLabel("You Have Logged In!")
        layout.addWidget(self.label)
        self.setLayout(layout)
