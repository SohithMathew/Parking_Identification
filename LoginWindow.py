import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from HomeWindow import HomeScreen
from encryption_helper import verify_password

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(400, 200)

        layout = QVBoxLayout()

        label_username = QLabel("Username : ")
        label_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_password = QLabel("Password : ")
        label_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_username = QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")
        self.input_password = QLineEdit()
        self.input_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_password.setEchoMode(QLineEdit.Password)

        button_login = QPushButton("Login")
        button_login.setStyleSheet("padding:5px;font-size:17px;background:green;color:#fff")

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color:red")

        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(button_login)
        layout.addWidget(self.error_label)

        button_login.clicked.connect(self.login)

        self.setLayout(layout)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if not username or not password:
            self.error_label.setText("Username and password are required!")
            return

        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)

            stored_username = config["admin_username"]
            stored_password = config["admin_password"]
            salt = config["salt"]

            if username == stored_username and verify_password(stored_password, password, salt):
                self.error_label.setText("Login successful!")
                self.home = HomeScreen()
                self.home.show()
                self.close()
            else:
                self.error_label.setText("Invalid username or password.")
        except Exception as e:
            self.error_label.setText(f"Error during login: {e}")
