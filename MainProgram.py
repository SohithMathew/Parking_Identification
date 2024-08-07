import sys
import os
# from InstallWindow import InstallWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = InstallWindow()
    # window.show()
    pix = QPixmap("Parkinn_logo.jpg")
    splassh = QSplashScreen(pix, Qt.WindowStaysOnTopHint)
    splassh.show()
    QTimer.singleShot(3000, splassh.close)  # 3000 milliseconds = 3 seconds
    # QTimer.singleShot(3000, show_main_window)
    print("Opening login screen...")
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())