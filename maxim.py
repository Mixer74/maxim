import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5 import QtCore

class FullscreenWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fullscreen Window")
        self.setWindowState(self.windowState() | QtCore.Qt.WindowFullScreen)
        self.resize(1920, 1080)  # Установка размера окна

        layout = QVBoxLayout()

        text_label = QLabel('''this is not a real VSC you are too cute HWHAHAHAHAHAHAHAHAHAHAHAHAHA
A problem has been detected and Windows has been shut down to prevent damage
to your computer.

The problem seems to be caused by the following file: xNtKrnl.exe

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Windows updates you might need.

If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use safe mode to remove or disable components, restart
your computer, press F8 to select Advanced Startup Options, and then
select Safe Mode.

Technical Information:

*** STOP: 0x1000007e (0xffffffffc0000005, 0xfffff80002e55151, 0xfffff880009a99d8,
0xfffff880009a9230)

*** xNtKrnl.exe - Address 0xfffff80002e55151 base at 0xfffff80002e0d000 DateStamp
0x4ce7951a''', self)
        font = QFont("Consolas")  # Установка шрифта
        font.setBold(True)
        font.setPointSize(20)  # Установка размера шрифта
        text_label.setFont(font)
        text_label.setStyleSheet("color: white;")
        layout.addWidget(text_label)

        self.setLayout(layout)
        self.setStyleSheet("background-color: blue;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullscreenWindow()
    window.showFullScreen()
    sys.exit(app.exec_())