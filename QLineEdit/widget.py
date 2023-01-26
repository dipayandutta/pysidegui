from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("FullName")
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.textEdited.connect(self.text_edited)


        button = QPushButton("Grab Data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I AM HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)


        self.setLayout(v_layout)

    def button_clicked(self):
        self.text_holder_label.setText(self.line_edit.text())
        print(self.line_edit.text())

    def return_pressed(self):
        print("Return Pressed")

    def text_edited(self,new_text):
        print("Text edited . New Text",new_text)
