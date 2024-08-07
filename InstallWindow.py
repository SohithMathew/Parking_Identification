# from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
# from LoginWindow import LoginScreen
# import json
# from DataBaseOperation import DBOperation
# from encryption_helper import hash_password
#
# class InstallWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Install Vehicle Parking System")
#         self.resize(400, 200)
#
#         layout = QVBoxLayout()
#
#         label_db_name = QLabel("Database Name : ")
#         label_db_name.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#         label_db_username = QLabel("Database Username : ")
#         label_db_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#         label_db_password = QLabel("Database Password : ")
#         label_db_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#         label_admin_username = QLabel("Admin Username : ")
#         label_admin_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#         label_admin_password = QLabel("Admin Password : ")
#         label_admin_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#         label_no_of_two_seater = QLabel("No of Two Wheeler Space : ")
#         label_no_of_two_seater.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#         label_no_of_four_seater = QLabel("No. of Four Wheeler Space : ")
#         label_no_of_four_seater.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
#
#         self.input_db_name = QLineEdit()
#         self.input_db_name.setText("vehicle_parking")
#         self.input_db_name.setStyleSheet("padding:5px;font-size:17px")
#
#         self.input_db_username = QLineEdit()
#         self.input_db_username.setText("vehicle")
#         self.input_db_username.setStyleSheet("padding:5px;font-size:17px")
#
#         self.input_db_password = QLineEdit()
#         self.input_db_password.setText("vehicle_password")
#         self.input_db_password.setStyleSheet("padding:5px;font-size:17px")
#
#         self.input_admin_username = QLineEdit()
#         self.input_admin_username.setStyleSheet("padding:5px;font-size:17px")
#         self.input_admin_password = QLineEdit()
#         self.input_admin_password.setStyleSheet("padding:5px;font-size:17px")
#         self.input_two_wheeler = QLineEdit()
#         self.input_two_wheeler.setStyleSheet("padding:5px;font-size:17px")
#         self.input_four_wheeler = QLineEdit()
#         self.input_four_wheeler.setStyleSheet("padding:5px;font-size:17px")
#
#         button_save = QPushButton("Save Config")
#         button_save.setStyleSheet("padding:5px;font-size:17px;background:green;color:#fff")
#         button_open_login = QPushButton("Login")
#         button_open_login.setStyleSheet("padding:5px;font-size:17px;background:blue;color:#fff")
#
#         self.error_label = QLabel()
#         self.error_label.setStyleSheet("color:red")
#
#         layout.addWidget(label_db_name)
#         layout.addWidget(self.input_db_name)
#         layout.addWidget(label_db_username)
#         layout.addWidget(self.input_db_username)
#         layout.addWidget(label_db_password)
#         layout.addWidget(self.input_db_password)
#         layout.addWidget(label_admin_username)
#         layout.addWidget(self.input_admin_username)
#         layout.addWidget(label_admin_password)
#         layout.addWidget(self.input_admin_password)
#         layout.addWidget(label_no_of_two_seater)
#         layout.addWidget(self.input_two_wheeler)
#         layout.addWidget(label_no_of_four_seater)
#         layout.addWidget(self.input_four_wheeler)
#         layout.addWidget(button_save)
#         layout.addWidget(button_open_login)
#         layout.addWidget(self.error_label)
#
#         button_save.clicked.connect(self.saveConfig)
#         button_open_login.clicked.connect(self.openLoginScreen)
#
#         self.setLayout(layout)
#
#     def saveConfig(self):
#         db_name = self.input_db_name.text()
#         db_username = self.input_db_username.text()
#         db_password = self.input_db_password.text()
#         admin_username = self.input_admin_username.text()
#         admin_password = self.input_admin_password.text()
#         two_wheeler = self.input_two_wheeler.text()
#         four_wheeler = self.input_four_wheeler.text()
#
#         if not db_name or not db_username or not db_password or not admin_username or not admin_password or not two_wheeler or not four_wheeler:
#             self.error_label.setText("All fields are required!")
#             return
#
#         salt, hashed_password = hash_password(admin_password)
#
#         config = {
#             "db_name": db_name,
#             "db_username": db_username,
#             "db_password": db_password,
#             "admin_username": admin_username,
#             "admin_password": hashed_password,
#             "salt": salt,
#             "two_wheeler": two_wheeler,
#             "four_wheeler": four_wheeler
#         }
#
#         try:
#             with open("config.json", "w") as config_file:
#                 json.dump(config, config_file)
#             self.error_label.setText("Configuration saved successfully.")
#         except Exception as e:
#             self.error_label.setText(f"Error saving configuration: {e}")
#
#
