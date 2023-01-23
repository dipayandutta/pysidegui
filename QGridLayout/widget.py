from PySide6.QtWidgets import QWidget, QSizePolicy, QGridLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout Example")

        button1 = QPushButton("One")
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")
        button6 = QPushButton("six")
        button7 = QPushButton("seven")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button1,0,0)
        grid_layout.addWidget(button2,0,1,1,2)
        grid_layout.addWidget(button3,1,0,2,1)
        grid_layout.addWidget(button4,1,1)
        grid_layout.addWidget(button5,1,2)
        grid_layout.addWidget(button6,2,1)
        grid_layout.addWidget(button7,2,2)

        self.setLayout(grid_layout)

    def button1_clicked(self):
        print("Button1 Clicked!")
