import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class TranslucentWidgetSignals(QtCore.QObject):
    # SIGNALS
    CLOSE = QtCore.pyqtSignal()

class TranslucentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TranslucentWidget, self).__init__(parent)

        # make the window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        labelA = QLabel(self)
        labelA.setText('Please Enter All Values')
        labelA.move(400, 250)
        labelA.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')

##        labelB = QLabel(self)
##        labelB.setText('or less than ambient temperature')
##        labelB.move(380, 280)
##        labelB.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')


        btn = QPushButton('close', self)
        btn.setStyleSheet("background-color:#4299ff;color:white;font-family:Arial;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
        btn.resize(150,50)
        btn.move(420, 320)
        btn.clicked.connect(self._onclose)

        self.fillColor = QtGui.QColor(255, 255, 255, 120)
        self.penColor = QtGui.QColor("#33333")

        self.popup_fillColor = QtGui.QColor(255, 255, 255, 255)
        self.popup_penColor = QtGui.QColor(200, 200, 200, 255)

        self.SIGNALS = TranslucentWidgetSignals()

##    def resizeEvent(self, event):
##        s = self.size()
##        popup_width = 1024
##        popup_height = 500
####        ow = int(s.width() / 2 - popup_width / 2)
####        oh = int(s.height() / 2 - popup_height / 2)
####        self.close_btn.move(ow + 265, oh + 5)

    def paintEvent(self, event):
        # This method is, in practice, drawing the contents of
        # your window.

        # get current window size
        s = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setPen(self.penColor)
        qp.setBrush(self.fillColor)
        qp.drawRect(0, 0, s.width(), s.height())

        # drawpopup
        qp.setPen(self.popup_penColor)
        qp.setBrush(self.popup_fillColor)
        popup_width = 500
        popup_height = 200
        ow = int(s.width()/2-popup_width/2)
        oh = int(s.height()/2-popup_height/2)
        qp.drawRoundedRect(ow, oh, popup_width, popup_height, 5, 5)

        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        qp.setFont(font)
        qp.setPen(QtGui.QColor(70, 70, 70))
        tolw, tolh = 80, -5
        qp.drawText(ow + int(popup_width/2) - tolw, oh + int(popup_height/2) - tolh, " ")

        qp.end()

    def _onclose(self):
        print("Close")
        main.close()






import sys
app = QtWidgets.QApplication(sys.argv)
main = TranslucentWidget()
main.setGeometry(7,30,1024, 600)
main.show()
sys.exit(app.exec_())
