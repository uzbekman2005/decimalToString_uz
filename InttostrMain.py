from PyQt6.QtWidgets import QMainWindow,QApplication, QMessageBox
from inttostr import *
from intToStr import *
import sys
"""
This program convertes decimals into string form of then in uzbek language
"""
class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineINput.textChanged.connect(self.makeVisible)

    def lengthError(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("ERROR")
        msg.setText("Sonlar xonasi oshib kettidi!!!")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        res = msg.exec()


    def makeVisible(self):
        temp = self.ui.lineINput.text()
        if len(temp) > 10:
            self.lengthError()
            self.ui.labeloutput.setText("Null")
            self.ui.lineINput.setText("")
        if temp =="":
            temp = "0"
            self.ui.labeloutput.setText("Null")
        if self.ui.lineINput.text().isdigit():
            self.ui.labeloutput.setText(IntToStr(int(temp)).converter())
def main():
    app = QApplication([])
    window =Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()