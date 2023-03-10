from PySide6.QtWidgets import QWidget,QLineEdit,QLabel,QPushButton,QGridLayout,QVBoxLayout,QMainWindow
from childWindow import ChildWindow

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login Window")
        self.setFixedSize(640,480)
        self.cWindow = ChildWindow()

        username = QLabel("Username:")
        self.user_edit = QLineEdit()
        
        password = QLabel("Password:")
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)

        button = QPushButton("login")
        button.clicked.connect(self.login_user)

        self.text_holder_label = QLabel("please Enter username and password ot login")

        grid_layout = QGridLayout()
        grid_layout.addWidget(username,0,0)
        grid_layout.addWidget(self.user_edit,0,1)
        grid_layout.addWidget(password,1,0)
        grid_layout.addWidget(self.pass_edit,1,1)
        grid_layout.addWidget(self.text_holder_label,2,0)
        grid_layout.addWidget(button,2,1)

        self.setLayout(grid_layout)

    def login_user(self):
        userCred = self.user_edit.text()
        passCred = self.pass_edit.text()

        if userCred=='admin' and passCred=='admin':
            self.cWindow.show()
        else:
            self.text_holder_label.setText("Wrong username or password") 
